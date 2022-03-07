import sqlite3
import os

from flask import Flask, render_template

app = Flask(__name__)

base_dir = os.path.dirname(__file__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/index')
def home():
    return render_template("index.html")


@app.route('/movie')
def movie():
    datalist = []
    con = sqlite3.connect(os.path.join(base_dir, 'movie.db'))  # 拼接绝对路径
    cur = con.cursor()
    sql = "select * from movie250"
    data = cur.execute(sql)
    print(data)
    for item in data:
        datalist.append(item)
    cur.close()
    con.close()
    return render_template("movie.html", movies=datalist)


@app.route('/score')
def score():
    score_list = []  # 评分列表
    num_list = []  # 每个电影评分对应的电影数量列表
    con = sqlite3.connect(os.path.join(base_dir, 'movie.db'))  # 拼接绝对路径
    cur = con.cursor()
    sql = "select score,count(score) from movie250 group by score"
    data = cur.execute(sql)
    for item in data:
        score_list.append(str(item[0]))
        num_list.append(item[1])
    cur.close()
    con.close()
    return render_template("score.html", score_list=score_list, num_list=num_list)


@app.route('/word')
def word():
    return render_template("word.html")


# @app.route('/team')
# def team():
#     return render_template("team.html")


if __name__ == '__main__':
    app.run()
