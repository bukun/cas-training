import folium

m = folium.Map(location=[35, 105], width=750, height=500)


from folium import GeoJson
import json

# import GeoJson

# Providing filename that shall be embedded.
jname = 'xx_gson.json'
GeoJson(jname)
# Providing filename that shall not be embedded.
GeoJson(jname, embed=False)
# Providing dict.
GeoJson(json.load(open(jname)))
# Providing string.
geojson = GeoJson(open(jname).read())

# Provide a style_function that color all states green but Alabama.
# style_function = lambda x: {'fillColor': '#0000ff' if x['properties']['name'] == '中华人民共和国' else '#00ff00'}
# GeoJson(geojson, style_function=style_function)

folium.ClickForMarker().add_to(m)

geojson.add_to(m)

m.save('xx_gson.html')


cnts = open('xx_gson.html').read()

with open('xx_picinfo202008.html', 'w') as fo:
    cnts = cnts.replace('https://cdn.jsdelivr.net/npm/leaflet@1.6.0/dist/leaflet.js',
                        'https://www.osgeo.cn/_f2elib/leaflet_1.3.1/leaflet.js')
    cnts = cnts.replace('https://code.jquery.com/jquery-1.12.4.min.js',
                        'https://www.osgeo.cn/_f2elib/jquery/jquery-3.3.1.min.js')
    cnts = cnts.replace('https://maxcdn.bootstrapcdn.com/bootstrap/3.2.0/js/bootstrap.min.js',
                        'https://www.osgeo.cn/_f2elib/bootstrap_3.3.7/js/bootstrap.min.js')

    cnts = cnts.replace(
        'https://cdnjs.cloudflare.com/ajax/libs/Leaflet.awesome-markers/2.0.2/leaflet.awesome-markers.js',
        '')

    cnts = cnts.replace(
        'https://cdn.jsdelivr.net/npm/leaflet@1.6.0/dist/leaflet.css',
        'https://www.osgeo.cn/_f2elib/leaflet_1.3.1/leaflet.css')

    cnts = cnts.replace(
        'https://maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap.min.css',
        'https://www.osgeo.cn/_f2elib/bootstrap_3.3.7/css/bootstrap.min.css')

    cnts = cnts.replace(
        'https://maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap-theme.min.css',
        '')
    cnts = cnts.replace(
        'https://maxcdn.bootstrapcdn.com/font-awesome/4.6.3/css/font-awesome.min.css',
        '')

    cnts = cnts.replace(
        'https://cdnjs.cloudflare.com/ajax/libs/Leaflet.awesome-markers/2.0.2/leaflet.awesome-markers.css',
        '')

    cnts = cnts.replace(
        'https://rawcdn.githack.com/python-visualization/folium/master/folium/templates/leaflet.awesome.rotate.css',
        '')
    ###################
    cnts = cnts.replace(
        '<script src=""></script>',
        '')
    cnts = cnts.replace(
        '<link rel="stylesheet" href=""/>',
        '')

    fo.write(cnts)