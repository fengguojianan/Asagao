import jieba
import jieba.posseg as pseg
import pandas as pd
import matplotlib.pyplot as plt

article=open('d:/python/xx.txt','r').read()
words=pd.DataFrame(jieba.cut(article))

words=words.rename(columns={0:'word'})
score=pd.read_table('d:/python/score.txt',encoding='utf8',sep=' ',names=['word','score'])

finish=pd.merge(left=words, right=score, how='left', left_on='word', right_on='word')

finish=finish[finish.score.isnull()==False]

print (finish.mean())






article=open('c:/python/hot/beiying.txt','r').read()
words=pd.DataFrame(jieba.cut(article))

words=words.rename(columns={0:'word'})
score=pd.read_table('c:/python/hot/score.txt',encoding='utf8',sep=' ',names=['word','score'])

finish=pd.merge(left=words, right=score, how='left', left_on='word', right_on='word')

finish=finish[finish.score.isnull()==False]
finish=finish[0:784]
finish=finish['score'].reshape(28,-1)

plt.matshow(finish, cmap=plt.cm.hot, vmin=-0.5, vmax=4)

plt.colorbar()

plt.show()