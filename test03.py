"""
input();
"""

name = input("请输入姓名：");
age = input("请输入年龄：");
print("姓名：",int(name) + int(age));
print("年龄：",age);

print("姓名：%s,年龄：%s" % (name,age), end = 'sss');