# ==================================================
# FreeCAD 3D To OpenSCAD
# ==================================================
# Copyright by Daizyu. since 3 Sep, 2016.
# version 1.0 Create 3 Sep, 2016.
# version 1.1 Update 3 Sep, 2016.
#    Change order "Rotate" and "Translate".
# version 1.2 Update 4 Sep, 2016.
#    create module for easy to modify. 
# ==================================================
# Software licensing
# License
# This program is free software; you can redistribute it and/or modify it 
# under the terms of the GNU General Public License as published 
# by the Free Software Foundation; either version 2 of the License, 
# or (at your option) any later version.
# Please visit this link for a copy of the license: GPL 2.0
# http://www.gnu.org/licenses/gpl-2.0.html
# ==================================================

import Mesh
import Tkinter
import tkMessageBox
import subprocess
import os
import math

class Conv2OpenSCAD:

	def __init__(self):
		self.root = Tkinter.Tk()
		self.root.withdraw()		
		self.TITLE = 'Conv to OpenSCAD'		
		self.doc=App.activeDocument()		
	
	def writeSTL(self,fp,obj,indent):
			fp.write('%simport("%s.stl");\n'%("  "*indent,obj.Name))
		
			__objs__=[]
			__objs__.append(obj)
			Mesh.export(__objs__,os.path.join(self.basedir,obj.Name+'.stl'))
			del __objs__
	
	def sphere(self,fp,obj,indent):
		indent += 1
		if obj.Angle1==-90.0 and obj.Angle2==90.0 and obj.Angle3==360.0:
			self.writeplacement(fp,obj,indent)
			fp.write('%ssphere(r=%f);\n'%("  "*indent,obj.Radius))
		else:
			writeSTL(fp,obj,indent)
	
	def cone(self,fp,obj,indent):
		indent += 1
		if obj.Angle==360.0:
			self.writeplacement(fp,obj,indent)
			fp.write('%scylinder(h = %f, r1 = %f, r2 = %f);\n'%("  "*indent,obj.Height,obj.Radius1,obj.Radius2))
		else:
			writeSTL(fp,obj,indent)
	
	def cylinder(self,fp,obj,indent):
		indent += 1
		if obj.Angle==360.0:
			self.writeplacement(fp,obj,indent)
			fp.write('%scylinder(h = %f, r = %f);\n'%("  "*indent,obj.Height,obj.Radius))
		else:
			writeSTL(fp,obj,indent)

	def box(self,fp,obj,indent):
		indent += 1
		self.writeplacement(fp,obj,indent)
		fp.write('%scube([%f,%f,%f]);\n'%("  "*indent,obj.Length,obj.Width,obj.Height))
	
	
	def writeplacement(self,fp,obj,indent):
	
		base = obj.Placement.Base
		if base[0]!=0.0 or base[1]!=0.0 or base[2]!=0.0 :
			fp.write('%stranslate([%f,%f,%f])\n'%
				("  "*indent, base[0],base[1],base[2] ))
		if obj.Placement.Rotation.Angle != 0.0 :
			fp.write('%srotate(a=%f, v=[%f,%f,%f])\n'%
				("  "*indent,
				math.degrees(obj.Placement.Rotation.Angle),
				obj.Placement.Rotation.Axis[0],
				obj.Placement.Rotation.Axis[1],
				obj.Placement.Rotation.Axis[2]))
		
	def Proc(self,fp,obj,indent):
	
		indent += 1
		if obj.TypeId=='Part::MultiFuse'	:
			self.writeplacement(fp,obj,indent)
			fp.write('%sunion(){\n'%("  "*indent))
		elif obj.TypeId=='Part::Cut'	:
			self.writeplacement(fp,obj,indent)
			fp.write('%sdifference(){\n'%("  "*indent))
		elif obj.TypeId=='Part::MultiCommon'	:
			self.writeplacement(fp,obj,indent)
			fp.write('%sintersection(){\n'%("  "*indent))
		elif obj.TypeId=='Part::Sphere'	:
			self.sphere(fp,obj,indent)
			return
		elif obj.TypeId=='Part::Box'	:
			self.box(fp,obj,indent)
			return		
		elif obj.TypeId=='Part::Cylinder'	:
			self.cylinder(fp,obj,indent)
			return		
		elif obj.TypeId=='Part::Cone'	:
			self.cone(fp,obj,indent)
			return
		else:
			self.writeSTL(fp,obj,indent)
			return
	
		for subObj in obj.OutList :
			self.Proc(fp,subObj,indent)
		fp.write('%s}\n'%("  "*indent))

	def proc(self):
	
		filename = Gui.ActiveDocument.Document.FileName
		if filename == u'':
			tkMessageBox.showinfo(self.TITLE,'Please save document before convert.')
			return

		self.basedir = os.path.join(
			os.path.dirname(filename) , 
			'openSCAD-' + os.path.basename(filename) )
		self.openscad = os.path.join(
			self.basedir , 
			'openSCAD-' + os.path.basename(filename) + '.scad' )
		if not os.path.exists(self.basedir):
			os.mkdir(self.basedir)

		fp = open(self.openscad,'w+')
		fp.write('$fn=100;\n')
		
		indent = 0
		iPartsNum = 0
		for obj in self.doc.Objects:
			if len(obj.InList)==0 :
				fp.write('module parts%d(){\n'%iPartsNum)
				self.Proc(fp,obj,indent)
				iPartsNum += 1
				fp.write('}\n')

		fp.write('\n')
		
		for idx in range(iPartsNum):
			fp.write('parts%d();\n'%idx)
				
		fp.close()
		
		tkMessageBox.showinfo(self.TITLE,'Complete')

conv2OpenSCAD = Conv2OpenSCAD()

conv2OpenSCAD.proc()
