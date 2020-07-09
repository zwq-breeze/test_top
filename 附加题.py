
def compare_version(v1, v2):
    """
    比较两个版本号
    :param v1:
    :param v2:
    :return: v1>v2 返回1，v1<v2 返回-1，否则返回0
    """
    v1_li = v1.split('.')
    v2_li = v2.split('.')
    len_v1 =len(v1_li)
    len_v2 =len(v2_li)
    if len_v1 > len_v2:
        for i in range(len_v1-len_v2):
            v2_li.append("0")
    if len_v1 < len_v2:
        for i in range(len_v2-len_v1):
            v1_li.append("0")

    for index in range(len(v1_li)):
        if int(v1_li[index]) == int(v2_li[index]):
            continue
        if int(v1_li[index]) > int(v2_li[index]):
            return 1
        if int(v1_li[index]) < int(v2_li[index]):
            return -1
    return 0


if __name__ == '__main__':
    res = compare_version('0.1', '1.1')
    res1 = compare_version('1.0.1', '1')
    res2 = compare_version('7.5.2.4', '7.5.3')
    res3 = compare_version('1.01', '1.001')
    res4 = compare_version('1.0', '1.0.0')
    res5 = compare_version('1.010', '1.009')
    res6 = compare_version('1.01', '1.009')
    res7 = compare_version('1', '2')
    print(res)
    print(res1)
    print(res2)
    print(res3)
    print(res4)
    print(res5)
    print(res6)
    print(res7)