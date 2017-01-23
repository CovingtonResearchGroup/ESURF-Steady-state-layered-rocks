from pylab import *
n=linspace(0.5,2,100)
K_ratio_weak = 2.
S_ratio_weak = ( (1. + K_ratio_weak**(1./(1-n)))/2.)**(1./n)

K_ratio_strong = 0.5
S_ratio_strong = ( (1. + K_ratio_strong**(1./(1-n)))/2.)**(1./n)

semilogy(n,S_ratio_strong, 'k-')
semilogy(n,S_ratio_weak, 'k--')
ylim(0.1,100)
xlim(0.5,2)
xlabel('n',fontsize=14)
ylabel('$S_{1,cont}/S_{1,topo}$', fontsize=16)
legend(['Strong', 'Weak'])
tight_layout()
savefig('fig6.pdf')
