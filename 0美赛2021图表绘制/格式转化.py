with open("相关系数矩阵.txt",'r', encoding='utf-8') as data:
    for line in data:
        x=line.replace('\t', ',')
        print(x,end='')