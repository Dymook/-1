cor = (1, 2, 3)
try:
    cor[1] = 100
except:
    print("невозможно")
# нельзя изменить кортеж
cor2 = cor + (4, 5)
print(cor2)
print(cor2.count(3))
print(cor2.index(4))
