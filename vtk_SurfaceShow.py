#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
Script Name	  : itkVectorFuzzyConnectednessImageFilter
Author		  : genispan(CSDN)
Created		  : 2018/7/11
Version		  : 1.0
Description	  : Sorry, I didn't understand how does the code work, so I just copied genispan's code from CSDN.
                The courses arrangement of this week is too full, and I have not been able to explore it very well.
  PURPOSE     : Vtk display surface
"""

import vtk

aRenderer = vtk.vtkRenderer();
renWin = vtk.vtkRenderWindow();
renWin.AddRenderer(aRenderer);
iren = vtk.vtkRenderWindowInteractor();
iren.SetRenderWindow(renWin);

v16 = vtk.vtkDICOMImageReader();
v16.SetDataByteOrderToLittleEndian();
v16.SetDirectoryName("D:\PythonCode\zx\Liver.stl");
v16.SetDataSpacing(3.2, 3.2, 1.5);

skinExtractor = vtk.vtkContourFilter();
skinExtractor.SetInputConnection(v16.GetOutputPort());
skinExtractor.SetValue(0, 500);
skinNormals = vtk.vtkPolyDataNormals();
skinNormals.SetInputConnection(skinExtractor.GetOutputPort());
skinNormals.SetFeatureAngle(60.0);
skinMapper = vtk.vtkPolyDataMapper();
skinMapper.SetInputConnection(skinNormals.GetOutputPort());
skinMapper.ScalarVisibilityOff();

skin = vtk.vtkActor();
skin.SetMapper(skinMapper);

outlineData = vtk.vtkOutlineFilter();
outlineData.SetInputConnection(v16.GetOutputPort());
mapOutline = vtk.vtkPolyDataMapper();
mapOutline.SetInputConnection(outlineData.GetOutputPort());
outline = vtk.vtkActor();
outline.SetMapper(mapOutline);
outline.GetProperty().SetColor(0, 0, 0);

aCamera = vtk.vtkCamera();
aCamera.SetViewUp(0, 0, -1);
aCamera.SetPosition(0, 1, 0);
aCamera.SetFocalPoint(0, 0, 0);
aCamera.ComputeViewPlaneNormal();

aRenderer.AddActor(outline);
aRenderer.AddActor(skin);
aRenderer.SetActiveCamera(aCamera);
aRenderer.ResetCamera();
aCamera.Dolly(1.5);

aRenderer.SetBackground(1, 1, 1);
renWin.SetSize(640, 480);
aRenderer.ResetCameraClippingRange();

iren.Initialize();
iren.Start();

v16.Delete();
skinExtractor.Delete();
skinNormals.Delete();
skinMapper.Delete();
skin.Delete();
outlineData.Delete();
mapOutline.Delete();
outline.Delete();
aCamera.Delete();
iren.Delete();
renWin.Delete();
aRenderer.Delete();