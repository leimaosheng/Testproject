#!-coding:utf-8-

# class Dog():
#
#     def __init__(self,name,age):
#         """初始化属性name和age"""
#         self.name=name
#         self.age=age
#     def site(self):
#         """模拟小狗被命令时蹲下"""
#         print(self.name.title()+" is now sitting.")
#     def roll_over(self):
#         """模拟小狗被命令时打滚"""
#         print(self.name.title()+" is rolled over!")
#
# my_dog=Dog('willie',6)
#
# print("My dog's name is " + my_dog.name.title()+'.')
# print("My dog is "+ str(my_dog.age)+" yeas old.")
#
# my_dog.roll_over()
# my_dog.site()

class Car():
    def __init__(self,make,model,year):
        """初始化汽车的描述信息"""
        self.make=make
        self.moduel=model
        self.year=year
        self.odometer_reading=0
    def get_descriptive_name(self):
        """返回整洁的描述性信息"""
        long_name=str(self.year)+" "+self.make+" "+self.moduel
        return long_name.title()
    def read_odometer(self):
        """打印一条支出汽车里程的消息"""
        print("This car has "+str(self.odometer_reading)+" miles on it.")
    def update_odometer(self,mileage):
        """修改里程表"""
        if mileage >= self.odometer_reading:
            self.odometer_reading=mileage
        else:
            print("You can't roll back an odometer")
    def increment_odometer(self,miles):
        """将里程表读书增加制定的量"""
        self.odometer_reading+=miles
    def fill_gas_tank(self):
        print("This has ten gas")

# my_new_car=Car('audi','a4',2016)
# print(my_new_car.get_descriptive_name())
# my_new_car.read_odometer()
# my_used_car=Car("subaru","outback",2013)
# print(my_used_car.get_descriptive_name())
# my_used_car.update_odometer(23000)
# my_used_car.read_odometer()
# my_used_car.increment_odometer(23)
# my_used_car.read_odometer()
class Battary():
    def __init__(self,battary_size=70):
        self.battary_size=battary_size
    def describe_battary(self):
        print("This cat has a "+str(self.battary_size)+"-kWh battary.")
    def get_range(self):
        if self.battary_size==70:
            range=240
        elif self.battary_size==85:
            range=270
        message="This car can go approximately "+str(range)
        message+=" miles on a full charge."
        print(message)



class ElectricCar(Car):
    def __init__(self,make,model,year):
        """初始化父类的属性"""
        # super().__init__(make,model,year)
        super(ElectricCar,self).__init__(make,model,year)
        # self.battary_size=70
        self.battary=Battary()

    # def describe_battary(self):
    #     print("This cat has a "+str(self.battary_size)+"-kWh battery.")

    def fill_gas_tank(self):
        print("This cat doesn't need a gas tank")

my_tesla=ElectricCar('tesla','model S',2016)
print(my_tesla.get_descriptive_name())
my_tesla.battary.describe_battary()
my_tesla.fill_gas_tank()
my_tesla.battary.get_range()