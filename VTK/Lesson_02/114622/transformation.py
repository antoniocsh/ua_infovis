###############################################################################
#       						Cone.py
###############################################################################

# This example creates a polygonal model of a Cone e visualize the results in a
# VTK render window.
# The program creates the cone, rotates it 360º and closes
# The pipeline  source -> mapper -> actor -> renderer  is typical 
# and can be found in most VTK programs

# Import all VTK modules
from vtkmodules.all import *

# Import only needed modules
# import vtkmodules.vtkInteractionStyle
# import vtkmodules.vtkRenderingOpenGL2
# from vtkmodules.vtkFiltersSources import vtkConeSource
# from vtkmodules.vtkRenderingCore import (
#     vtkActor,
#     vtkPolyDataMapper,
#     vtkRenderWindow,
#     vtkRenderWindowInteractor,
#     vtkRenderer
# )

def main():
    # Renderer and window
    ren = vtkRenderer()
    ren.SetBackground(0.1, 0.2, 0.4)

    renWin = vtkRenderWindow()
    renWin.AddRenderer(ren)
    renWin.SetSize(800, 600)
    renWin.SetWindowName("Textured Cube")

    iren = vtkRenderWindowInteractor()
    iren.SetRenderWindow(renWin)

    # Texture images and plane positions
    images = ["./images/Im1.jpg", "./images/Im6.jpg", "./images/Im3.jpg", "./images/Im4.jpg", "./images/Im2.jpg", "./images/Im5.jpg"]

    # Define translations
    transforms = [
        ((0, 0, 0.5), (0, 0, 0)),      # front
        ((0, 0, -0.5), (0, 180, 0)),   # back
        ((-0.5, 0, 0), (0, -90, 0)),   # left
        ((0.5, 0, 0), (0, 90, 0)),     # right
        ((0, 0.5, 0), (-90, 0, 0)),    # top
        ((0, -0.5, 0), (90, 0, 0)),    # bottom
    ]

    # Create and add actors
    for i in range(6):
        actor = createTexturedPlane(images[i], transforms[i][0], transforms[i][1])
        ren.AddActor(actor)

    # Start interaction
    renWin.Render()
    iren.Initialize()
    iren.Start()



def createTexturedPlane(texture_file, translation=(0,0,0), rotation=(0,0,0)):
    # Create plane
    plane = vtkPlaneSource()
    plane.Update()

    # Apply texture
    reader = vtkJPEGReader()
    reader.SetFileName(texture_file)
    reader.Update()

    texture = vtkTexture()
    texture.SetInputConnection(reader.GetOutputPort())

    # Apply transformation
    transform = vtkTransform()
    transform.Translate(*translation)
    transform.RotateX(rotation[0])
    transform.RotateY(rotation[1])
    transform.RotateZ(rotation[2])

    transformFilter = vtkTransformPolyDataFilter()
    transformFilter.SetTransform(transform)
    transformFilter.SetInputConnection(plane.GetOutputPort())
    transformFilter.Update()

    # Mapper and actor
    mapper = vtkPolyDataMapper()
    mapper.SetInputConnection(transformFilter.GetOutputPort())

    actor = vtkActor()
    actor.SetMapper(mapper)
    actor.SetTexture(texture)

    return actor


if __name__ == "__main__":
    main()
