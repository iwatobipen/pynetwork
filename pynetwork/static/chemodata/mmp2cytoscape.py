import igraph
from py2cytoscape.data.cyrest_client import CyRestClient
import py2cytoscape

cy = CyRestClient()
cy.session.delete()
G = igraph.Graph()

with open('testdata.smi', 'r') as vertexis:
    for v in vertexis:
        G.add_vertex(v.split(' ')[0], molname=v.split(' ')[1])

with open("testmmp.txt", "r") as edges:
    for edge in edges:
        G.add_edge(edge.split(",")[0], edge.split(",")[1], transform=edge.split(",")[4])

g_cy = cy.network.create_from_igraph(G)
cy.layout.apply(name='force-directed', network=g_cy)

mystyle = cy.style.create('mystyle')

defaults = {
    'NODE_HIGHT': 100,
    'NODE_WIDTH': 100,
    'NODE_FILL_COLOR': "#87CEFA",
    'NODE_BORDER_WIDTH': 5,
    'NODE_BORDER_PAINT': '#FFFFFF',
    'NODE_LABEL_FONT_SIZE': 14,
    'NODE_LABEL_COLOR': '#555555',
    'EDGE_TRANSPARENCY': 100,
    'EDGE_WIDTH': 20,
    'EDGE_STROKE_UNSELECTED_PAINT': '#FFFFFF',
    'NETWORK_BACKGROUND_PAINT': '#3B426F'
}

mystyle.update_defaults(defaults)
cy.style.apply(mystyle, network=g_cy)

print(py2cytoscape.util.from_igraph(G))
