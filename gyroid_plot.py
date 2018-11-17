import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import visvis as vv
from stl import mesh

from skimage import measure
# from skimage.draw import ellipsoid

def gyroid(X,Y,Z):
        gyr = np.sin(X)*np.cos(Y) + np.sin(Y)*np.cos(Z) + np.sin(Z)*np.cos(X)
        return gyr

def schwarz_p(X,Y,Z):
        schwarz = np.cos(X) + np.cos(Y) + np.cos(Z)
        return schwarz

def schwarz_d(X,Y,Z):
        schwarz = np.sin(X)*np.sin(Y)*np.sin(Z) + np.sin(X)*np.cos(Y)*np.cos(Z) + np.cos(X)*np.sin(y)*np.cos(Z) + np.cos(X)*np.cos(Y)*np.sin(Z)
        return schwarz

selections = {'gyroid': gyroid, 'schwarz_p':schwarz_p, 'schwarz_d':schwarz_d}

mm = [50, 50, 50]
n = 100
a = 10

x = np.linspace(0, mm[0], n)
y = np.linspace(0, mm[1], n)
z = np.linspace(0, mm[2], n)

X,Y,Z = np.meshgrid(x,y,z)

function_values = selections['schwarz_p'](X/a,Y/a,Z/a)

#Use marching cubes to obtain the surface mesh of the ellipsoids
verts, faces, normals, values = measure.marching_cubes_lewiner(function_values, 0)
for i, v in enumerate(mm):
        verts[:,i]*=(v/n)
#Fancy indexing: 'verts[faces]' to generate a collection of triangles
vv.mesh(np.fliplr(verts), faces, normals, values)
vv.use().Run()


# # Create the mesh
# gyr_mesh = mesh.Mesh(np.zeros(faces.shape[0], dtype=mesh.Mesh.dtype))
# for i, f in enumerate(faces):
#     for j in range(3):
#         gyr_mesh.vectors[i][j] = verts[f[j],:]

# gyr_mesh.save('gyroid_stl.stl')