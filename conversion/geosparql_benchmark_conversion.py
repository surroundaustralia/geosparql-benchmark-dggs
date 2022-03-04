from converter import lambda_convert
from rdflib import Graph, Literal, Namespace, URIRef

GEO = Namespace("http://www.opengis.net/ont/geosparql#")

g = Graph().parse(
    "https://raw.githubusercontent.com/OpenLinkSoftware/GeoSPARQLBenchmark/master/src/main/resources/gsb_dataset/dataset.rdf",
    format="xml",
)
geom_dict = {k: v for k, v in g.subject_objects(predicate=GEO.asWKT)}
geom_ids = [str(geom_id) for geom_id in list(geom_dict.keys())]
geom_wkt = []
for val in geom_dict.values():
    val = str(val).strip()
    if "EMPTY" in val:
        pass
    elif val == "":
        val = "POINT EMPTY"
    else:
        try:
            val = val.split("> ", 1)[1]
        except IndexError:
            pass
    geom_wkt.append(val)

level = 7
geom_dggs = lambda_convert(geom_ids, geom_wkt, "wkt", level)

geom_dggs_no_crs = {
    k: v.lstrip("<https://w3id.org/dggs/auspix> ") for k, v in geom_dggs.items()
}

# serialize with original data
for geom_id, dggs_geom in geom_dggs_no_crs.items():
    g.add((URIRef(geom_id), GEO.asDGGS, Literal(dggs_geom)))

g.serialize(f"output/dataset_dggs_level_{level}.rdf", format="xml")
g.serialize(f"output/dataset_dggs_level_{level}.ttl", format="turtle")
