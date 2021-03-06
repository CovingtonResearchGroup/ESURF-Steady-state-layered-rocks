################################################################
## This script documents the process to create                ##
##  Figure 10, but will not run without correct file names    ##
##  that link to outputs of DEMImport_v2 and Fastscape images ##
################################################################
from pylab import *
import pickle
matplotlib.use('Agg')
from landlab.plot import channel_profile as prf
from landlab.plot import imshow as llplot
from landlab.plot.imshow import imshow_node_grid
from matplotlib import image

def theoreticalprofile(K1, K2, H1, H2, U, nlayers, unit_area = 1., m = 0.5, n = 1, hshift = 0):
	if(abs(n-1)>1E-6):
		ratio = (K1/K2)**(1/(1-n))
		E2 = U*(H1 + ratio * H2)/(ratio*(H1+H2))
		E1 = ratio * E2
		
		Sx1 = (E1/K1)**(1/n) * unit_area**(n/m)
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
		return 0


#####################################################################
#File names here will have to be changed to reflect names of desired
# pickle files to process, which are output from DEMImport_v2.py
#####################################################################
pids_neq1 = open('13/chan-ids_neq1.p','rb')
profile_IDs_neq1 = pickle.load(pids_neq1)
d_ups_neq1 = open('13/dists-up-alternative_neq1.p','rb')
dists_upstr_neq1 = pickle.load(d_ups_neq1)
elevs_neq1 = open('13/topo_elev_neq1.p','rb')
topo_elevs_neq1 = pickle.load(elevs_neq1)

pids_nl1 = open('23/chan-ids_nl1.p','rb')
profile_IDs_nl1 = pickle.load(pids_nl1)
d_ups_nl1 = open('23/dists-up_nl1.p','rb')
dists_upstr_nl1 = pickle.load(d_ups_nl1)
elevs_nl1 = open('23/topo_elev_nl1.p','rb')
topo_elevs_nl1 = pickle.load(elevs_nl1)

pids_ng1 = open('32/chan-ids_ng1.p','rb')
profile_IDs_ng1 = pickle.load(pids_ng1)
d_ups_ng1 = open('32/dists-up_ng1.p','rb')
dists_upstr_ng1 = pickle.load(d_ups_ng1)
elevs_ng1 = open('32/topo_elev_ng1.p','rb')
topo_elevs_ng1 = pickle.load(elevs_ng1)

figure(figsize=(12,18))

#Panel A
subplot(3,2,1)#,adjustable='box')
prf.plot_profiles(dists_upstr_nl1, profile_IDs_nl1,topo_elevs_nl1)
profile = theoreticalprofile(K2 = 1.2E-4, K1 = 0.5 * 1.2E-4, H1 = 200, H2 = 300, U = 2.5E-3, nlayers = 6, m = 0.3333, n = 0.6667, hshift = -0.75)
plot(profile[:,0],profile[:,1], 'k--o',lw=2,ms=4)
xlim([0,20])
ylabel('Elevation [m]',fontsize=20)
xlabel('$\chi$ [m]',fontsize=16)
axhspan(200,500, color='k', alpha = 0.3, lw=0)
axhspan(700,1000, color='k', alpha = 0.3, lw=0)
axhspan(1200,1500, color='k', alpha = 0.3, lw=0)
axhspan(1700,2000, color='k', alpha = 0.3, lw=0)
axhspan(2200,2500, color='k', alpha = 0.3, lw=0)
axhspan(2700,3000, color='k', alpha = 0.3, lw=0)
text(0.05,0.9,'A', fontsize=25, transform=gca().transAxes)
bbox_props = dict(boxstyle='round', fc="w",alpha=0.9, ec="k")
text(0.07,0.75,'n=2/3', fontsize=20, transform=gca().transAxes,bbox=bbox_props)
text(30,750,'weak rocks', fontsize=20)
#text(125,115,'weak rocks', fontsize=12)
#text(0.05,0.85,'B', fontsize=20, transform=gca().transAxes)
#bbox_props = dict(boxstyle='round', fc="w",alpha=0.9, ec="k")
#text(0.07,0.67,'n=0.7', fontsize=14, transform=gca().transAxes,bbox=bbox_props)
tight_layout(h_pad=1)
#Panel B
subplot(3,2,3)#,adjustable='box')
prf.plot_profiles(dists_upstr_ng1, profile_IDs_ng1,topo_elevs_ng1 )
profile = theoreticalprofile(K2 = 1E-6, K1 = 0.5 * 1E-6, H1 = 200, H2 = 300, U = 2.5E-3, nlayers = 5, m = 0.75, n = 1.5, hshift = 0.4)
plot(profile[:,0],profile[:,1], 'k--o',lw=2,ms=4)

