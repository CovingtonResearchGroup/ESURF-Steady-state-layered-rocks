import cPickle as pickle
#from matplotlib.patches import Rectangle
#from matplotlib.pyplot import gca,tight_layout,figure,plot
from pylab import *

#####################################
# Function to calculate theoretical #
# profiles from continuity and      #
# flux steady state assumptions     #
#####################################
def theoreticalprofile(K1, K2, H1, H2, U, nlayers, unit_area = 1., m = 0.5, n = 1, hshift = 0):
	if(abs(n-1)>1E-6):
		ratio = (K1/K2)**(1/(1-n))
		E2 = U*(H1 + ratio * H2)/(ratio*(H1+H2))
		E1 = ratio * E2
		
		Sx1 = (E1/K1)**(1/n) * unit_area**(n/m)
		#E2 = U*((H2/H1) + (K2/K1)**(1/(1-n)))/(1 + H2/H1)
		#E2 = U * H2 / (H1 + H2 - H1 * U / E1)
		Sx2 = (E2/K2)**(1/n) * unit_area**(n/m)
		output = empty([2*nlayers+1,2])
		output[0,0]=hshift
		output[0,1]=0
		for i in range(nlayers):
			output[2*i+1,0]=output[2*i,0] + H1/Sx1
			output[2*i+2,0]=output[2*i+1,0] + H2/Sx2
			output[2*i+1,1]=output[2*i,1] + H1
			output[2*i+2,1]=output[2*i+1,1] + H2
		return output
	else:
		Sx1 = U/K1 * unit_area**(n/m)
		Sx2 = U/K2 * unit_area**(n/m)
		#print Sx1, Sx2
		output = empty([4*nlayers+2,2])
		output[0,0]=hshift
		output[0,1]=0
		output[1,0]=hshift
		output[1,1]=0
		for i in range(nlayers):
			output[4*i+2,0]=output[4*i+1,0] + H1/Sx1
			output[4*i+2,1]=output[4*i+1,1] + H1
			output[4*i+3,0]=output[4*i,0] + H1/Sx2
			output[4*i+3,1]=output[4*i,1] + H1

			output[4*i+4,0]=output[4*i+3,0] + H2/Sx2
			output[4*i+4,1]=output[4*i+3,1] + H2
			output[4*i+5,0]=output[4*i+2,0] + H2/Sx1
			output[4*i+5,1]=output[4*i+2,1] + H2
			
		for i in range(nlayers):
			output[4*i+4,0]=output[4*i+5,0]
			output[4*i+4,1]=output[4*i+3,1] + Sx2 * (output[4*i+4,0]-output[4*i+3,0])
		return output
#############################################
#Figure 3 (slope ratios as a function of n)
#############################################
figure(figsize=(5,4))
n=linspace(0.5,2.0,50)
k_w=2.
k_s=1.
k_w2 = 4.
k_w3 = 1.25
s_ratio = (k_w/k_s)**(1./(1.-n))
s_ratio_trad = (k_s/k_w)**(1./n)
s_ratio2 = (k_w2/k_s)**(1./(1.-n))
s_ratio_trad2 = (k_s/k_w2)**(1./n)
s_ratio3 = (k_w3/k_s)**(1./(1.-n))
s_ratio_trad3 = (k_s/k_w3)**(1./n)
big = s_ratio>1
small = s_ratio<1
semilogy(n[big],s_ratio[big],'-k',lw=2)
semilogy(n,s_ratio_trad,'--k',lw=2)
semilogy(n[small],s_ratio[small],'-k',lw=2)
plot([0.5,2.0],[1,1],':k',lw=1)
plot([1,1],[1e-5,1e5],':k',lw=1)
ylim([10**-3,10**3])
xlim([.5,2.0])
legend(['Horizontal contacts','Vertical contacts'],loc='upper right',fontsize=10.)
xlabel('$n$ value in Erosion law',fontsize=12)
ylabel('$S_w/S_s$',fontsize=14)
tight_layout()
savefig('fig3.pdf')

#################################################
#Stream profile figures (high uplift, Figure 4) #
#################################################

