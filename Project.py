
import streamlit as st
import numpy as np
from PyAstronomy import pyasl
import matplotlib.pylab as plt
from PyAstronomy.pyasl import planck
from PIL import Image
st.title("MSc PHYSICS PROJECT")
tab1, tab2, = st.tabs(["Keplerian orbit ", "Planks Radiation Law",])
with tab1:
        
    st.title("CALCUALTE THE KEPLERIAN ORBIT")
    st.header("ORIBITAL ELEMENTS")
    st.write("Let us characterize all planetary orbits using a common Cartesian coordinate system   ,   ,   , centered on the Sun.  The   -  plane defines a reference plane, which is chosen to be the ecliptic plane (i.e., the plane of the Earth's orbit), with the   -axis pointing towards the ecliptic north pole (i.e., the direction normal to the ecliptic plane in a northward sense). Likewise, the   -axis defines a reference direction, which is chosen to point in the direction of the vernal equinox (i.e., the point in the Earth's sky at which the apparent orbit of the Sun passes through the extension of the Earth's equatorial plane from south to north). Suppose that the plane of a given planetary orbit is inclined at an angle   to the reference plane. The point at which this orbit crosses the reference plane in the direction of increasing   is termed its ascending node. The angle   subtended between the reference direction and the direction of the ascending node is termed the longitude of the ascending node. Finally, the angle,   , subtended between the direction of the ascending node and the direction of the orbit's perihelion is termed the argument of the perihelion")

    image = Image.open('Orbit1.jpg')
    st.image(image)

    # Instantiate a Keplerian elliptical orbit with
    # semi-major axis of 1.3 length units,
    # a period of 2 time units, eccentricity of 0.5,
    # longitude of ascending node of 70 degrees, an inclination
    # of 10 deg, and a periapsis argument of 110 deg.
    print("")
    st.header('What is a Semi-Major Axis of an Ellipse?')
    st.write("The semi-major axis of an ellipse is defined as the longest radius of the ellipse. The length of the semi-major axis is the distance from the center of the ellipse to the furthest edge. Ellipses look like circles that have been stretched or elongated along one axis. This elongated axis is the major axis. The major axis is the longest axis across the ellipse. The semi-major axis is half of this distance and is part of the same axis of the ellipse. The semi-major axis starts at the center point and follows the major axis to the furthest edge-point.")
    image = Image.open('img1.jpg')
    st.image(image)

    a = st.number_input('Semi-major axis',value=1.3)
    st.write('Semi-major axis= ', a)
    tau= st.number_input('period in time units',value=2)
    st.write('Period in time units= ', tau)
    st.write("Eccentricity: (e < 1). The ratio of the distance of the focus from the center of the ellipse, and the distance of one end of the ellipse from the center of the ellipse. If the distance of the focus from the center of the ellipse is 'c' and the distance of the end of the ellipse from the center is 'a', then eccentricity e = c/a.")
    e=st.slider('Eccentricity',min_value=0.1,max_value=1.0,value=0.5 )
    st.write('value of eccentricity =', e)
    st.write("The angle omega subtended between the reference direction and the direction of the ascending node is termed the longitude of the ascending node")
    st.write('omega=longitude of ascending nodes in degrees')
    omega=st.slider('Omega',min_value=0.0,max_value=90.0,value=70.0)
    st.write('Omega=', omega)
    st.write('I=Inclination in degrees')
    st.write("the plane of a given planetary orbit is inclined at an angle $ I$ to the reference plane.")
    I=st.slider('Inclination',min_value=0.0,max_value=90.0,value=10.0)
    st.write('Inclination=', I)
    st.write(" the angle, $ \omega$ , subtended between the direction of the ascending node and the direction of the orbit's perihelion is termed the argument of the perihelion.")
    st.write('w= periapsis argument')
    W=st.slider(' periapsis argument',min_value=0,max_value=180,value=110)
    st.write('w=', W)

    ke = pyasl.KeplerEllipse(a, tau, e, Omega=omega, i=I, w=W)
    # Get a time axis
    T=st.slider('time',min_value=0.0,max_value=1.9,value=1.9)
    t = np.linspace(0, T, 200)
    # Calculate the orbit position at the given points
    # in a Cartesian coordinate system.
    pos = ke.xyzPos(t)
    st.write("Shape of output array: ", pos.shape)
    # x, y, and z coordinates for 50th time point
    ("x, y, z for 50th point: ", pos[50, ::])
    # Calculate orbit radius as a function of the
    radius = ke.radius(t)
    # Calculate velocity on orbit
    vel = ke.xyzVel(t)
    # Find the nodes of the orbit (Observer at -z)
    ascn, descn = ke.xyzNodes_LOSZ()
    # Plot x and y coordinates of the orbit
    #plt.subplot(2, 1, 1)
    plt.subplots()
    plt.title("Periapsis (red diamond), Asc. node (green circle), desc. node (red circle)")
    plt.xlabel("East ->")
    plt.ylabel("North ->")
    plt.plot([0], [0], 'k+', markersize=15)
    plt.plot(pos[::, 1], pos[::, 0], 'bp')


    # Point of periapsis
    plt.plot([pos[0, 1]], [pos[0, 0]], 'rd')

    # Nodes of the orbit
    plt.plot([ascn[1]], [ascn[0]], 'go', markersize=10)
    plt.plot([descn[1]], [descn[0]], 'ro', markersize=10)
    st.pyplot(plt)
    # Plot RV
    plt.subplot(2, 1, 2)
    plt.xlabel("Time")
    plt.ylabel("Radial velocity [length/time]")
    plt.plot(t, vel[::, 2], 'r.-')
    st.pyplot(plt)
    image = Image.open('orb.jpg')
    st.image(image)