ylabel('Elevation [m]',fontsize=20)
xlabel('$\chi$ [m]',fontsize=16)
axhspan(200,500, color='k', alpha = 0.3, lw=0)
axhspan(700,1000, color='k', alpha = 0.3, lw=0)
axhspan(1200,1500, color='k', alpha = 0.3, lw=0)
axhspan(1700,2000, color='k', alpha = 0.3, lw=0)
axhspan(2200,2500, color='k', alpha = 0.3, lw=0)
axhspan(2700,3000, color='k', alpha = 0.3, lw=0)
axhspan(3200,3500, color='k', alpha = 0.3, lw=0)
text(0.05,0.90,'C', fontsize=25, transform=gca().transAxes)
text(0.07,0.75,'n=3/2', fontsize=20, transform=gca().transAxes,bbox=bbox_props)
text(800,750,'weak rocks', fontsize=20)
#text(125,115,'weak rocks', fontsize=12)
#text(0.05,0.85,'C', fontsize=20, transform=gca().transAxes)
#bbox_props = dict(boxstyle='round', fc="w",alpha=0.9, ec="k")
#text(0.07,0.67,'n=1.2', fontsize=14, transform=gca().transAxes,bbox=bbox_props)
tight_layout(h_pad=1)
#Panel C
subplot(3,2,5)#,adjustable='box')
prf.plot_profiles(dists_upstr_neq1, profile_IDs_neq1,topo_elevs_neq1 )
ylabel('Elevation [m]',fontsize=20)
xlabel('$\chi$ [m]',fontsize=16)
axhspan(200,500, color='k', alpha = 0.3, lw=0)
axhspan(700,1000, color='k', alpha = 0.3, lw=0)
axhspan(1200,1500, color='k', alpha = 0.3, lw=0)
axhspan(1700,2000, color='k', alpha = 0.3, lw=0)
axhspan(2200,2500, color='k', alpha = 0.3, lw=0)
text(300,300,'weak rocks', fontsize=20)
text(0.05,0.90,'E', fontsize=25, transform=gca().transAxes)
text(0.07,0.75,'n=1', fontsize=20, transform=gca().transAxes,bbox=bbox_props)
tight_layout(h_pad=1)

#plt.axhspan(1700,2000, color='k', alpha = 0.3, lw=0)
#plt.axhspan(2200,2500, color='k', alpha = 0.3, lw=0)	                  
#savefig('./supp-prf-fig.pdf')
#show()
#close()

#Make DEM plots
#File names here need to be changed to desired images of dems
subplot(3,2,2)
img1 = image.imread('23/nl1-Topo2-small.png')
imshow(img1, interpolation='none')
text(0.77,0.89,'n=2/3', fontsize=20, transform=gca().transAxes,bbox=bbox_props)
text(0.07,0.88,'B', fontsize=25, transform=gca().transAxes,bbox=bbox_props)
xlabel('Node number')
ylabel('Node number')
tight_layout(h_pad=1)
subplot(3,2,4)
img2 = image.imread('32/ng1-Topo2-small.png')
imshow(img2, interpolation='none')
text(0.07,0.88,'D', fontsize=25, transform=gca().transAxes,bbox=bbox_props)
text(0.77,0.89,'n=3/2', fontsize=20, transform=gca().transAxes,bbox=bbox_props)
xlabel('Node number')
ylabel('Node number')
tight_layout(h_pad=1)
subplot(3,2,6)
img3 = image.imread('11/neq1-Topo2-small.png')
imshow(img3, interpolation='none')
text(0.07,0.88,'F', fontsize=25, transform=gca().transAxes,bbox=bbox_props)
text(0.77,0.89,'n=1', fontsize=20, transform=gca().transAxes,bbox=bbox_props)
xlabel('Node number')
ylabel('Node number')
tight_layout(h_pad=1)
#show()
savefig('Fastscape-results_3.pdf',dpi=300)