#Panel a
#n=2/3
figure(figsize=(9,6))
res = pickle.load(open('high_uplift_0.66.pkl','rb'))
chi = res['chi']
elev = res['elev']
start_soft = res['start_soft']
end_soft = res['end_soft']
start_soft_chi = res['start_soft_chi']
end_soft_chi = res['end_soft_chi']
uplift = res['uplift']
x = res['x']/1000. #convert to km
subplot(2,3,1)
idx = 450 #final timestep before duration was reached
nstep = 15
plot(chi,elev[idx], color='black', lw=2)
plot(chi,elev[idx-nstep]-uplift[idx-nstep]+uplift[idx], 'k', lw=2)
plot(chi,elev[idx+nstep]-uplift[idx+nstep]+uplift[idx], 'k', lw=2)
ax = gca()
ax1 = ax #save for use in shared axis
for i, lly in enumerate(end_soft[idx]):
    r = Rectangle((0,lly),200,start_soft[idx][i]-lly,color='grey',alpha=.5)
    ax.add_patch(r)
xlabel('$\chi$ [m]',fontsize=16)
ylabel('Elevation [m]',fontsize=12)
xlim([0,7])
ylim([0,600])
text(4,210,'weak rocks', fontsize=12)
text(0.05,0.85,'A', fontsize=20, transform=gca().transAxes)
bbox_props = dict(boxstyle='round', fc="w",alpha=0.9, ec="k")
text(0.07,0.67,'n=2/3', fontsize=14, transform=gca().transAxes,bbox=bbox_props)
#plot theoretical profile
profile = theoreticalprofile(2e-4,1e-4,50,50,2.5e-3,6,m=.33,n=2./3., unit_area=1.)
plot(profile[:,0],profile[:,1], 'k--o',ms=4)
tight_layout()

#Panel D
subplot(2,3,4)
idx = 450 #final timestep before duration was reached
nstep = 15
plot(x,elev[idx], color='black', lw=2)
plot(x,elev[idx-nstep]-uplift[idx-nstep]+uplift[idx], 'k', lw=2)
plot(x,elev[idx+nstep]-uplift[idx+nstep]+uplift[idx], 'k', lw=2)
ax = gca()
ax2 = ax #save for shared axis
ax.invert_xaxis()
for i, lly in enumerate(end_soft[idx]):
    r = Rectangle((0,lly),200,start_soft[idx][i]-lly,color='grey',alpha=.5)
    ax.add_patch(r)
xlabel('Distance from divide [km]',fontsize=12)
ylabel('Elevation [m]',fontsize=12)
xlim([50,0])
ylim([0,600])
text(45,310,'weak rocks', fontsize=12)
text(0.05,0.85,'D', fontsize=20, transform=gca().transAxes)
bbox_props = dict(boxstyle='round', fc="w",alpha=0.9, ec="k")
text(0.07,0.67,'n=2/3', fontsize=14, transform=gca().transAxes,bbox=bbox_props)
tight_layout()

#Panel B
#n=3/2
res = pickle.load(open('high_uplift_1.5.pkl','rb'))
chi = res['chi']
elev = res['elev']
start_soft = res['start_soft']
end_soft = res['end_soft']
uplift = res['uplift']
x = res['x']/1000.
subplot(2,3,2,sharey=ax1)
idx = 445
nstep = 15
plot(chi,elev[idx], color='black', lw=2)
plot(chi,elev[idx-nstep-2]-uplift[idx-nstep-2]+uplift[idx], 'k', lw=2)
plot(chi,elev[idx+nstep]-uplift[idx+nstep]+uplift[idx], 'k', lw=2)
ax = gca()
for i, lly in enumerate(end_soft[idx]):
    r = Rectangle((0,lly),200,start_soft[idx][i]-lly,color='grey',alpha=.5)
    ax.add_patch(r)
