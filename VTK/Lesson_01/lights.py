###############################################################################
#       						Cone.py
###############################################################################

# This example creates a polygonal model of a Cone e visualize the results in a
# VTK render window.
# The program creates the cone, rotates it 360º and closes
# The pipeline  source -> mapper -> actor -> renderer  is typical
# and can be found in most VTK programs

# Imports

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

    # We Create an instance of vtkConeSource and set some of its
    # properties. The instance of vtkConeSource "cone" is part of a
    # visualization pipeline (it is a source process object); it produces data
    # (output type is vtkPolyData) which other filters may process.

    coneSource = vtkConeSource()
    coneSource.SetHeight(2.0)
    coneSource.SetRadius(1.0)
    coneSource.SetResolution(20)

    # We create an instance of vtkPolyDataMapper to map the polygonal data
    # into graphics primitives. We connect the output of the cone source
    # to the input of this mapper.

    coneMapper = vtkPolyDataMapper()
    coneMapper.SetInputConnection(coneSource.GetOutputPort())

    # We create an actor to represent the cone. The actor orchestrates rendering
    # of the mapper's graphics primitives. An actor also refers to properties
    # via a vtkProperty instance, and includes an internal transformation
    # matrix. We set this actor's mapper to be coneMapper which we created
    # above.

    coneActor = vtkActor()
    coneActor.SetMapper(coneMapper)


    # Create the Renderer and assign actors to it. A renderer is like a
    # viewport. It is part or all of a window on the screen and it is
    # responsible for drawing the actors it has.  We also set the background
    # color here.
    ren = vtkRenderer()
    ren.AddActor(coneActor)

    ren.SetBackground(1, 1, 1)

    # cam1 = ren.GetActiveCamera()
    # cam1.SetPosition(10,0,0)
    # cam1.SetViewUp(0,1,1)
    # cam1.SetParallelProjection(False)
    # ren.SetActiveCamera(cam1)

    red = (1,0,0)
    green = (0,1,0)
    blue = (0,0,1)
    yellow = (1,1,0)

    # activateLightInPos(ren, red, (-5,0,0))
    # activateLightInPos(ren, green, (0,0,-5))
    # activateLightInPos(ren, blue, (5,0,0))
    # activateLightInPos(ren, yellow, (0,0,5))

    activateLightAndSphereAtPos(ren, red, (-5,0,0))
    activateLightAndSphereAtPos(ren, green, (0,0,-5))
    activateLightAndSphereAtPos(ren, blue, (5,0,0))
    activateLightAndSphereAtPos(ren, yellow, (0,0,5))
        

    # Finally we create the render window which will show up on the screen.
    # We put our renderer into the render window using AddRenderer. We also
    # set the size to be 300 pixels by 300.

    renWin = vtkRenderWindow()
    renWin.AddRenderer(ren)

    renWin.SetSize(300, 300)

    # renWin.SetWindowName('Cone')
    renWin.SetWindowName("Cone, Sphere and Cylinder")

    # # Now we loop over 360 degrees and render the cone each time.
    # for i in range(0,360):
    #     # render the image
    #     renWin.Render()
    #     # rotate the active camera by one degree
    #     ren.GetActiveCamera().Azimuth(1)
    # Adds a render window interactor to the cone example to


# enable user interaction (e.g. to rotate the scene)
    iren = vtkRenderWindowInteractor()
    iren.SetRenderWindow(renWin)
    iren.Initialize()
    iren.Start()


def activateLightInPos(renderer, lightColor, lightPosition):
    light = vtkLight()
    light.SetColor(lightColor)
    light.SetPosition(lightPosition)
    renderer.AddLight(light)

def activateLightAndSphereAtPos(renderer, lightColor, lightPosition):
    light = vtkLight()
    light.SetColor(lightColor)
    light.SetPosition(lightPosition)
    renderer.AddLight(light)

    sphereSource = vtkSphereSource()
    sphereSource.SetCenter(lightPosition)
    sphereSource.SetRadius(0.5)

    sphereMapper = vtkPolyDataMapper()
    sphereMapper.SetInputConnection(sphereSource.GetOutputPort())

    sphereActor = vtkActor()
    sphereActor.SetMapper(sphereMapper)
    sphereActor.GetProperty().SetColor(lightColor)
    sphereActor.GetProperty().LightingOff()

    renderer.AddActor(sphereActor)


if __name__ == "__main__":
    main()


