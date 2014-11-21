# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# test - 副本.py
# Created on: 2014-11-20 12:46:25.00000
#   (generated by ArcGIS/ModelBuilder)
# Usage: test - 副本 <Z_value_field> <polygon> <Power> <symbol_type> <result_temp2> 
# Description: 
# 测试
# ---------------------------------------------------------------------------

# Import arcpy module
import arcpy

# Check out any necessary licenses
arcpy.CheckOutExtension("spatial")

# Load required toolboxes
arcpy.ImportToolbox("E:/InterpolationService/InterpolationService.tbx")

# Script arguments
Z_value_field = arcpy.GetParameterAsText(0)
if Z_value_field == '#' or not Z_value_field:
    Z_value_field = "tu_pb" # provide a default value if unspecified

polygon = arcpy.GetParameterAsText(1)
if polygon == '#' or not polygon:
    polygon = "in_memory\\{4799DAF6-B6DE-4983-A79F-EC5CC46BD241}" # provide a default value if unspecified

Power = arcpy.GetParameterAsText(2)
if Power == '#' or not Power:
    Power = "2" # provide a default value if unspecified

symbol_type = arcpy.GetParameterAsText(3)
if symbol_type == '#' or not symbol_type:
    symbol_type = "Classified" # provide a default value if unspecified

result_temp2 = arcpy.GetParameterAsText(4)

# Local variables:
result_temp = Z_value_field
Intersect_shp = polygon
xiangtan2_DBO_samples = "xiangtan2.DBO.samples"

# Process: 相交
arcpy.Intersect_analysis("in_memory\\{9EDBE80A-D6AC-468B-B2D5-2AA773F9BCEC} #;xiangtan2.DBO.samples #", Intersect_shp, "ALL", "", "POINT")

# Process: IDW
arcpy.gp.Idw_sa(Intersect_shp, Z_value_field, result_temp, "225.823841199994", Power, "VARIABLE 12", "")

# Process: set_symbology2
arcpy.gp.toolbox = "E:/InterpolationService/InterpolationService.tbx";
# Warning: the toolbox E:/InterpolationService/InterpolationService.tbx DOES NOT have an alias. 
# Please assign this toolbox an alias to avoid tool name collisions
# And replace arcpy.gp.set-symbology2(...) with arcpy.set-symbology2_ALIAS(...)
arcpy.gp.set-symbology2(symbol_type, result_temp)

