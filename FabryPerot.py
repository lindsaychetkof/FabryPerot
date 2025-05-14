import numpy as np
import matplotlib.pyplot as plt
import math 

# Cavity Mode

lam = 399e-9 #399 nm wavelength
L = 0.1 # Length of cavity = 0.10 m

# solve for w0
w0 = math.sqrt((lam*L)/(2*np.pi))
print("w0: ", w0, "m")

z_R = (np.pi*w0*w0)/lam
print("z_R: ", z_R)

R = 0.1 # R = 10 cm 
z = 0.05 # 5 cm away from focus

w_z = w0 * np.sqrt(1 + (z / z_R)**2)

#solve for q_in with w0, w(z)
q_in = 1 / (1/R - 1j * lam / (np.pi * w_z**2))

print("w_z: ", w_z)
print("q_in: ", q_in)

# Takes in initial equation and focal length of lens 
#w_in = 0.0006 # 0.6 mm for beam going into telescope
w_in = 0.000475 #0.475 mm for incoming
def propogate(q_in, f):
    print("\033[1mFocal Length: \033[0m", f, "m")
    M_free = np.array([[1, f], [0, 1]])
    #print("Free-Space Matrix: ")
    #print(M_free)

    M_lens = np.array([[1,0],[-1/f, 1]])
    #print("Lens Matrix: ")
    #print(M_lens)

    # Free space of distance f followed by lens with focal length f
    M_total = np.dot(M_lens, M_free)
    print("Total Matrix: ")
    print(M_total)

    A, B, C, D = M_total.ravel()
    q_out = (A * q_in + B) / (C * q_in + D)
    print("q_out: ", q_out)

    # Beam radius at output
    w_out = np.sqrt(-lam / (np.pi * np.imag(1 / q_out)))
    print("w_out: ", w_out, "m")

    # Radius of curvature 
    R_out = 1 / np.real(1 / q_out)
    print("R_out: ", R_out, "m")

    #Telescope ratio
    print ("Telescope Ratio (f1/f2): ", w_in/w_out)

# Test various focal lengths
print("q_in: ", q_in)
propogate(q_in, 0.1)
propogate(q_in, 0.075)
propogate(q_in, 0.05)
propogate(q_in, 0.250)
propogate(q_in, 0.35)
