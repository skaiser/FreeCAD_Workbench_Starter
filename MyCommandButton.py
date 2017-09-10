#########################################################################################
#  This file is part of the FreeCAD_Workbench_Starter project.
#
#  Copyright (C) 2017 Stephen Kaiser <freesol29|at|gmail.com>
#
#  This library is free software; you can redistribute it and/or
#  modify it under the terms of the GNU Lesser General Public
#  License as published by the Free Software Foundation; either
#  version 2 of the License, or (at your option) any later version.
#                                                                                     
#  This library is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
#  Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public
#  License along with this library; if not, If not, see 
#  <http://www.gnu.org/licenses/>.
#
#########################################################################################
#!/usr/bin/python

import FreeCAD, Part
from FreeCAD import Gui

# Locate Workbench Directory
import os, FindIconPath
path_D3D = os.path.dirname(FindIconPath.__file__)
path_D3D_icons =  os.path.join(path_D3D, 'icons')

class MyCommandButtonClass():
    """Command to add the printer frame"""

    def GetResources(self):
        return {'Pixmap'  : path_D3D_icons + '/DrawStyleWireFrame.svg', # the name of a svg file available in the resources
                'Accel' : "Shift+S", # a default shortcut (optional)
                'MenuText': "Add a frame",
                'ToolTip' : "Adds a D3D printer frame"}

    def Activated(self):
        "Do something here when button is clicked"
        FreeCAD.Console.PrintMessage("Workbench is working!")
        if Gui.ActiveDocument == None:
            FreeCAD.newDocument()
#        view = Gui.activeDocument().activeView()
        doc=FreeCAD.activeDocument()
        n=list()
        c = Part.Circle() 
        c.Radius=2.0
        f = doc.addObject("Part::Feature", "Circle") # create a document with a circle feature
        f.Shape = c.toShape() # Assign the circle shape to the shape property
        doc.recompute()
        return

    def IsActive(self):
        """Here you can define if the command must be active or not (greyed) if certain conditions
        are met or not. This function is optional."""
        return True

Gui.addCommand('MyCommandButton', MyCommandButtonClass()) 
