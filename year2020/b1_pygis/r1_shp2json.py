from osgeo import ogr
import gdal
import os

shapefile = 'shps/AFG_adm2_v165.shp'
outjson = 'xx_gson.json'

shp_ds = ogr.Open(shapefile)
shp_lyr = shp_ds.GetLayer(0)

# 创建结果Geojson
baseName = os.path.basename(outjson)
out_driver = ogr.GetDriverByName('GeoJSON')
out_ds = out_driver.CreateDataSource(outjson)
if out_ds.GetLayer(baseName):
    out_ds.DeleteLayer(baseName)
out_lyr = out_ds.CreateLayer(baseName, shp_lyr.GetSpatialRef())
out_lyr.CreateFields(shp_lyr.schema)
out_feat = ogr.Feature(out_lyr.GetLayerDefn())

# 生成结果文件
for feature in shp_lyr:
    out_feat.SetGeometry(feature.geometry())
    for j in range(feature.GetFieldCount()):
        out_feat.SetField(j, feature.GetField(j))
    out_lyr.CreateFeature(out_feat)

del out_ds
del shp_ds

