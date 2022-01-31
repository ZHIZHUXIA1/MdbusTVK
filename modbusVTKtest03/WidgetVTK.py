from vtk.qt.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor
from vtkmodules.vtkRenderingCore import vtkRenderWindow
from ValuesVTKSphere import ValuesVTKSphere
from ValuesVTKCone import ValuesVTKCone
from vtkmodules.vtkRenderingCore import vtkRenderWindow,  vtkRenderer


class WidgetVTK(QVTKRenderWindowInteractor):  # vtk的显示
    def __init__(self, parent=None):
        QVTKRenderWindowInteractor.__init__(self, parent)
        self.actor = ValuesVTKSphere()
        self.actor1 = ValuesVTKCone()
        self.ren = vtkRenderer()
        self.ren.AddActor(self.actor)
        self.ren.AddActor(self.actor1)
        self.window = vtkRenderWindow()
        self.window.SetSize(600, 600)
        self.window.AddRenderer(self.ren)
        self.GetRenderWindow().AddRenderer(self.ren)
        self.GetRenderWindow().GetInteractor().Initialize()



