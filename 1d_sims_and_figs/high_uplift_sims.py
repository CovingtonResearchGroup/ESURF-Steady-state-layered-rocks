from stream_power import stream_erode
import subprocess

#Case n=2/3
case_name = 'high_uplift_0.66.pkl' 
res = stream_erode(outputfile=case_name,n=2./3., m=1./3.,
                 K1=1e-4,KR=2.0,uplift=0.0025,
                 thickness=50.,two_layers=100.,nx=2000.,nskip=80,
                 dx=25.,nt = 50000,A0 = 1., x0=1500.,
                 h = 1.67, #value from W+T 1999,Hack (1957)
                 k_a = 6.69,#value from W+T 1999, Hack (1957)
                 duration=10000./0.0025)
subprocess.check_call(['python', 'stream_power_movie.py', case_name])

#Case n=3/2
case_name = 'high_uplift_1.5.pkl' 
res = stream_erode(outputfile=case_name,n=3./2., m=3./4.,
                 K1=1.5e-6,KR=2.0,uplift=0.0025,
                 thickness=50.,two_layers=100.,nx=2000.,nskip=80,
                 dx=25.,nt = 50000,A0 = 1., x0=2500.,
                 h = 1.67, #value from W+T 1999,Hack (1957)
                 k_a = 6.69,#value from W+T 1999, Hack (1957)
                 duration=10000./0.0025)                  
subprocess.check_call(['python', 'stream_power_movie.py', case_name])

#Case n=1
case_name = 'high_uplift_1.pkl' 
res = stream_erode(outputfile=case_name,n=1., m=1./2.,
                 K1=2.e-5,KR=1.2,uplift=0.0025,
                 thickness=50.,two_layers=100.,nx=2000.,nskip=50,
                 dx=25.,nt = 50000,A0 = 1., x0=2500.,
                 h = 1.67, #value from W+T 1999,Hack (1957)
                 k_a = 6.69,#value from W+T 1999, Hack (1957)
                 duration=10000./0.0025)                  
subprocess.check_call(['python', 'stream_power_movie.py', case_name])

#Case n=2/3 with different thicknesses
case_name = 'diff_thickness_high_uplift_0.66.pkl' 
res = stream_erode(outputfile=case_name,n=2./3., m=1./3.,
                 K1=1e-4,KR=2.0,uplift=0.0025,
                 thickness=90.,two_layers=100.,nx=2000.,nskip=80,
                 dx=25.,nt = 50000,A0 = 1., x0=1500.,
                 h = 1.67, #value from W+T 1999,Hack (1957)
                 k_a = 6.69,#value from W+T 1999, Hack (1957)
                 duration=10000./0.0025)
subprocess.check_call(['python', 'stream_power_movie.py', case_name, '90'])

#Case n=3/2 with different thicknesses
case_name = 'diff_thickness_high_uplift_1.5.pkl' 
res = stream_erode(outputfile=case_name,n=3./2., m=3./4.,
                 K1=1.5e-6,KR=2.0,uplift=0.0025,
                 thickness=90.,two_layers=100.,nx=2000.,nskip=80,
                 dx=25.,nt = 50000,A0 = 1., x0=2500.,
                 h = 1.67, #value from W+T 1999,Hack (1957)
                 k_a = 6.69,#value from W+T 1999, Hack (1957)
                 duration=10000./0.0025)                  
subprocess.check_call(['python', 'stream_power_movie.py', case_name, '90'])





