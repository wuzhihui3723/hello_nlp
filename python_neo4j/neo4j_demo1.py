from neo4j import GraphDatabase

# 关于neo4j数据库的用户名,密码信息已经配置在同目录下的config.py文件中
from config import NEO4J_CONFIG

driver = GraphDatabase.driver( **NEO4J_CONFIG)

# 直接用python代码形式访问节点Company, 并返回所有节点信息
with driver.session() as session:
    cypher = "CREATE(c:Company) SET c.name='野生程序员' RETURN c.name"
    record = session.run(cypher)
    result = list(map(lambda x: x[0], record))
    print("result:", result)