xlabel('$\chi$ [m]',fontsize=16)
xlim([0,7])
ylim([0,600])
setp(ax.get_yticklabels(), visible=False)
bbox_props = dict(boxstyle='round', fc="w",alpha=0.9, ec="k")
text(0.07,0.67,'n=3/2', fontsize=14, transform=gca().transAxes,bbox=bbox_props)
text(4,210,'weak rocks', fontsize=12)
text(0.05,0.85,'B', fontsize=20, transform=gca().transAxes)
#make theoretical profile
profile = theoreticalprofile(3e-6,1.5e-6,50,50,2.5e-3,6,m=.75,n=3./2., unit_area=1.)
plot(profile[:,0],profile[:,1], 'k--o',ms=4)
tight_layout()

#Panel e
subplot(2,3,5, sharey=ax2)
plot(x,elev[idx], color='black', lw=2)
plot(x,elev[idx-nstep-2]-uplift[idx-nstep-2]+uplift[idx], 'k', lw=2)
plot(x,elev[idx+nstep]-uplift[idx+nstep]+uplift[idx], 'k', lw=2)
ax = gca()
for i, lly in enumerate(end_soft[idx]):
    r = Rectangle((0,lly),200,start_soft[idx][i]-lly,color='grey',alpha=.5)
    ax.add_patch(r)
ax.invert_xaxis()
setp(ax.get_yticklabels(), visible=False)
xlabel('Distance from divide [km]',fontsize=12)
xlim([50,0])
ylim([0,600])
bbox_props = dict(boxstyle='round', fc="w",alpha=0.9, ec="k")
text(0.07,0.67,'n=3/2', fontsize=14, transform=gca().transAxes,bbox=bbox_props)
text(45,310,'weak rocks', fontsize=12)
text(0.05,0.85,'E', fontsize=20, transform=gca().transAxes)

#Panel C
#n=1
res = pickle.load(open('high_uplift_1.pkl','rb'))
chi = res['chi']
elev = res['elev']
start_soft = res['start_soft']
end_soft = res['end_soft']
uplift = res['uplift']
x = res['x']/1000.
subplot(2,3,3, sharey=ax1)
idx = 445
nstep = 20
plot(chi,elev[idx], color='black', lw=2)
plot(chi,elev[idx-nstep-1]-uplift[idx-nstep-1]+uplift[idx], 'k', lw=2)
plot(chi,elev[idx+nstep]-uplift[idx+nstep]+uplift[idx], 'k', lw=2)
ax = gca()
for i, lly in enumerate(end_soft[idx]):
    r = Rectangle((0,lly),200,start_soft[idx][i]-lly,color='grey',alpha=.5)
    ax.add_patch(r)
xlabel('$\chi$ [m]',fontsize=16)
#ylabel('Elevation [m]',fontsize=12)
xlim([0,7])
ylim([0,600])
setp(ax.get_yticklabels(), visible=False)
bbox_props = dict(boxstyle='round', fc="w",alpha=0.9, ec="k")
text(0.07,0.67,'n=1', fontsize=14, transform=gca().transAxes,bbox=bbox_props)
text(4,210,'weak rocks', fontsize=12)
text(0.05,0.85,'C', fontsize=20, transform=gca().transAxes)
tight_layout()

#Panel f
subplot(2,3,6,sharey=ax2)
plot(x,elev[idx], color='black', lw=2)
plot(x,elev[idx-nstep-1]-uplift[idx-nstep-1]+uplift[idx], 'k', lw=2)
plot(x,elev[idx+nstep]-uplift[idx+nstep]+uplift[idx], 'k', lw=2)
ax = gca()
for i, lly in enumerate(end_soft[idx]):
    r = Rectangle((0,lly),200,start_soft[idx][i]-lly,color='grey',alpha=.5)
    ax.add_patch(r)
ax.invert_xaxis()
xlabel('Distance from divide [km]',fontsize=12)
#ylabel('Elevation [m]',fontsize=12)
xlim([50,0])
ylim([0,600])
bbox_props = dict(boxstyle='round', fc="w",alpha=0.9, ec="k")
text(0.07,0.67,'n=1', fontsize=14, transform=gca().transAxes,bbox=bbox_props)
text(45,310,'weak rocks', fontsize=12)
text(0.05,0.85,'F', fontsize=20, transform=gca().transAxes)
setp(ax.get_yticklabels(), visible=False)
tight_layout()
savefig('fig4.pdf')


