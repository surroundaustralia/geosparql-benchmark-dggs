# Run Jena including the DGGS jar for SF functions
Example docker command:
`docker run -p 3030:3030 -v <REPO_DIR>/dggs-jar/current:/fuseki-extra --name jena-dggs stain/jena-fuseki:4.0.0`
NB: version 4.0.0 includes code to copy the jar files to the java classpath. Version 4.0.0 is *not* tagged with 'latest'
on dockerhub, so it must be explicitly specified (or the jar files manually added to the classpath).
You will need to obtain the fuseki password from the log output of docker. This can be automated with a shiro.ini file
but has not been done for this repo.
# Utilising functions
1. Create a dataset in Jena
2. Upload `output/dataset_dggs_level_7.ttl` to the dataset
3. Run queries in the following format:
```PREFIX f: <java:main.dggs.geosparql.>
PREFIX geo: <http://www.opengis.net/ont/geosparql#>

SELECT ?a ?geoma ?b ?geomb {
  ?a geo:hasGeometry / geo:asDGGS ?geoma .
  { SELECT ?b ?geomb {
  	?b geo:hasGeometry / geo:asDGGS ?geomb .
	}
  }
  FILTER (?a != ?b)
  FILTER(f:SFWithin(?geoma, ?geomb))
}
```
