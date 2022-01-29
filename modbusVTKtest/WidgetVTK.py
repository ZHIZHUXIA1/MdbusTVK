from vtk.qt.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor

from ValuesVTK import ValuesVTK


class WidgetVTK(QVTKRenderWindowInteractor):  # vtk的显示
    def __init__(self, parent=None):
        QVTKRenderWindowInteractor.__init__(self, parent)
        self.ren = ValuesVTK()
        self.GetRenderWindow().AddRenderer(self.ren)
        self.GetRenderWindow().GetInteractor().Initialize()



