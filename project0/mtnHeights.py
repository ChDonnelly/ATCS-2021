tallestMountains = {"Everest":29029,"K2":28251,"Kangchenjunga":28169,"Lhotse":27940,"Makalu": 27838}

for key in tallestMountains.keys():
    print(key)
print("_______")
for value in tallestMountains.values():
    print(value)
print("_______")
for key, value in tallestMountains.items():
    print(key + " is " + str(value) + " feet tall")
