import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm

data = pd.read_csv('serie_9.csv') # <=====
df = data.dropna()

time = df['Tiempo (s)'].tolist()
position = df['Posición (m)'].tolist()
velocity = df['Vector velocidad (m/s)'].tolist()
aceleration = df['Aceleración (m/s²)'].tolist()
fuerza = df['Fuerza (N)']

t = np.array(time, dtype=np.float64)
p = np.array(position, dtype=np.float64)
v = np.array(velocity, dtype=np.float64)
a = np.array(aceleration, dtype=np.float64)
f = np.array(fuerza, dtype=np.float64)

###### Plots #####
plt.style.use(['science', 'notebook', 'grid']) # 'dark_background'
# Position
plt.figure(figsize=(8,5))
plt.plot(t, p, color='b', label='Posición')
plt.title('Posición')
plt.xlabel('Tiempo [s]')
plt.ylabel('Posicion [m]')
#plt.savefig('serie_9_position_plot.png', dpi=200)
plt.show()
# Velocity
plt.figure(figsize=(8,5))
plt.plot(t, v, color='g', label='Velocidad')
plt.title('Velocidad')
plt.xlabel('Tiempo [s]')
plt.ylabel('Velocidad [m/s]')
#plt.savefig('serie_9_velocity_plot.png', dpi=200)
plt.show()
# Aceleration
plt.figure(figsize=(8,5))
plt.plot(t, a, color='c', label='Aceleración')
plt.title('Aceleración')
plt.xlabel('Tiempo [s]')
plt.ylabel('Aceleración [m/s$^2$]')
#plt.savefig('serie_9_aceleration_plot.png', dpi=200)
plt.show()
# Force
plt.figure(figsize=(8,5))
plt.plot(t, f, color='purple', label='Fuerza')
plt.title('Fuerza')
plt.xlabel('Tiempo [s]')
plt.ylabel('Fuerza [N]')
#plt.savefig('serie_9_force_plot.png', dpi=200)
plt.show()
# Force over displacment
plt.figure(figsize=(8,5))
plt.plot(p, f, 'o', color='purple', label='Fuerza')
plt.title('Fuerza')
plt.xlabel('Posición [m]')
plt.ylabel('Fuerza [N]')
#plt.savefig('serie_9_force_displacment_plot.png', dpi=200)
plt.show()
# Fitting
pb = p[400:900]
fb = f[400:900]
x_new = sm.add_constant(pb)
model = sm.OLS(fb, x_new)
results = model.fit()

print("===Fit===")
print('summary:', results.summary())

r = f"Coefficient of determination rsquared = {results.rsquared}"
rs = results.rsquared
r_s = f"Adjusted coefficient of determination rsquared_adj = {results.rsquared_adj}"
rs_a = results.rsquared_adj
parm = f"Regression coefficients (b, m) = {results.params}"

new_parm = results.params
m = new_parm[0]
b = new_parm[1]

textstr_1 = '\n'.join((
    r'$y = mx + b$',
    r'$m=%.4f$' % (m),
    r'$b=%.4f$' % (b),
    r'$r^2=%.4f$' % (rs),
    r'$r^2 adj=%.4f$' % (rs_a)))


# Force over displacment and fitting
plt.figure(figsize=(8,5))
plt.plot(pb, fb, 'o', color='purple', label='Datos')
plt.plot(pb, results.fittedvalues, label='Ajuste', linewidth=4, color='lime', alpha=1)
plt.text(0.413, -2.5, textstr_1, ha='center', va='center', bbox=dict(facecolor='white', edgecolor='black'))
plt.title('Fuerza')
plt.xlabel('Posición [m]')
plt.ylabel('Fuerza [N]')
plt.legend(loc=0, fancybox=False, edgecolor='black')
#plt.savefig('serie_9_force_displacment_fit_plot.png', dpi=200)
plt.show()
