d = {0: "процентов", 1: 'процент', 2: 'процента',3: 'процента',4: 'процента', 5: "процентов", 6: "процентов", 7: "процентов", 8: "процентов", 9: "процентов"}
for i in range(1,11):
    print(i, d.get(i%10))
print('11 процентов')
print('12 процентов')
print('13 процентов')
print('14 процентов')
for i in range(15,101):
    print(i, d.get(i%10))