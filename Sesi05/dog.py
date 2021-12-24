class Dog :
    #class attribute
    species = "Canis familiaris"

    def __init__(self, name, age) :
        self.name = name
        self.age = age
        #self.breed = breed
    
     # Instance method
    def description(self):
        return f"{self.name} is {self.age} years old"
    
    def __str__(self):
        return f"{self.name} is {self.age} years old"

    def __repr__(self):
        return f"to create instance :: Dog( name={self.name}, age={self.age}) #REPR"

    # Another instance method
    def speak(self, sound):
        return f"{self.name} says {sound}"

#child class
class JackRussellTerrier(Dog):
    def speak(self, sound="Arf"):
        return f"{self.name} says {sound}"

class Dachshund(Dog):
    pass

class Bulldog(Dog):
    def __init__(self, name, age, weight):
        super().__init__(name, age)
        self.weight = weight


# miles = Dog("Miles", 4, "Jack Russell Terrier")
# buddy = Dog("Buddy", 9, "Dachshund")
# jack = Dog("Jack", 3, "Bulldog")
# jim = Dog("Jim", 5, "Bulldog")


# print(buddy.name)
# print(miles.speak("Woof Woof"))
# print(buddy.speak("Yap"))
# print(jim.speak("Woof"))

miles = JackRussellTerrier("Miles", 4)
print(miles.speak())
buddy = Dachshund("Buddy", 9)
jack = Bulldog("Jack", 3, 10)
jim = Bulldog("Jim", 5, 10)

print(jack)
print("=================================")
print(repr(miles))
print(miles.__repr__())
 
print(str(miles))
print(miles.__str__())
