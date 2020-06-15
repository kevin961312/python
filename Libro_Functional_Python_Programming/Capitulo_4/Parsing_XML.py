import xml.etree.ElementTree as XML

def comma_split(text):
    return text.split(",")
    
def row_iter_kml(file_obj):
    ns_map = {
        "ns0": "http://www.opengis.net/kml/2.2",
        "ns1": "http://www.google.com/kml/ext/2.2"}
    xpath = (
        "./ns0:Placemark/ns0:Point/ns0:coordinates")
    doc = XML.parse(file_obj)
    return (
        comma_split(coordinates.text) for coordinates in doc.findall(xpath, ns_map)
    )

with open("./Capitulo_4/file_obj.xml") as source:
    sources = source.read()    
    data = list(row_iter_kml(sources))

def row_iter(source):
    return csv.reader(source, delimiter=",")

def pick_lan_lon(lon,lat,alt):
    return lat, lon
    
def lat_lon_kml(row_iter):
    return (pick_lat_lon(*row) for row in row_iter)