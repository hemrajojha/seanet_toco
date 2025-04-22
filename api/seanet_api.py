from rdflib import Graph, Namespace

NET = Namespace("http://example.org/seanet#")

def connect_all_hosts(g: Graph):
    hosts = list(g.subjects(predicate=NET.hasPort))
    for i in range(len(hosts)):
        for j in range(i+1, len(hosts)):
            g.add((hosts[i], NET.connectedTo, hosts[j]))

def block_hosts(g: Graph, host_ids):
    for host in host_ids:
        for s, p, o in list(g.triples((NET[host], None, None))):
            g.remove((s, p, o))
