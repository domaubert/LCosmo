import numpy as np
import pylab as pl

def dadt(a,om,ov,H0):
    ok=1.-om-ov
    res=H0*np.sqrt(om/a+ov*a*a+ok)
    return res

def compa2t(om,ov,H0):
	dt=-1.
	acur=1.
	tcur=0.

	# backwards
	vt=np.zeros(50000)
	va=np.zeros(50000)
	i=0
	while acur>1e-3:
		da=dt*dadt(acur,om,ov,H0)
		acur=acur+da
		tcur=tcur+dt
		va[i]=acur
		vt[i]=tcur
		i=i+1


	# Forwards
	dt=1
	acur=1
	tcur=1
	signe=1
	while acur<2.0:
		da=dt*signe*dadt(acur,om,ov,H0)
		acur=acur+da
		tcur=tcur+dt
		if(om/acur+ov*acur*acur+(1.-om-ov))<0:
			acur=acur-2*da
			signe=-1
		va[i]=acur
		vt[i]=tcur
		if acur<1e-2:
			break
		i=i+1


	# remove zero
	va=va[0:i]
	vt=vt[0:i]

	# sort
	ss=np.argsort(vt)
	vt=vt[ss]
	va=va[ss]



	return va,vt


om=0.3
ov=0.7
H0=68e3/3.08e22*(1e6*365*24*3600.)


va,vt=compa2t(om,ov,H0)
pl.plot(vt,va)

om=1.0
ov=0.
va,vt=compa2t(om,ov,H0)
pl.plot(vt,va)

om=0.001
ov=0.999
va,vt=compa2t(om,ov,H0)
pl.plot(vt,va)

om=0.3
ov=0.
va,vt=compa2t(om,ov,H0)
pl.plot(vt,va)


om=5
ov=0.
va,vt=compa2t(om,ov,H0)
pl.plot(vt,va)

pl.legend(['om=0.3 ov=0.7','om=1.0 ov=0.','om=0.001 ov=0.999','om=0.3 ov=0.','om=5.0 ov=0.'],loc=2)
pl.xlabel('t[Myrs]')
pl.ylabel('aexp(t)')
pl.show()
