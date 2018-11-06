#加载需要使用的类库
from PIL import Image
import numpy as np
from wordcloud import WordCloud, ImageColorGenerator
from matplotlib import pyplot as plt
import jieba
import jieba.posseg as pseg
import pandas as pd


adj={'content':[],'cnt':[]}
for line in open('/Users/zhouxiaocong/Documents/pythoncode/text/duoqingjianke/多情剑客无情剑.txt','r'):

    adj['content'].append(line)
    words = pseg.cut(line)
    adj_cnt=0
    cnt=0
    for word, flag in words:
        if flag in ['Ag','a','ad','an']:
            adj_cnt+=1
        cnt+=1
    adj['cnt'].append(adj_cnt/cnt)
adj2=pd.DataFrame(adj)
adj2=adj2.sort_values(by = 'cnt',axis = 0,ascending = False)
print(adj2[:5])
c=pd.pivot_table(adj2,index=['content'],values=['cnt'],aggfunc=np.sum)
c.to_csv('/Users/zhouxiaocong/Documents/pythoncode/text/duoqingjianke/duoqingjianke.csv',mode='w',encoding='utf8')

#加载背景图片
cloud_mask = np.array(Image.open("/Users/zhouxiaocong/Documents/pythoncode/text/duoqingjianke/lxh.jpg"))
#忽略显示的词
#st=set(["东西","这是"])
#生成wordcloud对象
wc = WordCloud(background_color="white",
    mask=cloud_mask,
    max_words=200,
    font_path="./font/wb.ttf",
    min_font_size=15,
    max_font_size=50,
    width=400,
    #stopwords=st
               )


'''

cloud_text=adj2

wc.generate(cloud_text)
wc.to_file("/Users/zhouxiaocong/Documents/pythoncode/text/pic.png")


a={'word':[],'count':[]}
f=open('c:/python/wenben/chuan.txt','r',encoding='utf8').read()
words=list(jieba.cut(f))
for word in words:
    if len(word)>=4:
        a['word'].append(word)
        a['count'].append(1)
b=pd.DataFrame(a)
c=pd.pivot_table(b,index=['word'],values=['count'],aggfunc=np.sum)
c.to_csv('c:/python/wenben/chuan.csv',mode='w',encoding='utf8')
'''