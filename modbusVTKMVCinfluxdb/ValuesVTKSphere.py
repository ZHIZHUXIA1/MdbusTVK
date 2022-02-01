import vtkmodules.all as vtk
from vtkmodules.vtkFiltersSources import vtkSphereSource

from mvc.MyCtrl import MyView


class ValuesVTKSphere(vtk.vtkActor, MyView):  # vtk显示的具体内容
    def __init__(self):
        super(ValuesVTKSphere, self).__init__()
        self.source = vtkSphereSource()
        self.source.SetCenter(5, 0, 0)
        self.source.SetRadius(3)
        self.mapper = vtk.vtkPolyDataMapper()
        self.mapper.SetInputConnection(self.source.GetOutputPort())
        self.SetMapper(self.mapper)
        self.GetProperty().SetColor(0, 0, 1)
        self.GetProperty().SetColor(1, 1, 1)

    def slot_a(self, **kwargs):  # 改变
        interActor = kwargs["interActor"]
        p = kwargs["pos"]
        self.source.SetCenter(p[0], p[1], p[2])
        interActor.update()
