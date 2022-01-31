"""
   作者：zhan
   日期：2022年01月31日
"""
import vtkmodules.all as vtk
from vtkmodules.vtkRenderingCore import vtkRenderWindow
from vtkmodules_vtkFiltersSources import vtkConeSource

from mvc.MyCtrl import MyView


class ValuesVTKCone(vtk.vtkActor, MyView):  # vtk显示的具体内容
    def __init__(self):
        super(ValuesVTKCone, self).__init__()
        self.source = vtkConeSource()
        self.source.SetResolution(5)
        self.source.SetHeight(5)
        self.source.SetRadius(3)
        self.mapper = vtk.vtkPolyDataMapper()
        self.mapper.SetInputConnection(self.source.GetOutputPort())
        self.SetMapper(self.mapper)
        self.GetProperty().SetColor(0, 1, 1)

    def slot_a(self, **kwargs):  # 改变
        interActor = kwargs["interActor"]
        p = kwargs["pos"]
        self.source.SetCenter(p[0], p[1], p[2])
        interActor.update()