with tab2:
    st.title("Evaluate Planck’s radiation law.")
    image = Image.open('rad.jpg')
    st.image(image)

    # Define wavelength in meters
    lam = np.arange(1000.0*1e-10, 20000.*1e-10, 20e-10)
    T1=st.slider('Temperature1',min_value=0,max_value=10000,value=7000 )
    st.write('Temperature1 =', T1)
    T2=st.slider('Temperature2',min_value=0,max_value=10000,value=5000)
    st.write('Temperature2 =', T2)
    T3=st.slider('Temperature3',min_value=0,max_value=10000,value=9000)
    st.write('Temperature3 =', T3)
    # Get the Planck spectrum in [W/(m**2 m)] for a temperature of 7000 K
    s7 = planck(T1, lam=lam)
    # Get the Planck spectrum in [W/(m**2 m)] for a temperature of 5000 K
    s5 = planck(T2, lam=lam)
    # Get the Planck spectrum in [W/(m**2 m)] for a temperature of 9000 K
    s9 = planck(T3, lam=lam)

    # Convert into erg/(cm**2 * A * s)
    s5erg = s5 * 1e-7
    s7erg = s7 * 1e-7
    s9erg = s9 * 1e-7
    # Integrate the spectrum and compare with Stefan-Boltzmann law
    i5 = np.sum(s5) * (lam[1] - lam[0])
    i7 = np.sum(s7) * (lam[1] - lam[0])
    i9 = np.sum(s9) * (lam[1] - lam[0])
    print("5000 K integral: %.3e W/m**2 (Stefan-Boltzmann predicts %.3e W/m**2)" % (i5, (5.67e-8*5000.**4)))
    print("7000 K integral: %.3e W/m**2 (Stefan-Boltzmann predicts %.3e W/m**2)" % (i7, (5.67e-8*7000.**4)))
    print("7000 K integral: %.3e W/m**2 (Stefan-Boltzmann predicts %.3e W/m**2)" % (i9, (5.67e-8*9000.**4)))
    fig1, ax = plt.subplots()
    ax.set_xlabel("Wavelength [$\AA$]")
    ax.set_ylabel("Flux [erg/cm$^2$/A/s]")
    ax.plot(lam*1e10, s5erg, 'r-')
    ax.plot(lam*1e10, s7erg, 'b-')
    ax.plot(lam*1e10, s9erg, 'c-')
    #plt.show()
    st.pyplot(fig1)

    st.header("Wien's Displacement Law")
    st.subheader("This Law is usefull to find the temperature of the distance planet")
    st.write("b=Wein's Displacement constant in 28.97 mK")
    st.write("K=temperature in kelvin")
    b=2.8971*10**-3
    st.write(" max wavelent coming from the star in Angstron  ")
    lam1=st.slider('max wavelenght', min_value=1000,max_value=10000,value=5000)
    W=lam1*10**-10
    Temp=b/W
    st.write("temperacture of the star is=" , Temp, ("kelvin"))
        

