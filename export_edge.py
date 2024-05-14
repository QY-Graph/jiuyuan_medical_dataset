from py2neo import Graph

# 连接到Neo4j数据库
graph = Graph("bolt://localhost:7687", auth=("neo4j", "hpcgrid3102"))

# 获取所有关系类型
relationship_types = graph.run("CALL db.relationshipTypes()").data()

# 为每种关系类型导出CSV
for rel_type in relationship_types:
    type_name = rel_type['relationshipType']
    filename = f"./medical/edges/{type_name}.csv"
    cypher_query = f"MATCH (a)-[r:{type_name}]->(b) RETURN id(a) as a_id, labels(a) as a_labels, id(b) as b_id, labels(b) as b_labels, r"
    export_query = f"CALL apoc.export.csv.query(\"{cypher_query}\", \"{filename}\", {{d:'|'}})"
    graph.run(export_query)
    print(f"Exported {type_name} relationships to {filename}")
