## Animal is-a object
class Animal(object):
    pass

##is-a
class Dog(Animal):

    def __init__(self, name):
        ## is-a
        self.name = name
        print "Bark, bark!"

## is-a
class Cat(Animal):

    def __init__(self, name):
        ## is-a
        self.name = name
        print "Meow, meow!"

## is-a
class Person(object):

    def __init__(self, name, haircolour):
        ## is-a
        self.name = name
        self.haircolour = haircolour

        ## Person has-a pet of some kind
        self.pet = None

## is-a
class Employee(Person):

    def __init__(self, name, salary):
        ## has-a
        super(Employee, self).__init__(name)
        ## has-a
        self.salary = salary

## is-a
class Fish(object):

    def __init__(self, gills):
        self.gills = gills

## is-a
class Salmon(Fish):

    def __init__(self, gills, colour):
        super(Salmon, self).__init__(gills)
        self.colour = colour

myLittleSalmon = Salmon("big gills", "red")

print "I got a little salmon that has %s and a %s colour." % (myLittleSalmon)

## is-a
class Halibut(Fish):
    pass


# rover is-a Dogf
rover = Dog("Rover")
print rover

# satan is-a Cat
satan = Cat("Satan")
print satan

# mary is-a Person
mary = Person("Mary", "Blue")

## mary has-a pet
mary.pet = satan

# frank is-a Employee
frank = Employee("Frank", 120000)

## frank has-a pet
frank.pet = rover

## flipper is-a Fish
flipper = Fish()

## crouse is-a Salmon
crouse = Salmon()

## harry is-a Halibut
harry = Halibut()
