'''
Script to import *.dem files generated from FastScape and process channels
'''
from landlab.components.flow_routing.route_flow_dn import FlowRouter
from landlab.plot import channel_profile as prf
from landlab.plot.imshow import imshow_node_grid
from landlab import RasterModelGrid
import os, glob, pylab,numpy,pickle,time,copy,matplotlib,multiprocessing, sys
sys.setrecursionlimit(10000)

#Function to calculate chi
def get_chi(grid, len_node_arrays, profile_IDs, links_to_flow_receiver, unit_area = 1., m = 1./3., n = 2./3.):
    distances_upstream = []
    for i in xrange(len(profile_IDs)):
        data_store = []
        total_distance=0.
        data_store.append(total_distance)
        for j in xrange(len(profile_IDs[i])-1):
            total_distance += grid.link_length[links_to_flow_receiver[profile_IDs[i][j+1]]] * (unit_area / grid.at_node['drainage_area'][profile_IDs[i][j+1]]) ** (m / n)
            data_store.append(total_distance)
        distances_upstream.append(numpy.array(data_store))
    return distances_upstream

######################################################
# Function to process dem file (provide file name)  ##
# and output pickle files of channel properties     ##
######################################################
def mk_profile(dem_name, m=0.5, n=1, nx=3000, ny=3000, cellsize=100, cumulative_uplift=0):
    fle_name = dem_name[4:-4]
    t_stepnum = dem_name[4:-4]
    if t_stepnum[0:1] == '0':
        t_stepnum = t_stepnum[1:]
    dem_file = open(dem_name, 'rb')
    z = numpy.fromfile(dem_file, dtype='float32', count=nx*ny)
    dem_file.close()
    z = z.astype('float64')
    mg = RasterModelGrid(nx,ny,cellsize)
    _ = mg.add_field('node', 'topographic__elevation',z)
    _ = mg.diagonal_links_at_node()
    fr = FlowRouter(mg) 
    mg = fr.route_flow()
    pylab.figure("long_profiles_chi")
    profile_IDs = prf.channel_nodes(mg, mg.at_node['topographic__steepest_slope'],
                                    mg.at_node['drainage_area'],mg.at_node['flow_receiver'], number_of_channels=50)
    id_obj = open('chan-ids.p',"wrb")
    pickle.dump(profile_IDs,id_obj)
    id_obj.close()
    dists_upstr = get_chi(mg, len(mg.at_node['topographic__steepest_slope']),
                          profile_IDs, mg.at_node['links_to_flow_receiver'], m=m, n=n)
    dist_obj = open("dists-up.p",'wrb')
    pickle.dump(dists_upstr,dist_obj)
    dist_obj.close()
    
    elev = mg['node']['topographic__elevation']

    elev_obj = open("topo_elev.p",'wrb')
    pickle.dump(elev,elev_obj)
    dist_obj.close()

