from pylab import *
#######################################
## Damping length scale as a function #
## of erodibility ratio (Fig 8)       #
#######################################
figure(figsize=(6,5))
KR = 10.**linspace(0.01,2,150)
l1 = 1 + 1./(KR**(1./1.) - 1.)
l2 = 1 + 1./(KR**(1./0.5) - 1.)
l3 = 1 + 1./(KR**(1./1.5) - 1.)
semilogx(KR,l1, 'k-')
semilogx(KR,l2, 'k--')
semilogx(KR,l3, 'k-.')
xlabel('$K_w / K_s$', fontsize=18)
ylabel('$\lambda^*$',fontsize=20)
ylim([0,5])
legend(['n=1','n=0.5', 'n=1.5'],fontsize=15)
tight_layout()
savefig('fig8.pdf')

