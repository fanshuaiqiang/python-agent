
import keyword;
from decimal import Decimal

'''
    多行注释
'''
"""
    多行注释
"""

# 单行注释

html = '''
    <div>
    <h1>hello world</h1>
    </div>
'''

print(html);

str1 = 'hello world111'
print(str1.encode('GBK'))

print(keyword.kwlist)


dec = 10;
print("二进制",bin(dec))
print("八进制",oct(dec))
print("十六进制",hex(dec))

# 数据类型
# 数值： int float complex bool
# 字符串： str
# 容器： 列表[] 元组 () 集合{} 字典{}
# 

num1 = 10
num2 = 3.14
print(type(num1))
print(type(num2))
print(num1 == num2)

list =  [1,2,3,4,5]
print(isinstance(False,int))

f1 = 0.1;
f2 = 0.2;
print(Decimal(str(f1)) + Decimal(str(f2)))


