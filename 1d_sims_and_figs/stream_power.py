from numpy import arange,zeros,ones,linspace,mean,size,logical_and
import cPickle as pickle
################################################
#General function for stream power simulations #
################################################

def stream_erode(outputfile = 'output-test.pkl',n=2./3., m=1./3.,
                 K1=1e-4,KR=2.0,uplift=0.0025,
                 thickness=50.,two_layers=100.,nx=2000.,nskip=100,
                 dx=5.,nt = 50000,A0 = 1., x0=2500.,
                 h = 1.67, 
                 k_a = 6.69,#value from Whipple+Tucker (1999) and Hack (1957)
                 duration=10000./0.0025):

    #K2 is calculated from K1 and a multiplying factor (KR)
    K2 = KR*K1
    x = dx*arange(nx) + x0
    A = k_a*(x)**h#A0 + x**A_power
    Am = A**m
    elevations=linspace(10.,1.,nx)
    elev_rec = zeros([round(nt/nskip),nx])
    time_rec = zeros(round(nt/nskip))
    uplift_rec = zeros(round(nt/nskip))
    CFL_crit=0.9 #timestep adjusted to produce this Courant-Friedrich-Lax number
    times=zeros(nt)
    recnum=0
    E1=[]
    E1_avg = []
    E2=[]
    E2_avg = []
    tot_uplift =0.
    start_soft_rec = []
    end_soft_rec = []
    start_soft_chi_rec = []
    end_soft_chi_rec = []
    #Calculate chi's
    chi = zeros(nx)
    for i in arange(nx):
        chi[i] = sum((A0/A[i:])**(m/n)*dx)
    duration_reached = False
    laststep = False
    nstep_after = 0
    rec_this=False
    for i in arange(nt-1):
        if not laststep:
            K=K1*ones(nx)
            where_soft = (elevations-uplift*times[i]) % two_layers < thickness
            K[where_soft] = K2
            slope = (elevations[:-1]-elevations[1:])/dx
            C = K[:-1]*Am[:-1]*slope**(n-1)
            #set timestep for stable CFL criteria
            dt = CFL_crit*dx/max(abs(C))
            if (times[i]+dt > duration) and not duration_reached:
                dt = duration - times[i]
                duration_reached = True
                rec_this=True
            if times[i]>duration:
                rec_this=False
                if nstep_after==nskip*2:
                    laststep=True
                nstep_after += 1
            times[i+1] = times[i] + dt
            erosion = -dt*K[:-1]*(Am[:-1])*(slope)**n
            elevations[:-1] += erosion + uplift*dt
            tot_uplift += uplift*dt
            E1.append(mean(erosion[~where_soft[:-1]]/dt))
            E2.append(mean(erosion[where_soft[:-1]]/dt))
            if ((i % nskip) == 0) or rec_this:
                print "Recording timestep:", i
                #record elevations
                elev_rec[recnum]=elevations
                time_rec[recnum]=times[i]
                uplift_rec[recnum]=tot_uplift
                #keep track of locations of soft and hard layers
                start_soft = []
                end_soft = []
                start_soft_chi = []
                end_soft_chi = []
                for j,is_soft in enumerate(where_soft):
                    if is_soft:
                        if j==0:
                            start_soft.append(elevations[j])
                            start_soft_chi.append(chi[j])
                        if j>0:
                            if where_soft[j-1] == False:
                                start_soft.append(elevations[j])
                                start_soft_chi.append(chi[j])
                        if j<(size(where_soft)-1):
                            if where_soft[j+1] == False:
                                end_soft.append(elevations[j])
                                end_soft_chi.append(chi[j])
                        if j==size(where_soft)-1:
                            end_soft.append(elevations[j])
                            end_soft_chi.append(chi[j])
                start_soft_rec.append(start_soft)
                end_soft_rec.append(end_soft)
                start_soft_chi_rec.append(start_soft_chi)
                end_soft_chi_rec.append(end_soft_chi)
                E1_avg.append(mean(E1))
                E2_avg.append(mean(E2))
                E1 = []
                E2 = []
                recnum+=1

 
    results = {'elev':elev_rec,'time':time_rec, 'uplift':uplift_rec, 'chi':chi, 'x':x, 'A':A, 'start_soft':start_soft_rec,'end_soft':end_soft_rec,'start_soft_chi':start_soft_chi_rec,'end_soft_chi':end_soft_chi_rec}
    pickle.dump(results, open(outputfile,'wb'))
    return results

