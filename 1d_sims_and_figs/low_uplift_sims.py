from stream_power import stream_erode
import subprocess

#Case n=2/3
case_name = 'low_uplift_0.66.pkl' 
res = stream_erode(outputfile=case_name,n=2./3., m=1./3.,
                 K1=4e-5,KR=2.0,uplift=0.00025,
                 thickness=10.,two_layers=20.,nx=2000.,nskip=100,
                 dx=100.,nt = 50000,A0 = 1., x0=5000.,
                 h = 1.67, #value from W+T 1999,Hack (1957)
                 k_a = 6.69,#value from W+T 1999, Hack (1957)
                 duration=1000000./0.0025)
subprocess.check_call(['python', 'stream_power_movie.py', case_name, '10'])

#Case n=3/2
case_name = 'low_uplift_1.5.pkl' 
res = stream_erode(outputfile=case_name,n=3./2., m=3./4.,
                 K1=3.e-6,KR=2.0,uplift=0.00025,
                 thickness=10.,two_layers=20.,nx=2000.,nskip=100,
                 dx=100.,nt = 50000,A0 = 1., x0=5000.,
                 h = 1.67, #value from W+T 1999,Hack (1957)
                 k_a = 6.69,#value from W+T 1999, Hack (1957)
                 duration=1000000./0.0025)                  
subprocess.check_call(['python', 'stream_power_movie.py', case_name, '10'])

#Case n=1
case_name = 'low_uplift_1.pkl' 
res = stream_erode(outputfile=case_name,n=1., m=1./2.,
                 K1=2.e-5,KR=1.2,uplift=0.00025,
                 thickness=10.,two_layers=20.,nx=2000.,nskip=50,
                 dx=100.,nt = 50000,A0 = 1., x0=5000.,
                 h = 1.67, #value from W+T 1999,Hack (1957)
                 k_a = 6.69,#value from W+T 1999, Hack (1957)
                 duration=1000000./0.0025)                  
subprocess.check_call(['python', 'stream_power_movie.py', case_name, '10'])



