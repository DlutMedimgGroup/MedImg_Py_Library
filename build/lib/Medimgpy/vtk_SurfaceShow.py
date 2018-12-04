#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
Script Name	  : itkVectorFuzzyConnectednessImageFilter
Author		  : zengxiao
Created		  : 2018/7/11
Version		  : 2.0
Description	  : Sorry, I didn't understand how does the code work, so I just copied genispan's code from CSDN.
                The courses arrangement of this week is too full, and I have not been able to explore it very well.
  PURPOSE     : Vtk display surface
  Modified    : Change to a simple display method.
"""

import vtk

filename = "Liver.stl"

reader = vtk.vtkSTLReader()
reader.SetFileName(filename)

mapper = vtk.vtkPolyDataMapper()

mapper.SetInputConnection(reader.GetOutputPort())

actor = vtk.vtkActor()
actor.SetMapper(mapper)

# Create a rendering window and renderer
ren = vtk.vtkRenderer()
renWin = vtk.vtkRenderWindow()
renWin.AddRenderer(ren)

# Create a renderwindowinteractor
iren = vtk.vtkRenderWindowInteractor()
iren.SetRenderWindow(renWin)

# Assign actor to the renderer
ren.AddActor(actor)

# Enable user interface interactor
iren.Initialize()
renWin.Render()
iren.Start()