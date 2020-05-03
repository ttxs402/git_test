#%% 0、dog.py
class Dog():
    """一次模拟小狗的简单尝试"""
    def __init__(self,name,age):
        """初始化属性name和age"""
        self.name = name
        self.age = age

    def sit(self):
        """模拟小狗被命令时蹲下"""
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        """模拟小狗被命令时打滚"""
        print(self.name.title() + " rolled over!")


# %% 1、根据类创建实例
my_dog = Dog(name = 'willie',age = 6)
print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")

# %% 2、调用方法
my_dog.sit()
my_dog.roll_over()

# %% 3、创建多个实例
my_dog = Dog('willie',6)
your_dog = Dog('lucy',3)

print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")
my_dog.sit()

print("\nYour dog's name is " + your_dog.name.title() + ".")
print("Your dog is " + str(your_dog.age) + " years old.")
your_dog.sit()

#9.2 使用类和实例
# %% 0、car.py
class Car():
    """一次模拟汽车的简单尝试"""

    def __init__(self,make,model,year):
        """初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year

    def get_descriptive_name(self):
        """返回整洁的描述信息"""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()


# %% 1、创建实例
my_new_car = Car('audi','a4','2016')
print(my_new_car.get_descriptive_name())


# %% 2、给属性指定默认值
class Car():
    """一次模拟汽车的简单尝试"""

    def __init__(self,make,model,year):
        """初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0 #添加新属性，默认值为0

    def get_descriptive_name(self):
        """返回整洁的描述信息"""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):#添加新方法
        """打印一条指出汽车里程的消息"""
        print("This car has " + str(self.odometer_reading) + " miles on it.")


my_new_car = Car('audi','a4','2016')
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()
# %% 3、修改属性
my_new_car.odometer_reading = 23
my_new_car.read_odometer()

# %% 3.1、通过方法修改属性的值
class Car():
    """一次模拟汽车的简单尝试"""

    def __init__(self,make,model,year):
        """初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0 #添加新属性，默认值为0

    def get_descriptive_name(self):
        """返回整洁的描述信息"""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):#添加新方法
        """打印一条指出汽车里程的消息"""
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self,mileage):
        """将里程表读数设置为指定的值"""
        self.odometer_reading = mileage

my_new_car = Car('audi','a4','2016')
my_new_car.update_odometer(25)
my_new_car.read_odometer()

# %%
class Car():
    """一次模拟汽车的简单尝试"""

    def __init__(self,make,model,year):
        """初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 10 #添加新属性，默认值为0

    def get_descriptive_name(self):
        """返回整洁的描述信息"""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):#添加新方法
        """打印一条指出汽车里程的消息"""
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self,mileage):
        """
        将里程表读数设置为指定的值
        禁止将里程表读数往回调
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    def increment_odometer(self,miles):
        """将里程表读数增加指定的量"""
        self.odometer_reading+=miles

        
my_new_car = Car('audi','a4','2016')
my_new_car.update_odometer(25)
my_new_car.read_odometer()


# %%
my_used_car = Car('subaru','outback',2013)
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23500)
my_used_car.read_odometer()

my_used_car.increment_odometer(1000)
my_used_car.read_odometer()
#%%
#类的继承#
#%% 1、电动车
class ElectricCar(Car):
    """电动汽车的独特之处"""

    def __init__(self,make,model,year):
        """首先初始化父类属性"""
        super().__init__(make,model,year)


my_tesla = ElectricCar('tesla','model_s',2016)
print(my_tesla.get_descriptive_name())

# %% 2、给子类定义属性和方法
class ElectricCar(Car):
    """电动汽车的独特之处"""

    def __init__(self,make,model,year):
        """
        首先初始化父类属性
        在初始化电动汽车特有的属性
        """
        super().__init__(make,model,year)
        self.battery_size = 70

    def describe_battery(self):
        """打印一条描述电瓶容量的消息"""
        print("This car has a " + str(self.battery_size) + "-kwh battery.")


my_tesla = ElectricCar('tesla','model_s',2016)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()

# %% 3、将实例用作属性
class Battery():
    """一次模拟电动汽车的简单尝试"""

    def __init__(self,battery_size = 70):
        """初始化电池属性"""
        self.battery_size = battery_size
    
    def describe_battery(self):
        """打印一条描述电瓶容量的消息"""
        print("This car has a " + str(self.battery_size) + "-kwh battery.")
    def get_range(self):
        """打印一条消息，指出电瓶的续航里程"""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)

class ElectricCar(Car):
    """电动汽车的独特之处"""

    def __init__(self,make,model,year):
        """
        首先初始化父类属性
        在初始化电动汽车特有的属性
        """
        super().__init__(make,model,year)
        self.battery = Battery()
        
my_tesla = ElectricCar('tesla','model_s',2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
# %%
a = list(range(10))
print(a)
b = []
for i in a:
    b.append(i)
print(b)

# %%

#%%
