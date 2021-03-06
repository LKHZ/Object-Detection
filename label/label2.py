import simplejson

m=1  #保存文件的序列

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



with open('via_region_data (16).json', 'r+') as f:
        dic = simplejson.load(f)                      #将json文件变为字典

key_dict = list(dic.keys())

for i in range(len(key_dict)):
    print(key_dict[i])
    print(dic[(key_dict[i])])
    X = get_target_value('cx', dic[(key_dict[i])], [])  # 得到X坐标
    Y = get_target_value('cy', dic[(key_dict[i])], [])  # 得到Y坐标

    for j in range(len(Y)):     #y轴翻转，因此需要减去y轴的大小
        Y[j] = abs(Y[j] - 600)

    point = [100] * len(X)  # 标签类型，点源，则为100
    label_list = list(zip(point, X, Y))  # 合并标签列表
    with open(r"D:/A_Postgraduate/SKA_seg/segment600_600/adbin_data_denoise/" + '/' + 'aaa{}.list'.format(m), 'w+') as f:  # 保存成list文件
        for i in range(len(X)):
            s = str(label_list[i]).replace(',', '').replace('(', '').replace(')', '') + '\n'
            f.write(s)
    m += 1
