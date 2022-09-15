from neo4j import GraphDatabase

# 关于neo4j数据库的用户名,密码信息已经配置在同目录下的config.py文件中
from config import NEO4J_CONFIG

driver = GraphDatabase.driver( **NEO4J_CONFIG)

def _some_operations(tx, cat_name, mouse_name):
    tx.run("MERGE (a:Cat{name: $cat_name})"
           "MERGE (b:Mouse{name: $mouse_name})"
           "MERGE (a)-[r:And]-(b)",
           cat_name=cat_name, mouse_name=mouse_name)


with driver.session() as session:
    session.write_transaction(_some_operations, "Tom", "Jerry")