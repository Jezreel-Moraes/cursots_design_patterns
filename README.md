Creartional: How objects are created

Structural: How objects related to each other

Behavioral: How objects comunicate with each other

+------------+------------+------------+
| Creational | Structural | Behavioral |
+------------+------------+------------+
| Singleton  | Decorator  | Iterator   |
| Prototype  | Proxy      | Observer   |
| Builder    | Facade     | Mediator   |
| Factory    |            | States     |
+------------+------------+------------+

# Creational:

   ## Singleton:

	Create a single instance of an class. 
	(A singleton class shouldn’t have multiple instances in any case and at any cost).
	It must have global access.
	
   ## Prototype:

	Create an instance of an class, and save it in an "cache", so you can copy this instance
	as you wish *(warning with shallow copy or deep copy):
	It cost less then create a new instance of a class.

   ## Builder:

   An class with functions that return an instantiated object with some specific properties
   already defined, for any case... Is more easy to create some default objects, and create new
   objects with variated internal values... You can build a complex object like a lego...

   ## Factory:

   An class, function or module that create objects, and return them. Is like a builder, but the returned object 
   do not receive adicional properties or functions like builder where you can add more and more atributes to the object.

   (factory -> you receive the house done. builder -> You build the house pice by pice... )
	
   ## Abstract Factory:

   Is almost like a factory, but work with a family of objects. 
   Ex: You are creating a GUI app for 2 OS's (Windows and Linux), and you need to create a factory for each OS.
   A button for Windows work differently that a button for Linux and a window container is created differently in each one.
   You can not have a Windows button for a Linux window container. So, for each OS you need a factory that only
   create things for that OS. 
   
   WidowsFactory -> createWindowContainer() -> createButton() 
   LinuxFactory -> createWindowContainer() -> createButton() 

# Structural:

   ## Decorator:

   ## Facade:

	

   ## Proxy:

	

#Behavioral:

   # Iterator:

	

   # Observer:

	

   # Mediator:

	

   # States:
	
	