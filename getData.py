import PIL
import itchat


# 获取性别信息
def get_gender(message):
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

    return sex_dic, sex_list


# 获取省份信息
def get_province(message):
    province_list = []

    for i in range(1, len(message)):
        province = message[i]['Province']
        if province == '':
            province_list.append(None)
        else:
            province_list.append(province)

    return province_list


# 获取城市信息
def get_city(message):
    city_list = []

    for i in range(1, len(message)):
        city = message[i]['City']
        if city == '':
            city_list.append(None)
        else:
            city_list.append(city)

    return city_list





