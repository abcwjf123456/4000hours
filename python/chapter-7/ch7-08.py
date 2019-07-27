# 返回字典
def build_person(first_name, last_name, age=''):
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person


musician = build_person('hh', 'jjj', 9)
print(musician)

# {'first': 'hh', 'last': 'jjj', 'age': 9}
