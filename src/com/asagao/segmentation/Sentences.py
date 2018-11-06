import jieba
import jieba.posseg as pseg
import pandas as pd
import matplotlib.pyplot as plt
from gensim.models import Word2Vec
#分词并生成语料库
f1 =open("c:/python/wenben/lu.txt",encoding='utf8')
f2 =open("c:/python/wenben/word.txt", 'w',encoding='utf8')
lu=f1.read()
lu.replace('\t','').replace('\n','').replace(' ','')
word = jieba.cut(lu)
f2.write(" ".join(word))
f1.close()
f2.close()
#用语料训练词向量
sentences =word2vec.Text8Corpus("c:/python/wenben/word.txt")
model =word2vec.Word2Vec(sentences, size=200)
#输出同义词
y = model.wv.most_similar("笑",topn=20)
for item in y:
    print (item[0], item[1])







result2={'role':[],'xiaobao':[],'ake':[],'suquan':[],'jianning':[],'shuanger':[],'junzhu':[],'fangyi':[],'zengrou':[]}

for a in b.columns.values:

    x=xiaobao=ake=suquan=jianning=shuanger=junzhu=fangyi=zengrou=0

    while x<=11580:

        if b.iloc[x][a]==1:

            if b.iloc[x]['xiaobao']==1:

                xiaobao+=1

            if b.iloc[x]['ake']==1:

                ake+=1

            ...

        x+=1

    result2['role'].append(a)

    result2['xiaobao'].append(xiaobao)

    result2['ake'].append(ake)

    result2['suquan'].append(suquan)

    result2['jianning'].append(jianning)

    result2['shuanger'].append(shuanger)

    result2['junzhu'].append(junzhu)

    result2['fangyi'].append(fangyi)

    result2['zengrou'].append(zengrou)

o=pd.DataFrame(result2)

o.to_csv('d:/lu/lu2.csv',mode='w',encoding='UTF-8')