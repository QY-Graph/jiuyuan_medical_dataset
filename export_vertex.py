from py2neo import Graph

# 连接到Neo4j数据库
graph = Graph("bolt://localhost:7687", auth=("neo4j", "hpcgrid3102"))

# 获取所有节点类型
labels = graph.run("CALL db.labels()").data()

# 为每种节点类型导出CSV
for label in labels:
    label_name = label['label']
    filename = f"./medical/vertices/{label_name}.csv"
    cypher_query = f"MATCH (n:{label_name}) RETURN n"
    export_query = f"CALL apoc.export.csv.query(\"{cypher_query}\", \"{filename}\", {{d:'|'}})"
    graph.run(export_query)
    print(f"Exported {label_name} nodes to {filename}")
