import matplotlib.pyplot as p
import gc, sys, subprocess
import cPickle as pickle
from matplotlib.patches import Rectangle

#############################################
## Figure with different thicknesses (Fig 7)#
#############################################

#n=3/2 case
res_diff = pickle.load(open('diff_thickness_high_uplift_1.5.pkl', 'rb'))
#simulation frame to display
diff_frame = 138
res_equal = pickle.load(open('high_uplift_1.5.pkl', 'rb'))
#equivalent frame from equal thickness simulation
equal_frame = 143

fig = p.figure(figsize=(9,4))
p.subplot(1,2,1)
p.plot(res_diff['chi'], res_diff['elev'][diff_frame], 'k')
p.plot(res_equal['chi'], res_equal['elev'][equal_frame], 'k--')
p.ylabel('Elevation [m]', fontsize=12)
p.xlabel('$\chi$ [m]', fontsize=16)
p.legend(['Different thickness', 'Equal thickness'], loc='upper left',fontsize=12)

ax = p.gca()
thickness = 90.
for i, lly in enumerate(res_diff['end_soft'][diff_frame]):
    if  (i>0) and (i==len(res_diff['end_soft'][diff_frame])-1): 
        #original code, but we need this for first rectangle
        r = Rectangle((0,lly),200,res_diff['start_soft'][diff_frame][i]-lly,color='grey',alpha=.5)
    else:
        #went to set thickness to avoid jumpiness in movies
        r = Rectangle((0,lly),200,thickness,color='grey',alpha=.5)
    ax.add_patch(r)
bbox_props = dict(boxstyle='round', fc="w",alpha=0.9, ec="k")
p.text(0.07,0.67,'n=3/2', fontsize=14, transform=ax.transAxes,bbox=bbox_props)
p.text(4,150,'weak rocks', fontsize=12)
p.tight_layout()

#n=2/3 case
res_diff = pickle.load(open('diff_thickness_high_uplift_0.66.pkl', 'rb'))
diff_frame = 160
res_equal = pickle.load(open('high_uplift_0.66.pkl', 'rb'))
equal_frame = 163
p.subplot(1,2,2)
p.plot(res_diff['chi'], res_diff['elev'][diff_frame], 'k-')
p.plot(res_equal['chi'], res_equal['elev'][equal_frame], 'k--')
p.ylabel('Elevation [m]', fontsize=12)
p.xlabel('$\chi$ [m]', fontsize=16)
p.legend(['Different thickness', 'Equal thickness'], loc='upper left', fontsize=12)
ax = p.gca()
thickness = 90.
for i, lly in enumerate(res_diff['end_soft'][diff_frame]):
    if  (i>0) and (i==len(res_diff['end_soft'][diff_frame])-1): 
        #original code, but we need this for first rectangle
        r = Rectangle((0,lly),200,res_diff['start_soft'][diff_frame][i]-lly,color='grey',alpha=.5)
    else:
        #went to set thickness to avoid jumpiness in movies
        r = Rectangle((0,lly),200,thickness,color='grey',alpha=.5)
    ax.add_patch(r)
p.text(0.07,0.67,'n=2/3', fontsize=14, transform=ax.transAxes,bbox=bbox_props)
p.text(4,150,'weak rocks', fontsize=12)
p.tight_layout()
p.savefig('fig7.pdf')



