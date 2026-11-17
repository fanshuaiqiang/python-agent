from random import randint;


balance = randint(0, 100);

price = 50;

if balance >= price:
    print("购买成功")
else:
    print("余额不足")   

print("余额为：",balance);