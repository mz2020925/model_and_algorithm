import xlrd



def data(dir_filename):
    xlsx = xlrd.open_workbook(dir_filename)
    sheet1 = xlsx.sheets()[0]  # 获得第1张sheet，索引从0开始
    sheet1_nrows = sheet1.nrows  # 获得行数
    # sheet1_name = sheet1.name  # 获得名称
    # sheet1_cols = sheet1.ncols  # 获得列数
    # print(sheet1_name)
    # print(sheet1_nrows)
    # print(sheet1_cols)
    list_current = []
    for row in range(5, sheet1_nrows):
        list_current.append((sheet1.row(row)[1].value, sheet1.row(row)[2].value))
    # print(list_current)
    return list_current


# print(data("2020112317152744775.xls"))
data_list = data("2020112317152744775.xls")
data_dict = dict(data_list)
data_dict1 = {}
for key, value in data_dict.items():
    data_dict1[key.strip()[:3]] = value
print(data_dict1)


animal_plant = data_dict1['第1类'] + data_dict1['第2类']

food = data_dict1['第3类'] + data_dict1['第4类']

hemical_products =data_dict1['第 5'] + data_dict1['第6类'] + \
                  data_dict1['第7类'] + data_dict1['第13']

clothes = data_dict1['第8类'] +data_dict1['第9类'] +\
          data_dict1['第10'] +data_dict1['第11'] +\
          data_dict1['第12']

metal = data_dict1['第14'] + data_dict1['第15']

technology_machine = data_dict1['第16'] + data_dict1['第17'] +\
                     data_dict1['第18'] + data_dict1['第19']

others = data_dict1['第20'] + data_dict1['第21'] +\
         data_dict1['第22']


class_total = []
class_total.append(animal_plant)
# print(animal_plant)
class_total.append(food)
class_total.append(hemical_products)
class_total.append(clothes)
class_total.append(metal)
class_total.append(technology_machine)
class_total.append(others)

print(class_total)
print(sum(class_total))
total = sum(class_total)
print([i / total*100 for i in class_total])