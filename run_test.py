# -*- coding: utf-8 -*-
from native_bayes_sentiment_analyzer import SentimentAnalyzer


model_path = './data/bayes.pkl'
userdict_path = './data/userdict.txt'
stopword_path = './data/stopwords.txt'
corpus_path = './data/review.csv'


analyzer = SentimentAnalyzer(model_path=model_path, stopword_path=stopword_path, userdict_path=userdict_path)
sentences = [
        "很好，演技不错",
        "要是好就奇怪了",
        "一星给字幕",
        "演技好，演技好，演技好，演技好，很差",
        "剧情还不错，但演员演技不行",
        "虽然剧情一般，但是演员演技非常好",
        "虽然演员演技好，但是剧情很糟糕",
        "虽然剧情不行，但是演员演技非常好",
        "这片子的逻辑就像片中的怪物一样，看不见。",
        "深深的隐喻。连儿子都杀。大邪若正。",
        "不是很喜欢。"
    ]
for i in range(len(sentences)):
    print(sentences[i])
    analyzer.analyze(text=sentences[i])
# text = '倍感失望的一部诺兰的电影，感觉更像是盗梦帮的一场大杂烩。虽然看之前就知道肯定是一部无法超越前传2的蝙蝠狭，但真心没想到能差到这个地步。节奏的把控的失误和角色的定位模糊绝对是整部影片的硬伤。'
# analyzer.analyze(text=text)
