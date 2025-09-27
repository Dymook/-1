from collections import Counter


text ="""
    Python is a powerful programming language. 
    It is used in data science, web development, automation, and many other fields!
    PYTHON is easy to learn, yet very versatile.
"""
print("#1")
text.strip()
text = text.lower()
print(text)
print("#2")
text = text.replace("!", ".")
print(text)
print("#3")
tt = text.split(".")
tt.pop(-1)
for i in range(len(tt)):
    tt[i] = tt[i].replace("\n", "")
    tt[i] = tt[i].lstrip()
print(tt)
print("#7")
print(tt[0].startswith("python "), tt[0].endswith("language"))
print("#5")
tt[0] = tt[0].split(" ")
print(tt)
print("#6")
print(tt[0].count("python"))

print("#8")
c = 0
ca = 0
for i in range(len(tt[0])):
    c += len(tt[0][i])
    ca += tt[0][i].count("a")

c += len(tt[1])
c += len(tt[2])
ca += tt[1].count("a")
ca += tt[2].count("a")
print(c, ca, tt[1].find("data"))


print("#9")

tt[0] = "-".join(tt[0])
tt[1] = "-".join(tt[1].split())
tt[2] = "-".join(tt[2].split())
print(tt)

print("#10")
dd = Counter(text.split())
print(dd)
print("#11")
def clean_text(n):
    n.strip()
    n.rstrip()
    n.lstrip()
    zn = [",", ".", "!", "?", "...", "  "]
    for i in zn:
        while i in n:
            n = n.replace(i, "", 1)
    if n[0] == " ":
        n = n[1:]
    if n[-1] == " ":
        n = n[0:-1]
    return n

p = "   ghhhj sdkffhguhjk   fkigjfg lkg?"
print(clean_text(p))