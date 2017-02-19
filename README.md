This is ...
---
FreeCAD is good tool.
But I think that Boolean engine is poor than other CAD.
Many times , FreeCAD created broken object.

This tool is second chance to convert broken models of FreeCAD.
This tool can convert from FreeCAD files to openSCAD files.  
You can use openSCAD boolean engine.

How to install
---
Macro filename is "ConvOpenSCAD.py".
Please put it into your macro folder.
http://www.freecadweb.org/wiki/index.php?title=How_to_install_macros

How to use
---
- Please create your model.

- Please save your model.

- Please run this macro.

- Display "Complete" dialog.
  Please click Ok button.

- Please open "scad file".
  This macro automatically create sub folder on your parent folder of  FreeCAD file.
  Folder name is "OpenSCAD - " & your FreeCAD filename.
  
 
Detail...
---
- This macro automatically create some STL files.
  This macro load and use these stl files for boolean process.

- This macro don't create STL for some futures.
   Sphere,Cylinder, cube,cone.
   These futures are converted to OpenScad modules.
   But if angle is modified , these futures will convert STL files. 

Advice
---
- Some time FreeCAD created broken STL files even if model is simple. 
  Please try to fix STL using netfabb before compile &render openSCAD.
  And sometime openSCAD create brken STL ,too. You need to fix such broken STL 
  netfabb has free licence mode.It is netfabb Basic.
  And netfabb has crowd mode.
  https://www.netfabb.com/products/netfabb-basic
  https://netfabb.azurewebsites.net/

- openSCAD boolean engine is better than FreeCAD.
  But this boolean engine is also not perfect.
  openSCAD boolean engine cannot create correct STL , you need to try to fix your self.
  For example  , you can cut out short parts nodes , and you can convert each short parts node to STL.  
  Or , you need to try to use other CAD.

Update...
---
- version 1.0 Create 3 Sep, 2016.
- version 1.1 Update 3 Sep, 2016.
    Change order "Rotate" and "Translate".
- version 1.2 Update 4 Sep, 2016.
    create module for easy to modify. 


Thank you for your reading.
 
