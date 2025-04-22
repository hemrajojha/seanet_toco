# SeaNet on Google Colab

## Requirements
```python
!pip install rdflib
```

## How to Use

### 1. Generate RDF
```python
from generator.generate_kb import *
```

### 2. Manipulate Graph
```python
from rdflib import Graph
from api.seanet_api import *
g = Graph().parse("seanet.rdf", format="turtle")
connect_all_hosts(g)
block_hosts(g, ["host1"])
```

### 3. Query with SPARQL
```python
for row in g.query(open("sparql/queries.rq").read()):
    print(row)
```
