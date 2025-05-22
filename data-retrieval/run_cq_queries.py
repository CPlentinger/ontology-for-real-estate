import time

from SPARQLWrapper import SPARQLWrapper, JSONLD


sparql = SPARQLWrapper("http://localhost:3000/sparql")

sparql_files = [
    "../sparql/1.sparql",
    "../sparql/2.sparql",
    "../sparql/3.sparql",
    "../sparql/4.sparql",
    "../sparql/5.sparql",
    "../sparql/6.sparql",
    "../sparql/7.sparql",
    "../sparql/8.sparql",
    "../sparql/9.sparql",
    "../sparql/10.sparql",
    "../sparql/11.sparql",
]

for sparql_file in sparql_files:
    with open(sparql_file, "r") as file:
        query = file.read()
        sparql.setQuery(query)
        sparql.setReturnFormat(JSONLD)
        start_time = time.time()
        results = sparql.query().convert()
        end_time = time.time()

        print(f"Results for competency question query: {sparql_file}")
        print(f"Query execution time: {end_time - start_time} seconds")
        print(f"Number of results: {len(results['results']['bindings'])}")
        print("-" * 50)
        for result in results["results"]["bindings"]:
            print(result)
        print("-" * 50)
