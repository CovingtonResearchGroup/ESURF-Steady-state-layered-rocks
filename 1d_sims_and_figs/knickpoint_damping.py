from stream_power import *
import subprocess

#Case n=1.2
#chi~2.45
case_name = 'damping_high_1.2.pkl' 
res = stream_erode(outputfile=case_name,n=1.2, m=0.6,
                 K1=1.5e-5,KR=1.5,uplift=0.0025,
                 thickness=50.,two_layers=100.,nx=2000.,nskip=80,
                 dx=250.,nt = 50000,A0 = 1., x0=5000.,
                 h = 1.67, #value from W+T 1999,Hack (1957)
                 k_a = 6.69,#value from W+T 1999, Hack (1957)
                 duration=10000./0.0025)
subprocess.check_call(['python', 'stream_power_movie.py', case_name, '50', '2.45'])

#Case n=0.8
# chi ~ 2.25
case_name = 'damping_med_0.8_long.pkl' 
res = stream_erode(outputfile=case_name,n=0.8, m=0.4,
                   K1=1.e-4,KR=1.5,uplift=0.0025,
                 thickness=50.,two_layers=100.,nx=2000.,nskip=80,
                 dx=250.,nt = 50000,A0 = 1., x0=5000.,
                 h = 1.67, #value from W+T 1999,Hack (1957)
                 k_a = 6.69,#value from W+T 1999, Hack (1957)
                 duration=100000./0.0025)                  
subprocess.check_call(['python', 'stream_power_movie.py', case_name, '50', '2.25'])





#Case n=0.9
# high damping
#case_name = 'damping_low_0.9_small_KR.pkl' 
#res = stream_erode(outputfile=case_name,n=0.95, m=0.45,
#                 K1=5.e-5,KR=1.05,uplift=0.0025,
#                 thickness=50.,two_layers=100.,nx=2000.,nskip=80,
#                 dx=25.,nt = 50000,A0 = 1., x0=2500.,
#                 h = 1.67, #value from W+T 1999,Hack (1957)
#                 k_a = 6.69,#value from W+T 1999, Hack (1957)
#                 duration=100000./0.0025)                  
#subprocess.check_call(['python', 'stream_power_movie.py', case_name])

