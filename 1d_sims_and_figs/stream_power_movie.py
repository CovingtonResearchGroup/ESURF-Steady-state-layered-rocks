import multiprocessing
from pandas import read_csv
from numpy import array,arange
import os
import matplotlib.pyplot as p
import gc, sys, subprocess
import cPickle as pickle
from matplotlib.patches import Rectangle
from pylab import *

#Make an individual frame in animation
def make_frame(frame_dict):
    fig=p.figure()
    p.plot(frame_dict['chi'],frame_dict['elev'], 'k-')
    if frame_dict['damping_length'] != 0:
        p.plot([frame_dict['damping_length'],frame_dict['damping_length']],
               [0,frame_dict['max_elev']], 'r-', lw=3)
    p.ylim(0,frame_dict['max_elev'])
    #Can be added and edited to create descriptive label
    #text(0.25,0.8,'n=1.5', transform= gca().transAxes)
    #text(0.25,0.75,'uplift=0.25 mm/yr', transform= gca().transAxes)
    p.ylabel('Elevation (m)')
    p.xlabel('Chi (m)')
    ax = p.gca()
    thickness= frame_dict['thickness']
    for i, lly in enumerate(frame_dict['end_soft']):
        if  (i>0) and (i==len(frame_dict['end_soft'])-1): 
            #original code, but we need this for first rectangle
            r = Rectangle((0,lly),200,frame_dict['start_soft'][i]-lly,color='grey',alpha=.5)
        else:
            #went to set thickness to avoid jumpiness in movies
            r = Rectangle((0,lly),200,thickness,color='grey',alpha=.5)
        ax.add_patch(r)
    p.tight_layout()
    p.savefig(frame_dict['basename']+'/temp%09d.png'%frame_dict['i'])
    fig.clf()
    p.close()
    gc.collect()
    
if __name__ == '__main__':
    picklefile = sys.argv[1]
    if len(sys.argv)>2:
        thickness=float(sys.argv[2])
    else:
        thickness=50.
    if len(sys.argv)>3:
        damping_length = float(sys.argv[3])
    else:
        damping_length=0
    if len(sys.argv)>4:
        n = sys.argv[4]
    else:
        n=''
    if len(sys.argv)>5:
        uplift = sys.argv[5]
    else:
        uplift=''
    res = pickle.load(open(picklefile,'rb'))
    basename = picklefile[:-4]
    if not os.path.exists('./'+basename):
        os.makedirs('./'+basename)
    chi = res['chi']
    elev = res['elev']
    start_soft = res['start_soft']
    end_soft = res['end_soft']
    uplift = res['uplift']
    frame_dict_list = []
    max_elev = elev.max()
    for i,frame_elev in enumerate(elev):
        frame_dict = {}
        frame_dict['elev'] = frame_elev
        frame_dict['chi'] = chi
        frame_dict['start_soft'] = start_soft[i]
        frame_dict['end_soft'] = end_soft[i]
        frame_dict['uplift'] = uplift[i]
        frame_dict['max_elev'] = max_elev
        frame_dict['basename'] = basename
        frame_dict['i'] = i
        frame_dict['thickness']=thickness
        frame_dict['damping_length']=damping_length
        frame_dict['n'] = n
        frame_dict['uplift'] = uplift
        frame_dict_list.append(frame_dict)
    pool_size = 4
    pool = multiprocessing.Pool(processes=pool_size)
    outputs = pool.map_async(make_frame,frame_dict_list,4)
    pool.close()
    pool.join()
    print "Creating avi file..."
    command = ('mencoder',
               'mf://'+basename+'/*.png',
               '-mf',
               'type=png:w=800:h=600:fps=10',
               '-ovc',
               'lavc',
               '-lavcopts',
               'vcodec=mpeg4',
               '-oac',
               'copy',
               '-o',
               basename+'/'+basename+'.avi')
    subprocess.check_call(command)
