import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import visvis as vv
from stl import mesh

from skimage import measure
# from skimage.draw import ellipsoid

# Generate a level set about zero of two idenntical ellipsoids in 3D
s = 50
n = 100
x = np.linspace(0,s,n)
y = np.linspace(0,s,n)
z = np.linspace(0,s,n)
a = 5

X,Y,Z = np.meshgrid(x,y,z)
gyroid = np.sin(X/a)*np.cos(Y/a) + np.sin(Y/a)*np.cos(Z/a) + np.sin(Z/a)*np.cos(X/a)

#Use marching cubes to obtain the surface mesh of the ellipsoids
verts, faces, normals, values = measure.marching_cubes_lewiner(gyroid, 0)
verts = verts*(s/n)
#Fancy indexing: 'verts[faces]' to generate a collection of triangles
vv.mesh(np.fliplr(verts), faces, normals, values)
vv.use().Run()


# Create the mesh
gyr_mesh = mesh.Mesh(np.zeros(faces.shape[0], dtype=mesh.Mesh.dtype))
for i, f in enumerate(faces):
    for j in range(3):
        gyr_mesh.vectors[i][j] = verts[f[j],:]

gyr_mesh.save('gyroid_stl.stl')