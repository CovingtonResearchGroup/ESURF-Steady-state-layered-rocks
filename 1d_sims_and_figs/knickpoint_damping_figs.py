import cPickle as pickle
from pylab import *

####################################
# Knickpoint damping figure (Fig 9)#
####################################

#Panel A
#n=1.2
res = pickle.load(open('damping_high_1.2.pkl','rb'))
chi = res['chi']
elev = res['elev']
start_soft = res['start_soft']
end_soft = res['end_soft']
start_soft_chi = res['start_soft_chi']
end_soft_chi = res['end_soft_chi']
uplift = res['uplift']
x = res['x']/1000. #convert to km
figure(figsize=(8,8))
subplot(2,2,1)
idx = 452 #final timestep before duration was reached
nstep = 4
plot(chi,elev[idx], 'k', lw=2)
ax = gca()
ax1 = ax #save for use in shared axis
for i, lly in enumerate(end_soft[idx]):
    r = Rectangle((0,lly),200,start_soft[idx][i]-lly,color='grey',alpha=.5)
    ax.add_patch(r)
plot([2.45,2.45], [0,1000], 'r',lw=3)
xlabel('$\chi$ [m]',fontsize=16)
ylabel('Elevation [m]',fontsize=12)
xlim([0,12])
ylim([0,600])
text(0.05,0.85,'A', fontsize=20, transform=gca().transAxes)
bbox_props = dict(boxstyle='round', fc="w",alpha=1.0, ec="k")
text(0.07,0.67,'n=1.2', fontsize=14, transform=gca().transAxes,bbox=bbox_props)
tight_layout()

#Panel C
subplot(2,2,3)
idx = 452 #final timestep before duration was reached
nstep = 4
plot(chi,elev[idx], 'k--', lw=2)
plot(chi,elev[idx-nstep], 'k:', lw=2)
plot(chi,elev[idx+nstep], 'k', lw=2)
ax = gca()
ax1 = ax #save for use in shared axis
plot([2.45,2.45], [0,250], 'r', lw=3)
xlabel('$\chi$ [m]',fontsize=16)
ylabel('Elevation [m]',fontsize=12)
xlim([0,3])
ylim([0,200])
text(0.05,0.85,'C', fontsize=20, transform=gca().transAxes)
bbox_props = dict(boxstyle='round', fc="w",alpha=1.0, ec="k")
text(0.07,0.67,'n=1.2', fontsize=14, transform=gca().transAxes,bbox=bbox_props)
tight_layout()

#Panel B
#n=0.8
res = pickle.load(open('damping_med_0.8_long.pkl','rb'))
chi = res['chi']
elev = res['elev']
start_soft = res['start_soft']
end_soft = res['end_soft']
uplift = res['uplift']
x = res['x']/1000.
subplot(2,2,2)
idx = 434
nstep = 4
plot(chi,elev[idx], 'k', lw=2)
plot([2.25,2.25], [0,1000], 'r', lw=3)
ax = gca()
for i, lly in enumerate(end_soft[idx]):
    r = Rectangle((0,lly),200,start_soft[idx][i]-lly,color='grey',alpha=.5)
    ax.add_patch(r)
xlabel('$\chi$ [m]',fontsize=16)
ylabel('Elevation [m]',fontsize=12)
xlim([0,12])
ylim([0,550])
bbox_props = dict(boxstyle='round', fc="w",alpha=1.0, ec="k")
text(0.07,0.67,'n=0.8', fontsize=14, transform=gca().transAxes,bbox=bbox_props)
text(0.05,0.85,'B', fontsize=20, transform=gca().transAxes)
tight_layout()
#Panel D
subplot(2,2,4)
idx = 434
nstep = 4
plot(chi,elev[idx], 'k--', lw=2)
plot(chi,elev[idx-nstep-2], 'k:', lw=2)
plot(chi,elev[idx+nstep], 'k', lw=2)
plot([2.25,2.25], [0,250], 'r', lw=3)
ax = gca()
xlabel('$\chi$ [m]',fontsize=16)
ylabel('Elevation [m]',fontsize=12)
xlim([0,3])
ylim([0,175])
bbox_props = dict(boxstyle='round', fc="w",alpha=1.0, ec="k")
text(0.07,0.67,'n=0.8', fontsize=14, transform=gca().transAxes,bbox=bbox_props)
text(0.05,0.85,'D', fontsize=20, transform=gca().transAxes)
tight_layout()
savefig('fig9.pdf')
