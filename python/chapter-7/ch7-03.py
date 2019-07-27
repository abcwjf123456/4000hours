# 传递实参
def describe_pet(animal_type, pet_name):
    print("\nI have a" + animal_type + ".")
    print("my " + animal_type + "'s name is" + pet_name.title())


describe_pet('hamster', 'harry')

# 需要按照顺序传参
# I have ahamster.
# my hamster's name isHarry
