import batman
import numpy as np
import matplotlib.pyplot as plt

params = batman.TransitParams()
params.t0 = 0.
params.per = 4.04961
params.rp = 0.0689
params.a = 0.02144
params.inc = 89.75
params.ecc = 0.0
params.w = -8.73
params.u = [0.4238, 0.215]
params.limb_dark = "quadratic"

t = np.linspace(-0.025, 0.025, 1000)  
m = batman.TransitModel(params, t)

flux = m.light_curve(params)
plt.plot(t,flux)
radii = np.linspace(0.09, 0.11, 20)

for r in radii:
        params.rp = r                           
        new_flux = m.light_curve(params) 
        
plt.plot(t,_new_flux)

