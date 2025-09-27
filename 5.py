val = [3, 1, 3, 2, 1, 5, 2]
un_val = set(val)
print(un_val)
print(len(un_val))
# я убедился, что python не сломался на этом моменте
oth = {2, 4, 5}
print(un_val & oth)
print(un_val | oth)
print(oth - un_val)
