scores = {"Alice": 85, "Bob": 90}
print("#1")
scores["Charlie"] = 78
print("#2")
scores["Bob"] = 95
print("#3")
print(scores.get("Dave"))
scores["Dave"] = 83
print(scores.get("Dave"))
scores.pop("Dave")
print("#4")
scores.pop("Alice")
print("#5")
print(scores, len(scores))
print(scores.keys(), scores.values())

