class Person:  #for class we capitalize every word. in case multiple words EmailClient (pascal naming convention).
   def __init__(self, name):
      self.name=name
   def talk(self):          #creating class with the name "Point"
      print(f"Hi, I am {self.name}")

John = Person("John Smith")
John.talk()

bob = Person("Bob Smith")

bob.talk()
