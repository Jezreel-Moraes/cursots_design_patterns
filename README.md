Creational: How objects are created

Structural: How objects related to each other

Behavioral: How objects communicate with each other

+------------+------------+------------+
| Creational | Structural | Behavioral |
+------------+------------+------------+
| Singleton  | Composite  | Strategy   |
| Prototype  | Adapter    | Command    |
| Builder    | Bridge     | Memento    |
| Factory    | Decorator  |            |
| A. Factory | Facade     |            |
|            | Proxy      |            |
|            | Flyweight  |            |
+------------+------------+------------+

# Creational:

   ## Singleton:

	Create a single instance of an class. 
	(A singleton class shouldn’t have multiple instances in any case and at any cost). It must have global access.
	
   ## Prototype:

	Create an instance of an class, and save it in an "cache", so you can copy this instance as you wish *(warning with shallow copy or deep copy): It cost less then create a new instance of a class.

   ## Builder:

   An class with functions that return an instantiated object with some specific properties already defined, for any case. Is more easy to create some default objects, and create new objects with variated internal values. You can build a complex object like a lego.

   ## Factory:

   An class, function or module that create objects, and return them. Is like a builder, but the returned object do not receive adicional properties or functions like builder where you can add more and more atributes to the object.

   **Ex:**
   
   Factory: you receive the house done.
   Builder: You build the house pice by pice.
	
   ## Abstract Factory:

   Is almost like a factory, but work with a family of objects.
   Ex: You are creating a GUI app for 2 OS's (Windows and Linux), and you need to create a factory for each OS. A button for Windows work differently that a button for Linux and a window container is created differently in each one.
   You can not have a Windows button for a Linux window container. So, for each OS you need a factory that only create things for that OS. 
   
   **Ex:**

   WidowsFactory: createWindowContainer() -> createButton() 
   LinuxFactory: createWindowContainer() -> createButton() 

# Structural:

   ## Composite:

   A class that contain other classes with the same properties and methods. A structure that behave yourself like a single object, delegating methods calls
   to its children. 
   
   **Ex:**

   (Component -> getPrice(): calls -> Leaf -> getPrice())

   ## Adapter:

   A class that adapts dependencies to a new own system interface. Separate the client code of that dependencies.

   **Ex:**

   clientCode -> Adapter.getUSDPrice() -> Adapter -> Dependence.getUSDPrice()

   ## Decorator:

   Add new functionality to an object without changing its structure.
   
   **Ex:**

   shirt -> printedShirt(shirt) -> shirt with a print on the shirt. extend the object without changing it.

   ## Facade:

	A class that provides an interface to a subsystem. This is a way to decrease the complexity of the code, simplifying it in to methods in a class.

   ## Proxy:

   Try substitute an object. It calls the original object methods only when it is necessary. Can be used in different cases, in different ways

   ## Flyweight:

   Us a design pattern that is intended to use sharing to efficiently support large numbers of objects in a granular way.

   **Ex:**

   Object:
   - Share the intrinsic part (that never changes) to all objects.
   - Create the extrinsic part (that changes for each object) for each new object.
   - Join the two parts to create the object, or use the two parts in a function that know how use them.

# Behavioral:

   ## Strategy:

   A class that defines an interface for a family of algorithms, encapsulates each one, and make them interchangeable. The strategy pattern is used to solve the problem of having multiple implementations of the same algorithm in a program. It allows the algorithm to vary independently from clients that use it.

   ## Command:

   A class that encapsulates a request as an object, thereby letting you parameterize clients with different requests, queue or log requests. It allows clients to pass requests to a request queue, and allows you to undo operations on the request queue.

   ## Memento:

   A class that provides a way to save and restore the state of an object without breaking the encapsulation of its implementation. It is used to save the state of the object to restore it when it is necessary. 