# Three is a Crowd - Part 1
def crowd_test_1(lst):
    if len(lst) > 3:
        print("The room is crowded!")

names = ["Aaron", "Ben", "Charles", "Dave", "Eric", "Fred"]

crowd_test_1(names)

name = names[:2]

crowd_test_1(name)

# Three is a Crowd - Part 2
def crowd_test_2(lst):
    if len(lst) > 3:
        print("The room is crowded!")
    else:
        print("The room is not very crowded.")

crowd_test_2(names)

crowd_test_2(name)

# Six is a Mob
def crowd_test_3(lst):
    if len(lst) > 5:
        print("There's a mob in the room!")
    elif len(lst) > 2:
        print("The room is crowded!")
    elif len(lst) > 0:
        print("The room is not very crowded.")
    else:
        print("The room is empty.")

crowd_test_3(names)
crowd_test_3(name)
crowd_test_3(names[:4])
crowd_test_3([])