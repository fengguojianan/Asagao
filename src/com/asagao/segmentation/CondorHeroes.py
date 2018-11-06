import jieba
import pandas as pd

#分割文本

s=open('/Users/zhouxiaocong/Documents/pythoncode/text/shendiaoxialv/shendiaoxialv.txt','r')
q=s.read()
f=q.split('\n')
x=1
for i in f:
    b=open('/Users/zhouxiaocong/Documents/pythoncode/text/shendiaoxialv/'+str(x)+'.txt','w')
    b.write(i)
    x+=1
    print (x)
s.close


#找词
x=1
result={'yangguo':[],'xiaolongnv':[],'guoxiang':[],'huangrong':[],'limochou':[],'honglingbo':[],'luwushuang':[],'guofu':[],'chengying':[],'wanyanping':[],'gongsunlve':[],'yelvyan':[]}

while x<=14325:
    a={'word':[],'count':[]}
    f=open('/Users/zhouxiaocong/Documents/pythoncode/text/shendiaoxialv/'+str(x)+'.txt','r').read()
    words=list(jieba.cut(f))
    #杨过
    if u'杨过' in words:
        result['yangguo'].append(1)
    elif u'过儿' in words:
        result['yangguo'].append(1)
    elif u'傻蛋' in words:
        result['yangguo'].append(1)
    elif u'臭小子' in words:
        result['yangguo'].append(1)
    elif u'杨少侠' in words:
        result['yangguo'].append(1)
    elif u'大哥哥' in words:
        result['yangguo'].append(1)
    elif u'西狂' in words:
        result['yangguo'].append(1)
    elif u'神雕大侠' in words:
        result['yangguo'].append(1)
    else:
        result['yangguo'].append(0)
    #小龙女
    if u'小龙女' in words:
        result['xiaolongnv'].append(1)
    elif u'姑姑' in words:
        result['xiaolongnv'].append(1)
    elif u'龙儿' in words:
        result['xiaolongnv'].append(1)
    elif u'龙姑娘' in words:
        result['xiaolongnv'].append(1)
    elif u'龙姐姐' in words:
        result['xiaolongnv'].append(1)
    else:
        result['xiaolongnv'].append(0)
    #郭襄
    if u'郭襄' in words:
        result['guoxiang'].append(1)
    elif u'襄儿' in words:
        result['guoxiang'].append(1)
    elif u'郭女侠' in words:
        result['guoxiang'].append(1)
    elif u'小东邪' in words:
        result['guoxiang'].append(1)
    else:
        result['guoxiang'].append(0)
    #黄蓉
    if u'黄蓉' in words:
        result['huangrong'].append(1)
    elif u'郭伯母' in words:
        result['huangrong'].append(1)
    elif u'蓉儿' in words:
        result['huangrong'].append(1)
    elif u'郭夫人' in words:
        result['huangrong'].append(1)
    elif u'黄帮主' in words:
        result['huangrong'].append(1)
    else:
        result['huangrong'].append(0)
    #李莫愁
    if u'李莫愁' in words:
        result['limochou'].append(1)
    elif u'赤练仙子' in words:
        result['limochou'].append(1)
    elif u'莫愁' in words:
        result['limochou'].append(1)
    elif u'女魔头' in words:
        result['limochou'].append(1)
    elif u'师姐' in words:
        result['limochou'].append(1)
    else:
        result['limochou'].append(0)

    # 洪凌波
    if u'洪凌波' in words:
        result['honglingbo'].append(1)
    elif u'凌波' in words:
        result['honglingbo'].append(1)
    else:
        result['honglingbo'].append(0)

    # 陆无双
    if u'陆无双' in words:
        result['luwushuang'].append(1)
    elif u'无双' in words:
        result['luwushuang'].append(1)
    elif u'双儿' in words:
        result['luwushuang'].append(1)
    elif u'媳妇儿' in words:
        result['luwushuang'].append(1)
    else:
        result['luwushuang'].append(0)

    # 郭芙
    if u'郭芙' in words:
        result['guofu'].append(1)
    elif u'芙儿' in words:
        result['guofu'].append(1)
    elif u'郭大小姐' in words:
        result['guofu'].append(1)
    elif u'郭世妹' in words:
        result['guofu'].append(1)
    else:
        result['guofu'].append(0)

    # 程英
    if u'程英' in words:
        result['chengying'].append(1)
    elif u'程姑娘' in words:
        result['chengying'].append(1)
    else:
        result['chengying'].append(0)

    # 完颜萍
    if u'完颜萍' in words:
        result['wanyanping'].append(1)
    else:
        result['wanyanping'].append(0)

    # 公孙绿萼
    if u'公孙绿萼' in words:
        result['gongsunlve'].append(1)
    if u'公孙姑娘' in words:
        result['gongsunlve'].append(1)
    if u'绿萼' in words:
        result['gongsunlve'].append(1)
    if u'萼儿' in words:
        result['gongsunlve'].append(1)
    else:
        result['gongsunlve'].append(0)

    # 耶律燕
    if u'耶律燕' in words:
        result['yelvyan'].append(1)
    else:
        result['yelvyan'].append(0)
    x += 1

result2={'role':[],'yangguo':[],'xiaolongnv':[],'guoxiang':[],'huangrong':[],'limochou':[],'honglingbo':[],'luwushuang':[],'guofu':[],'chengying':[],'wanyanping':[],'gongsunlve':[],'yelvyan':[]}

for a in b.columns.values:
    x=yangguo=xiaolongnv=guoxiang=huangrong=limochou=honglingbo=luwushuang=guofu=chengying=wanyanping=gongsunlve=yelvyan=0

    while x<=14325:
        if b.iloc[x][a]==1:
            if b.iloc[x]['yangguo'] == 1:
                yangguo += 1
            if b.iloc[x]['xiaolongnv'] == 1:
                xiaolongnv += 1
            if b.iloc[x]['guoxiang'] == 1:
                guoxiang += 1
            if b.iloc[x]['huangrong'] == 1:
                huangrong += 1
            if b.iloc[x]['limochou'] == 1:
                limochou += 1
            if b.iloc[x]['honglingbo'] == 1:
                honglingbo += 1
            if b.iloc[x]['luwushuang'] == 1:
                luwushuang += 1
            if b.iloc[x]['guofu'] == 1:
                guofu += 1
            if b.iloc[x]['chengying'] == 1:
                chengying += 1
            if b.iloc[x]['wanyanping'] == 1:
                wanyanping += 1
            if b.iloc[x]['gongsunlve'] == 1:
                gongsunlve += 1
            if b.iloc[x]['yelvyan'] == 1:
                yelvyan += 1


        x += 1
    result2['role'].append(a)
    result2['yangguo'].append(yangguo)
    result2['xiaolongnv'].append(xiaolongnv)
    result2['guoxiang'].append(guoxiang)
    result2['huangrong'].append(huangrong)
    result2['limochou'].append(limochou)
    result2['honglingbo'].append(honglingbo)
    result2['luwushuang'].append(luwushuang)
    result2['guofu'].append(guofu)
    result2['chengying'].append(chengying)
    result2['wanyanping'].append(wanyanping)
    result2['gongsunlve'].append(gongsunlve)
    result2['yelvyan'].append(yelvyan)


o = pd.DataFrame(result2)

o.to_csv('/Users/zhouxiaocong/Documents/pythoncode/text/shendiaoxialv/shendiaoxialv2.csv', mode='w', encoding='UTF-8')


