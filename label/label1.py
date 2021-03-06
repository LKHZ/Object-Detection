# 标签1.0
# 每张图像的标签保存在不同的json文件中
import os
import simplejson
rootdir = r"D:/A_Postgraduate/Project/fits_segment/json文件/"

def get_target_value(key, dic, point_list):
    """
    :param key: 目标key值
    :param dic: JSON数据
    :param point_list:  用于存储获取的数据
    :return: list
    """
    if not isinstance(dic, dict) or not isinstance(point_list, list):  # 对传入数据进行格式校验
        return 'argv[1] not an dict or argv[-1] not an list '

    if key in dic.keys():
        point_list.append(dic[key])  # 传入数据存在则存入

    for value in dic.values():  # 传入数据不符合则对其value值进行遍历
        if isinstance(value, dict):
            get_target_value(key, value, point_list)  # 传入数据的value值是字典，则直接调用自身
        elif isinstance(value, (list, tuple)):
            _get_value(key, value, point_list)  # 传入数据的value值是列表或者元组，则调用_get_value


    return point_list

def _get_value(key, val, point_list):
    for val_ in val:
        if isinstance(val_, dict):
            get_target_value(key, val_, point_list)  # 传入数据的value值是字典，则调用get_target_value
        elif isinstance(val_, (list, tuple)):
            _get_value(key, val_, point_list)   # 传入数据的value值是列表或者元组，则调用自身

m=1
file_list = os.listdir(rootdir) #列出文件夹下所有的目录与文件
for i in range(0,len(file_list)):
    path = os.path.join(rootdir,file_list[i])
    if os.path.isfile(path):
        filename = rootdir + os.path.basename(path)
        print(os.path.basename(path))
    #filename = 'via_region_data.json'
    with open(filename, 'r+') as f:
        dic = simplejson.load(f)
    X = get_target_value('cx',dic,[])   # 得到X坐标
    Y = get_target_value('cy',dic,[])   # 得到Y坐标
    point = [100]*len(X)                # 赋予点源的值
    label_list = list(zip(point,X, Y))  # 标签列表
    with open('SKA{}.list'.format(m), 'w+') as f: # 保存成list文件
        for i in range(len(X)):
            s = str(label_list[i]).replace(',', '').replace('(', ' ').replace(')', ' ') + '\n'
            f.write(s)
    m+=1
