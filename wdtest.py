#!/usr/bin/python3
# -*- codeing = utf-8 -*-
# @Time : 2021/9/1 12:29
# @Author: 王治国
# @File : wdtest.py
# @Software:PyCharm
from matplotlib.pyplot import imread
from wordcloud import ImageColorGenerator, WordCloud
from matplotlib import pyplot as plt  # 绘图数据可视化


font = "C:/Fonts/AaMingYueJiuLinTian.ttf"
mask_image = imread(r'.\static\assets\img\djcloud.jpg')

bg_color = ImageColorGenerator(mask_image, default_color=None)
wc = WordCloud(font_path=font,
              background_color="white",
              mask=mask_image,
              color_func=bg_color)


wc.fit_words(1)

plt.imshow(wc)
plt.axis("off")
plt.show()
