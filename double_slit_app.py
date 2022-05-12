import streamlit as st
import numpy as np
from numpy import cos, sin, pi
import matplotlib.pyplot as plt
import altair as alt

from pathlib import Path
# markdown file
md=Path("double_slit.md").read_text()
st.markdown(md, unsafe_allow_html=True)

# max and min lambda
lam_min=380
lam_max=700

# number of grid points
n=2000
theta=np.linspace(-np.pi/64,np.pi/64,n)
angles=theta*180/pi

# make matplotlib background dark 
plt.style.use('dark_background')

def intensity(D,d,lam,theta):
    
    # I_0 is taken to be 1
    
    k=2*pi/lam
    
    beta=k*D*sin(theta)/2
    alpha=k*d*sin(theta)/2
    
    # single slit shape
    f1 = sin(beta)**2/beta**2
    
    # 2-slit shape
    f2 = sin(2*alpha)**2/sin(alpha)**2
        
    return f1, f2

st.sidebar.write("Adjust the plotting parameters here.")

st.sidebar.write(r"Select slit width D in $10^{-6}~m$ (micrometers).")
D=st.sidebar.slider("",min_value=10, max_value=400, step=10,value=40)
D=D*1e-6

st.sidebar.write(r"Select slit spaceing d in $10^{-6}~m$ (micrometers).")
d=st.sidebar.slider(" ",min_value=10, max_value=400, step=10,value=70)
d=d*1e-6

st.sidebar.write(r"Select wavelength $\lambda$ in $10^{-9}~m$ (nanometers).")
lam=st.sidebar.slider(" ",min_value=lam_min, max_value=lam_max, step=10,value=515)
lam=lam*1e-9


f1, f2=intensity(D,d,lam,theta)

# calculate and scale intensity 
I=f1*f2
I=I/np.max(I)
        
f1=f1*np.max(f2)
f1=f1/np.max(f1)
f2=f2/np.max(f2)

# make plot
fig=plt.figure(figsize=(14,6))
ax=fig.add_subplot()
ax.set_xlim(angles[0],angles[-1])
ax.set_xlabel(r"$\theta$ [degrees]",size=20)
ax.set_ylabel(r"$I/I_0$",size=20)
ax.plot(angles,f1,"--",lw=3,color="yellow",alpha=.5)
ax.plot(angles,f2,lw=3,color="orange", alpha=.5)
ax.plot(angles,I,lw=3,color="red")
ax.grid()

st.pyplot(fig)


st.write("J. E. McEwen, (c) 2022")