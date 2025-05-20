java -jar /usr/local/bin/rmlmapper.jar -m mapping_core.rml.ttl -s turtle -o result.ttl

npx yarrrml-parser -i mapping_core.yml -o mapping_core.rml.ttl -c


PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX re: <https://cplentinger.github.io/ontology-for-real-estate/real-estate-listing#>
PREFIX ex: <http://example.com/#>

SELECT ?subject
WHERE {
?subject rdf:type re:RealEstateListing
}