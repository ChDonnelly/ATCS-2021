names = ["John","Amy","Max",'Richard']

def crowd_test(names):
    if len(names) > 3:
        print("The room is crowded.")
    else:
        print("The room is not very crowded.")

crowd_test(names)

names.remove("Amy")

crowd_test(names)

