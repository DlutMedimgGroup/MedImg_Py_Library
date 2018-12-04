
"""
 Script Name	  : meshSubdivision
 Author		  : BoyceTian
 Created		  : 2018/7/20
 Version		  : 1.0
 Description	  :
   PURPOSE     : An example for subdividing meshes by using pymesh
   INPUTS      :
   - filepath  : Path of original mesh
                 Type of data: .stl
   - filenew   : Path of subdivided mesh
                 Type of data: stl
   - mesh      : original mesh
                 Type of data: str
   - mesh_new  : subdivided mesh

    OUTPUTS    :
"""

import pymesh

# get the path of the original mesh and set the path of the Subdivided mesh
filepath="./Spleen_3D-interpolation.stl"
filenew="./Spleen_3D-interpolation_new.stl"
#get the original mesh
mesh=pymesh.load_mesh(filepath)
#subdivide the mesh
mesh_new=pymesh.subdivide(mesh,order=3,method='simple')
#write the subdivided mesh as a new file
pymesh.save_mesh(filenew,mesh_new)
