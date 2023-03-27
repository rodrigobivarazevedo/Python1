import math
import numpy as np
import matplotlib.pyplot as plt


from IPython.display import IFrame
IFrame('./HI-1_WS22-23_FoS_triangle_HW3.pdf', width=900, height=800)

c = np.array([65., 67., 70., 64., 65., 66., 64.])
alpha = np.array([37., 36., 37., 35., 36., 37., 35.])
alpha_grad = alpha/180 * np.pi
a = 2*c*np.sin(alpha_grad/2)

a_mean = a.mean()
a_std = a.std()
print ("a = {0:.3f} +- {1:.3f} mm".format(a_mean , a_std))

c_mean = c.mean()
c_std = c.std()
print ("c = {0:.3f} +- {1:.3f} mm".format(c_mean , c_std))

alpha_mean = alpha.mean()
alpha_std = alpha.std()
print ("alpha = {0:.3f} +- {1:.3f} °".format(alpha_mean , alpha_std))

height = math.sqrt(c_mean**2 + (a_mean/2)**2 )
area = (a_mean * height)/2

print("area =",area,"mm")

uncertainty_of_area = math.sqrt((a_mean**2)*(a_std**2) + (c_mean**2)*(c_std**2))
print("uncertainty of area =",uncertainty_of_area, "mm")
print("Area of triangule =",area, "+-", uncertainty_of_area, "mm")