import vtkmodules.all as vtk
from vtkmodules.vtkRenderingCore import vtkRenderWindow
from vtkmodules_vtkFiltersSources import vtkConeSource

from mvc.MyCtrl import MyView


class ValuesVTK(vtk.vtkRenderer, MyView):  # vtk显示的具体内容
    def __init__(self):
        super(ValuesVTK, self).__init__()
        self.source = vtk.vtkSphereSource()
        self.source.SetCenter(0, 0, 0)
        self.source.SetRadius(10)
        self.source1 = vtkConeSource()
        self.source1.SetResolution(5)  # 圆锥的棱边数
        self.source1.SetHeight(30)  # 指定高度
        self.source1.SetRadius(5)  # 指定半径
        self.mapper = vtk.vtkPolyDataMapper()
        self.mapper.SetInputConnection(self.source.GetOutputPort())
        self.mapper1 = vtk.vtkPolyDataMapper()
        self.mapper1.SetInputConnection(self.source1.GetOutputPort())
        self.actor = vtk.vtkActor()
        self.actor.SetMapper(self.mapper)
        self.actor.GetProperty().SetColor(1, 0, 1)
        self.actor1 = vtk.vtkActor()
        self.actor1.SetMapper(self.mapper1)
        self.actor1.GetProperty().SetColor(1, 0, 1)
        self.AddActor(self.actor)
        self.AddActor(self.actor1)
        self.window = vtkRenderWindow()
        self.window.SetSize(400, 400)
        self.window.AddRenderer(self)
        self.SetBackground(1, 1, 1)

    def slot_a(self, **kwargs):  # 改变
        interActor = kwargs["interActor"]
        p = kwargs["pos"]
        p1 = kwargs["pos1"]
        self.source.SetCenter(p[0], p[1], p[2])
        self.source1.SetCenter(p1[0], p1[1], p1[2])
        interActor.update()
