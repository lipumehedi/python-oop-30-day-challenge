def name_generator(names):
    for name in names:
       yield name

for name in name_generator(["Lipu", "Rahim", "Karim", "Hasan"]):
    print(name)