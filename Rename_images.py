import os
# 1.找到所有文件：获取code文件夹的目录 -- listdir()
os.chdir('D:\ArticleSoftware\MatlabR2020a\\bin\代码库\matlab公选课\class4_3D画图_图像处理')
file_name = os.listdir()
print(file_name)

# 2.构造新名字并重命名 -- 添加前缀

for i in file_name:
    if i.endswith('.m'):
        if 'Four_class' or 'four_class' in i:
            new_name = 'eg'+i[10:]
            os.rename(i, new_name)
# 删除前缀 -- 关键在于新名字的构造，即就是字符串的切片功能
# elif fldg == 2:
#     for i in file_name:
#         num = len('python_')
#         new_name = i[num:]
#         os.rename(i, new_name)
