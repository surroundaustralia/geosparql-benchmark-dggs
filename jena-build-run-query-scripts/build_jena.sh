export PATH=/usr/local/apache-maven-3.8.4/bin:$PATH &&
cd /mnt/sda2/Surround/jena-source/jena/jena-geosparql &&
mvn clean install &&
cd /mnt/sda2/Surround/jena-source/jena/jena-fuseki2/jena-fuseki-geosparql &&
mvn clean install
