class Parent:
  def greet(self):
    print("hello from parent")

class Child(Parent):
  def hello(self):
    print("Hello from child")


obj = Child()
obj.greet()
obj.hello()