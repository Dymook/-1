f = " Hello, Python! "
f1 = f.strip()
f2 = f1.replace("!", "?")
f3 = f2.upper()
print(f1, f2, f3)
f4 = f3.lower()
print(f4)
if f4 == "hello, python?":
    print("yes")