#######################################
## Stream profiles (Low uplift, Fig 5)#
#######################################

#Panel A
#n=2/3
figure(figsize=(9,6))
res = pickle.load(open('low_uplift_0.66.pkl','rb'))
chi = res['chi']
elev = res['elev']
start_soft = res['start_soft']
end_soft = res['end_soft']
start_soft_chi = res['start_soft_chi']
end_soft_chi = res['end_soft_chi']
uplift = res['uplift']
x = res['x']/1000. #convert to km
subplot(2,3,1)
idx = 436 #final timestep before duration was reached
nstep = 15
plot(chi,elev[idx], color='black', lw=2)
plot(chi,elev[idx-nstep]-uplift[idx-nstep]+uplift[idx], 'k', lw=2)
plot(chi,elev[idx+nstep]-uplift[idx+nstep]+uplift[idx], 'k', lw=2)
ax = gca()
ax1 = ax #save for use in shared axis
for i, lly in enumerate(end_soft[idx]):
    r = Rectangle((0,lly),200,start_soft[idx][i]-lly,color='grey',alpha=.5)
    ax.add_patch(r)
xlabel('$\chi$ [m]',fontsize=16)
ylabel('Elevation [m]',fontsize=12)
xlim([0,9])
ylim([0,100])
text(4,210,'weak rocks', fontsize=12)
text(0.05,0.85,'A', fontsize=20, transform=gca().transAxes)
bbox_props = dict(boxstyle='round', fc="w",alpha=0.9, ec="k")
text(0.07,0.67,'n=2/3', fontsize=14, transform=gca().transAxes,bbox=bbox_props)
#plot theoretical profile
profile = theoreticalprofile(8e-5,4e-5,10,10,2.5e-4,5,m=.33,n=2./3., unit_area=1.)
plot(profile[:,0],profile[:,1], 'k--o',ms=4)
tight_layout()

#Panel D
subplot(2,3,4)
plot(x,elev[idx], color='black', lw=2)
plot(x,elev[idx-nstep]-uplift[idx-nstep]+uplift[idx], 'k', lw=2)
plot(x,elev[idx+nstep]-uplift[idx+nstep]+uplift[idx], 'k', lw=2)
ax = gca()
ax2 = ax #save for shared axis
ax.invert_xaxis()
for i, lly in enumerate(end_soft[idx]):
    r = Rectangle((0,lly),200,start_soft[idx][i]-lly,color='grey',alpha=.5)
    ax.add_patch(r)
xlabel('Distance from divide [km]',fontsize=12)
ylabel('Elevation [m]',fontsize=12)
xlim([200,0])
ylim([0,100])
text(45,310,'weak rocks', fontsize=12)
text(0.05,0.85,'D', fontsize=20, transform=gca().transAxes)
bbox_props = dict(boxstyle='round', fc="w",alpha=0.9, ec="k")
text(0.07,0.67,'n=2/3', fontsize=14, transform=gca().transAxes,bbox=bbox_props)
tight_layout()

#Panel B
#n=3/2
res = pickle.load(open('low_uplift_1.5.pkl','rb'))
chi = res['chi']
elev = res['elev']
start_soft = res['start_soft']
end_soft = res['end_soft']
uplift = res['uplift']
x = res['x']/1000.
subplot(2,3,2,sharey=ax1)
idx = 439
nstep = 15
plot(chi,elev[idx], color='black', lw=2)
plot(chi,elev[idx-nstep-2]-uplift[idx-nstep-2]+uplift[idx], 'k', lw=2)
plot(chi,elev[idx+nstep]-uplift[idx+nstep]+uplift[idx], 'k', lw=2)
ax = gca()
for i, lly in enumerate(end_soft[idx]):
    r = Rectangle((0,lly),200,start_soft[idx][i]-lly,color='grey',alpha=.5)
    ax.add_patch(r)
