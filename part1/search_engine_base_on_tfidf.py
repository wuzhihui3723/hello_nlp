import json

import jieba

from part1.calculate_tfidf import calculate_tfidf

#加载文档数据（可以想象成网页数据），计算每个网页的tfidf字典
def load_data(path):
    corpus = []
    with open(path,encoding="utf8") as f:
        documents = json.loads(f.read())
        for document in documents:
            corpus.append(document["title"]+"\n"+document["content"])
        tf_idf_dict = calculate_tfidf(corpus)
    return tf_idf_dict,corpus


def search_engine(query, tf_idf_dict, corpus,top = 3):
    query_words = jieba.lcut(query)
    res = []
    for doc_id,tf_idf in tf_idf_dict.items():
        score = 0
        for word in query_words:
            score += tf_idf.get(word,0)
        res.append([doc_id,score])
    res = sorted(res,reverse=True,key=lambda x:x[1])
    for i in range(top):
        doc_id = res[i][0]
        print(corpus[doc_id])
        print("--------")


    return res


if __name__ == '__main__':
    path = "data/sogou_news.json"
    tf_idf_dict,corpus = load_data(path)
    while True:
        query = input("请输入您要搜索的内容:")
        search_engine(query,tf_idf_dict,corpus)
    # print(tf_idf_dict)
    # print("-------")
    # print(corpus)