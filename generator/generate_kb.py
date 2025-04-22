from rdflib import Graph, Namespace

NET = Namespace("http://example.org/seanet#")
g = Graph()
g.bind("net", NET)

# Example triples
g.add((NET.switch1, NET.hasPort, NET.port1))
g.add((NET.host1, NET.hasPort, NET.port2))
g.serialize(destination="seanet.rdf", format="turtle")