xlabel('$\chi$ [m]',fontsize=16)
xlim([0,9])
ylim([0,100])
setp(ax.get_yticklabels(), visible=False)
bbox_props = dict(boxstyle='round', fc="w",alpha=0.9, ec="k")
text(0.07,0.67,'n=3/2', fontsize=14, transform=gca().transAxes,bbox=bbox_props)
text(4,210,'weak rocks', fontsize=12)
text(0.05,0.85,'B', fontsize=20, transform=gca().transAxes)
#make theoretical profile
profile = theoreticalprofile(6e-6,3e-6,10,10,2.5e-4,5,m=.75,n=3./2., unit_area=1.)
plot(profile[:,0],profile[:,1], 'k--o',ms=4)
tight_layout()
#Panel e
subplot(2,3,5, sharey=ax2)
plot(x,elev[idx], color='black', lw=2)
plot(x,elev[idx-nstep-2]-uplift[idx-nstep-2]+uplift[idx], 'k', lw=2)
plot(x,elev[idx+nstep]-uplift[idx+nstep]+uplift[idx], 'k', lw=2)
ax = gca()
for i, lly in enumerate(end_soft[idx]):
    r = Rectangle((0,lly),200,start_soft[idx][i]-lly,color='grey',alpha=.5)
    ax.add_patch(r)
ax.invert_xaxis()
setp(ax.get_yticklabels(), visible=False)
xlabel('Distance from divide [km]',fontsize=12)
xlim([200,0])
ylim([0,100])
bbox_props = dict(boxstyle='round', fc="w",alpha=0.9, ec="k")
text(0.07,0.67,'n=3/2', fontsize=14, transform=gca().transAxes,bbox=bbox_props)
text(45,310,'weak rocks', fontsize=12)
text(0.05,0.85,'E', fontsize=20, transform=gca().transAxes)

#Panel C
#n=1
res = pickle.load(open('low_uplift_1.pkl','rb'))
chi = res['chi']
elev = res['elev']
start_soft = res['start_soft']
end_soft = res['end_soft']
uplift = res['uplift']
x = res['x']/1000.
subplot(2,3,3, sharey=ax1)
idx = 454
nstep = 20
plot(chi,elev[idx], color='black', lw=2)
plot(chi,elev[idx-nstep-1]-uplift[idx-nstep-1]+uplift[idx], 'k', lw=2)
plot(chi,elev[idx+nstep]-uplift[idx+nstep]+uplift[idx], 'k', lw=2)
ax = gca()
for i, lly in enumerate(end_soft[idx]):
    r = Rectangle((0,lly),200,start_soft[idx][i]-lly,color='grey',alpha=.5)
    ax.add_patch(r)
xlabel('$\chi$ [m]',fontsize=16)
#ylabel('Elevation [m]',fontsize=12)
xlim([0,9])
ylim([0,100])
setp(ax.get_yticklabels(), visible=False)
bbox_props = dict(boxstyle='round', fc="w",alpha=0.9, ec="k")
text(0.07,0.67,'n=1', fontsize=14, transform=gca().transAxes,bbox=bbox_props)
text(4,210,'weak rocks', fontsize=12)
text(0.05,0.85,'C', fontsize=20, transform=gca().transAxes)
tight_layout()
#Panel f
subplot(2,3,6,sharey=ax2)
plot(x,elev[idx], color='black', lw=2)
plot(x,elev[idx-nstep-1]-uplift[idx-nstep-1]+uplift[idx], 'k', lw=2)
plot(x,elev[idx+nstep]-uplift[idx+nstep]+uplift[idx], 'k', lw=2)
ax = gca()
for i, lly in enumerate(end_soft[idx]):
    r = Rectangle((0,lly),200,start_soft[idx][i]-lly,color='grey',alpha=.5)
    ax.add_patch(r)
ax.invert_xaxis()
xlabel('Distance from divide [km]',fontsize=12)
xlim([200,0])
ylim([0,100])
bbox_props = dict(boxstyle='round', fc="w",alpha=0.9, ec="k")
text(0.07,0.67,'n=1', fontsize=14, transform=gca().transAxes,bbox=bbox_props)
text(45,310,'weak rocks', fontsize=12)
text(0.05,0.85,'F', fontsize=20, transform=gca().transAxes)
setp(ax.get_yticklabels(), visible=False)
tight_layout()
savefig('fig5.pdf')
