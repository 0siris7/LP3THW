#Aninal is-a object
class Animal(object):
    pass

#Dog is-a Animal
class Dog(Animal):
    def __init__(self, name):
        ## Dog has-a name
        self.name = name

##Cat is-a animal
class Cat(Animal):

    def __init__(self, name):
        ##Cat has-a name
        self.name = name

## Person is-a object
class Person(object):

    def __init__(self, name):
        ## Person has-a name
        self.name = name

        ## Person has-a pet of some kind
        self.pet = None

##Employee is a Person

class Employee(Person):
    def __init__(self, name, salary):
        ##??
        super(Employee, self).__init__(name)
        ## salary is-a salary
        self.salary = salary

##Fish is-a objext
class Fish(object):
    pass

# Salmon is-a Fish
class Salmon(Fish):
    pass

## Halibut is-a fish
class Halibut(Fish):
    pass

## rover is-a dog
rover = Dog("Rover")

## Cat is-a Satan
satan = Cat("Satan")

##Mary is-a person
Mary = Person("Mary")

## Mary has-a pet Satan
Mary.pet = satan

##frank is-a employee
frank = Employee("Frank", 120000)

## frank has-a pet rover
frank.pet = rover

##Flipper is-a fish
flipper = Fish()

## crouse is a Salmon
crouse = Salmon()


##Hary is-a Halibut
harry = Halibut()
