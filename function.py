#!-coding:utf-8-

def describe_pet(animal_type,pet_name):
    """显示宠物的信息"""
    print("\nI have a " + animal_type.title() + ".")
    print("My" + animal_type + "'s name is " + pet_name.title()+".")

describe_pet(animal_type='hamster',pet_name='harrt')

def make_shirt(size="L",word='I Love Python'):
    print(size.strip()+" T-shirt "+word.title())

make_shirt('s')
make_shirt("M",'python')

def get_formatted_name(first_name,last_name,middle_name=''):
    """返回姓名"""
    if middle_name:
        full_name=first_name+' '+middle_name+' '+last_name
    else:
        full_name=first_name+' '+last_name+' '
    return full_name
name=get_formatted_name('Motion','Re','-')
print(name)

def build_person(first_name,last_name,age=''):
    person={'first':first_name,'last':last_name}
    if age:
        person['age']=age
    return person
musician=build_person('jimi','hendirix',age=27)
print(musician)

unprinted_designs=['iphone case','robot pendant','dodecahedron']
completed_models=[]
while unprinted_designs:
    current_design=unprinted_designs.pop()
    print("Printing mode:"+current_design)
    completed_models.append(current_design)
print("\nThe following models have been printed:")
for completed_models in completed_models:
    print(completed_models)


