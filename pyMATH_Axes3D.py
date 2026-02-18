#--------------
import numpy as np
import matplotlib.pyplot as plt
import ipywidgets
#--------------
x = np.linspace(-5,5,101)
y = np.linspace(-5,5,101)
X,Y = np.meshgrid(x,y)

def fxy2(x,y,a0=1,a1=0,a2=0,a3=0.2,a4=0,a5=0):
    """
    calculate 2D curved plane and plot it
    """
    # plane a0 + a1*x + a2*y + a3*x**2 + a4*y**2 + a5*x*y
    z = a0 + a1*x + a2*y + a3*x**2 + a4*y**2 + a5*x*y
    # plot
    scale=2
    ax = plt.figure(figsize=(6,6)).add_subplot(projection='3d')
    ax.set(xlim=(scale*x.min(),scale*x.max()), 
           ylim=(scale*y.min(),scale*y.max()), 
           zlim=(-10,10),
           xlabel='X', ylabel='Y', zlabel='Z')
    # 3D plot
    ax.plot_surface(x,y,z,lw=0.0,alpha=0.8,cmap='coolwarm', antialiased=False)
    ax.contour(x,y,z,linewidths=1,alpha=1.0,colors='black')
    # 3 2D plots alng side walls
    ax.contour(x,y,z, zdir='z', offset=-10, cmap='coolwarm')
    ax.contour(x,y,z, zdir='x', offset=scale*x.min(), cmap='coolwarm')
    ax.contour(x,y,z, zdir='y', offset=scale*y.max(), cmap='coolwarm')
    plt.show()
    return

ipywidgets.interact(fxy2,
                    x=ipywidgets.fixed(X),
                    y=ipywidgets.fixed(Y),
                    a0=ipywidgets.FloatSlider(min=-4,max=4,step=0.1,value=1),
                    a1=ipywidgets.FloatSlider(min=-2,max=2,step=0.1,value=0),
                    a2=ipywidgets.FloatSlider(min=-2,max=2,step=0.1,value=0),
                    a3=ipywidgets.FloatSlider(min=-0.5,max=0.5,step=0.1,value=0.1),
                    a4=ipywidgets.FloatSlider(min=-0.5,max=0.5,step=0.1,value=0),
                    a5=ipywidgets.FloatSlider(min=-0.5,max=0.5,step=0.1,value=0)
                   )
