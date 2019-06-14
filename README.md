# Wechat_Friends
<h2>&nbsp;一、itchat</h2>
<p>　　itchat是一个开源的微信个人号接口，这一次就用它来来玩玩。</p>
<p>　　在使用之前，先下载，老规矩通过 pip install itchat 即可安装。</p>
<p>　　想要获取朋友圈信息，只需要几行代码就可以获取。将获取到的信息保存到 json 文件中即可。</p>
<div>
<pre>def get_gender(message):
    sex_dic = {}
    sex_list = []

    for i in range(1, len(message)):
        sex = message[i]['Sex']
        if sex == 1:
            sex_dic['Male'] = sex_dic.get('Male', 0) + 1
            sex_list.append("男")
        elif sex == 2:
            sex_dic['Female'] = sex_dic.get('Female', 0) + 1
            sex_list.append("女")
        else:
            sex_dic['Unknown'] = sex_dic.get('Unknown', 0) + 1
            sex_list.append("Unknown")

    return sex_dic, sex_list</pre>
</div>
<h2>二、读取文件获取信息</h2>
<p>　　我们只需要关注里面其中的主要信息，按照需求获取。由于只是玩玩而已，就只单单获取性别和城市信息。</p>
<p>　　先获取性别信息</p>
<div>
<pre>def get_gender(message):
    sex_dic = {}
    sex_list = []

    for i in range(1, len(message)):
        sex = message[i]['Sex']
        if sex == 1:
            sex_dic['Male'] = sex_dic.get('Male', 0) + 1
            sex_list.append("男")
        elif sex == 2:
            sex_dic['Female'] = sex_dic.get('Female', 0) + 1
            sex_list.append("女")
        else:
            sex_dic['Unknown'] = sex_dic.get('Unknown', 0) + 1
            sex_list.append("Unknown")

    return sex_dic, sex_list</pre>
</div>
<p>　　再获取城市信息</p>
<div>
<pre>def get_city(message):
    city_list = []

    for i in range(1, len(message)):
        city = message[i]['City']
        if city == '':
            city_list.append(None)
        else:
            city_list.append(city)

    return city_list</pre>
</div>
<h2>三、可视化</h2>
<p>　　将性别绘制成饼状图，城市分布绘制成柱状图。具体绘制的代码就不上了</p>
<div>
<pre>
with open("./friend_message.json", 'r', encoding='utf-8') as file:
    f_msg = json.load(file)
file.close()

sex_dic, sex_list = getData.get_gender(f_msg)
city_list = getData.get_city(f_msg)
<p># 将三个属性组成 DataFrame</p>
data = pd.DataFrame({'gender': sex_list, 'city': city_list})
<p># 获取城市前十的数量</p>
city_dict = data['city'].value_counts()[:15].to_dict()
<p># 绘制性别环状图</p>
draw_pie(sex_dic)
<p># 绘制城市柱状图</p>
draw_bar(city_dict)
</pre>
</div>
<h2>四、总结</h2>
<p>　　　　　　<img src="https://img2018.cnblogs.com/blog/1458123/201906/1458123-20190614143801827-407630656.png" alt="" width="527" height="406" /></p>
<p>　　说实话，这里面的男生绝对大部分是在大学认识的，毕竟理工科学校可不是闹着玩儿的；还有这 6.58% 不明性别的人不知道怎么设置的，为什么我没办法不设置，还是说......</p>
<p>&nbsp;　　　　　　　<img src="https://img2018.cnblogs.com/blog/1458123/201906/1458123-20190614144433988-1260526753.png" alt="" width="600" height="480" /></p>
<p>　　作为一个在东莞上学的广东汕头人，这样的分布确实是在意料之中。毕竟汕头是我生活了那么久的地方，在东莞也快度过三个年头了，不知不觉要大四了，最近的压力已经逐渐增加了，无力吐槽。</p>
<p>&nbsp;</p>
<p>　　这只是玩玩而已，如果你有什么脑洞或者想要挖掘更多个人好友信息，可以使用 itchat 接着玩。</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
