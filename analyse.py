import json
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.style as style
import getData


style.use('seaborn-colorblind')    # 设置图表风格
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签


def draw_bar(data_dic):
    labels = []     # 存放label
    count = []
    # 分别得到 count 的 key 和 value
    for key, value in data_dic.items():
        labels.append(key)
        count.append(value)
    # 生成 keys 个数的数组
    x = np.arange(len(labels)) + 1
    # 将 values 转换成数组
    y = np.array(count)

    fig, axes = plt.subplots(figsize=(10, 8))
    axes.bar(x, y, color="#1195d0")
    plt.xticks(x, labels, size=13, rotation=0)
    # 根据坐标将数字标在图中，ha、va 为对齐方式
    for a, b in zip(x, y):
        plt.text(a, b + 1, '%.0f' % b, ha='center', va='bottom', fontsize=12)
    plt.show()


# 绘制环状图
def draw_pie(dic):
    labels = []
    count = []

    for key, value in dic.items():
        labels.append(key)
        count.append(value)

    fig, ax = plt.subplots(figsize=(13, 10), subplot_kw=dict(aspect="equal"))

    # 绘制饼状图，wedgeprops 表示每个扇形的宽度
    wedges, texts = ax.pie(count, wedgeprops=dict(width=0.5), startangle=0)
    # 文本框设置
    bbox_props = dict(boxstyle="square,pad=0.9", fc="w", ec="k", lw=0)
    # 线与箭头设置
    kw = dict(xycoords='data', textcoords='data', arrowprops=dict(arrowstyle="-"),
              bbox=bbox_props, zorder=0, va="center")

    for i, p in enumerate(wedges):
        ang = (p.theta2 - p.theta1) / 2. + p.theta1
        y = np.sin(np.deg2rad(ang))
        x = np.cos(np.deg2rad(ang))
        # 设置文本框在扇形的哪一侧
        horizontalalignment = {-1: "right", 1: "left"}[int(np.sign(x))]
        # 用于设置箭头的弯曲程度
        connectionstyle = "angle,angleA=0,angleB={}".format(ang)
        kw["arrowprops"].update({"connectionstyle": connectionstyle})
        # annotate()用于对已绘制的图形做标注，text是注释文本，含 'xy' 的参数跟坐标点有关
        text = labels[i] + ": " + str('%.2f' % ((count[i]) / sum(count) * 100)) + "%"
        ax.annotate(text, size=12, xy=(x, y), xytext=(1.35 * np.sign(x), 1.4 * y),
                    horizontalalignment=horizontalalignment, **kw)
    plt.show()


with open("./friend_message.json", 'r', encoding='utf-8') as file:
    f_msg = json.load(file)
file.close()

sex_dic, sex_list = getData.get_gender(f_msg)
city_list = getData.get_city(f_msg)
# 将三个属性组成 DataFrame
data = pd.DataFrame({'gender': sex_list, 'city': city_list})
# 获取城市前十的数量
city_dict = data['city'].value_counts()[:15].to_dict()
# 绘制性别环状图
draw_pie(sex_dic)
# 绘制城市柱状图
draw_bar(city_dict)

