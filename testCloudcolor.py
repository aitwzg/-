#!/usr/bin/python3
# -*- codeing = utf-8 -*-
# @Time : 2021/9/1 13:04
# @Author: 王治国
# @File : testCloudcolor.py.py
# @Software:PyCharm
import jieba  # 分词
from matplotlib import pyplot as plt  # 绘图数据可视化
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator  # 词云
from PIL import Image  # 图片处理
import numpy as np  # 矩阵运算
import sqlite3  # 数据库

con = sqlite3.connect('movie.db')
cur = con.cursor()
sql = 'select introduction from movie250'
data = cur.execute(sql)
text = ""
for item in data:
    text = text + item[0]

cur.close()
con.close()
cut = jieba.cut(text)

string = ' '.join(cut)
print(len(string))
img = Image.open(r'.\static\assets\img\djcloud.jpg')
img_array = np.array(img)
wc = WordCloud(
    background_color='white',
    mask=img_array,
    font_path="msyh.ttc"
)
wc.generate_from_text(string)
image_colors = ImageColorGenerator(img_array)

plt.imshow(img, interpolation="None")
plt.axis("off")
plt.show()
plt.imshow(wc, interpolation="None")
plt.axis("off")
plt.show()
plt.imshow(wc.recolor(color_func=image_colors), alpha=0.98, interpolation="None")
plt.axis("off")
plt.show()
# plt.savefig(r'.\static\assets\img\djword6.jpg', dpi=500)
