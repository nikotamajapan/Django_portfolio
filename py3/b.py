money = int(input('money - '))

maisu = money // 10000
money = money % 10000
print('10000 - ' , maisu)

maisu = money // 5000
money = money % 5000
print('5000 - ' , maisu)

maisu = money // 1000
money = money % 1000
print('1000 - ' , maisu)

maisu = money // 500
money = money % 500
print('500 - ' , maisu)

maisu = money // 100
money = money % 100
print('100 - ' , maisu)

maisu = money // 50
money = money % 50
print('50 - ' , maisu)

maisu = money // 10
money = money % 10
print('10 - ' , maisu)

maisu = money // 5
money = money % 5
print('5 - ' , maisu)

maisu = money // 1
money = money % 1
print('1 - ', maisu)