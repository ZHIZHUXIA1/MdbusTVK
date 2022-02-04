from vtk.qt.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor
from vtkmodules.vtkRenderingCore import vtkRenderWindow
from ValuesVTKSphere import ValuesVTKSphere
from ValuesVTKCone import ValuesVTKCone
from vtkmodules.vtkRenderingCore import vtkRenderWindow, vtkRenderer
from readxml import readxml
from readjson import readjson


class WidgetVTK(QVTKRenderWindowInteractor):  # vtk的显示
    def __init__(self, parent=None):
        QVTKRenderWindowInteractor.__init__(self, parent)
        self.srnum = readjson.runnum()
        self.ren = vtkRenderer()
        self.ren.SetBackground(1, 0, 1)
        self.action = []
        for i in range(self.srnum):
            self.action.append(ValuesVTKSphere())
            self.ren.AddActor(self.action[i])
        self.window = vtkRenderWindow()
        self.window.SetSize(600, 600)
        self.window.AddRenderer(self.ren)
        self.GetRenderWindow().AddRenderer(self.ren)
        self.GetRenderWindow().GetInteractor().Initialize()
