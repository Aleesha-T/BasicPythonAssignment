name = input("Enter your name")
for x in name:
    if x.lower() in ("a","e","i","o","u"):
        name = name.replace(x,"")

print(name)        