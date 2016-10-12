A large computer system is very different from a small system in the sense that the way the whole system is designed and implemented gains a lot of say in the maintainability cost and the flexibility of the system to change. There are some common problems in a large and complex environment. Attacking these problems, design patterns were proposed in the `Gang of Four book`_. In software engineering, a design pattern is a generally accepted solution to a common problem in a specific solution. They are mainly ideas that must be implemented according to the context and based on the specific language that they are being implemented. Here in this post I will discuss some general and more common design patterns and the context in which we should look forward to implementing them.

Below are some common patterns that can be used and the context in which that they can be implemented. I have tried to given a simple exxplanation of the patterns along with a use cases where these can be implemented so that you are able to grasp some of the context in which these can be used. I have also tried to provide some common pitfalls or risks that the developer should be aware of while implementing the pattern. Of course the actual implementation of the specific pattern depends on the context of the application code and how well this is implemented. You should not look forward to implementing a pattern just because you think that you know about it. If implemented carelessly, one part of the code can have adverse effects on other parts of the system.

The GOF proposed three kinds of patterns:
<ol>
	<li>Creational patterns: These patterns isolate the object creation part from the actual implementation.</li>
	<li>Structural patterns: These deal with the architecture of the whole program and are concerned with how objects and classes can be combined to form larger structures.</li>
	<li>Behavioural patterns: They are concerned more with the interaction between objects and the way an object behaves.</li>
</ol>
Singleton pattern

This is a creation pattern and is thought of as a more elegant design to the global variable. The philosophy is that we will have one and only one object of a given type. Use cases are logging, database operations, print requests to the printer, where there is a need to have only one instance across the application to avoid conflicting requests to the same resource.

Singletons can have adverse effects in that a variable might get changed in one class without the knowledge of the developer with the inadvertent introduction of a bug. Or classes might get instantiated which are resource intensive without the actual usage of those classes.

Factory pattern

This is another creation pattern where there exists a class that is responsible for creating objects of required types. It will enable loose coupling between the object creation and the implementation part. There are at-least two kinds of Factory patterns: Factory Method and the Abstract Factory method. Use cases can be designing a GUI where a factory object is created appropriate to the GUI that needs to be worked on like a new button or a new menu. Thus use this method when you observe that new types of objects need to be added to the system. Of course this is an overkill if there are only one or two types of objects in the system and would only make the application code harder to read and understand as there would be more layers of abstraction.

Façade pattern

This is a structural pattern. Use this pattern when you need to abstract away the complexities of the underlying system and need to provide and clear and simple interface to the client. The underlying classes should not be aware of the facade layer. Use cases can be providing a single api to get all the computer information at one go as is shown in the present `wikipedia link`_.

The facade is not a method to shield the underlying system and the client can dig into the underlying system if it so wishes. So please use the facade if it makes the use of the system less complicated to the client by various orders of magnitude since for a simple system this will just be an additional class and will add unnecessary complexity to the system.

Proxy pattern

This is used when we need an intermediary between the system and the client. Objective maybe to provide security or to provide a local client to the remote machine. Use cases are swing icons for a picture library or maybe an public facing api protecting the underlying system

Observer pattern

This is a behavioral pattern and here the Subject keeps a list of Observers which are notified if there is any change in the state of the Subject.

This is required when there is a distributed service and the functionality of the different services is dependent on the state of a core service. Use cases can be that of the android play-store where if any app version is upgraded all the phones are notified that an updated version of the app is available and they can chose to upgrade the app if they so wish. Another use case is the stock market.

This pattern should be implemented with care as if the architecture is not sound then this can result in race conditions or add unnecessary complexity.

Command pattern

This is another behavioral pattern where the idea is to encapsulate or record all the choices needed to perform the desired function before hand and then the actual application is launched with the required choices. A good use case is the installation wizard which stores all the choices of the user and then the actual installation happens. In this pattern the program should have all the possible combinations and at run time a specific combination would be implemented based on the context. The Command instance will be instantiated by Client but the implementation will be done by an Invoker, and the invoker and the client will know nothing about each other.

Closures are a way of implementing the command pattern and in cases where the language has support for that should be used in that manner.

Template Method pattern

The template method is a behavioural pattern and this is used when we need to implement different algorithms and classes into similar or identical logic. Multiple algorithms can be defined by letting the subclasses implement the behaviour through overriding. A use case can be a cross platform application where the whole behaviour can be implemented through the template pattern and OS - specific actions are delegated to the subclass for the concerned OS. Or when refactoring is performed and a common behaviour is identified between the classes, then an abstract base class containing all the common code(in the template method) should be created to avoid code duplication.

The template pattern is also referred to as the Hollywood principle in the sense that its the high level abstract class has the steps for the algorithm. Depending on the algorithm, low level classes are called to define the concrete steps in the implementation of the program.

When this pattern is being implemented, documentation and strict error handling should be done else debugging and understanding the flow of the program might get too complicated. Changes in any layer of the code can disturb the implementation. Hence maintenance will become very tough.

MVC

MVC is a compound pattern. The most common example where this is used is the case of a website.

This pattern might be an overkill when designing quick single page applications or for landing pages.

State Design pattern

This is a behavioural pattern in that this is used to allow an object to change its internal behaviour as the state changes. An use case maybe the vending machine where the serving depends on the amount of cash deposited and the items that are present in its inventory. Or maybe a TV remote where the next channel behaviour depends on the present channel that the TV is on right now. Another use case is implementing network protocols where we can have a finite number of use cases.

This pattern is used to implement the Finite State Machines.

Code for all the patterns listed here and many more can be found in the GitHub link `here`_. Please contribute to it or if a better implementation is found please update the libraries and examples.
<p style="font-size: 12px;">References and Further Readings:</p>

<ul style="font-size: 12px;">
	<li>http://gameprogrammingpatterns.com/state.html</li>
	<li>http://legacy.python.org/workshops/1997-10/proceedings/savikko.html</li>
	<li>http://www.aleax.it/gdd_pydp.pdf</li>
	<li>https://github.com/victorlin/design-patterns/tree/master/tests</li>
	<li>https://github.com/faif/python-patterns</li>
	<li>http://www.oodesign.com/template-method-pattern.html</li>
</ul>

.. _Gang of Four book: http://www.amazon.in/Design-Patterns-Elements-Reusable-Oriented/dp/8131700070/ref=sr_1_1?ie=UTF8&amp;qid=1460127461&amp;sr=8-1&amp;keywords=gang+of+four
.. _wikipedia link: https://en.wikipedia.org/wiki/Facade_pattern#Java
.. _here: https://github.com/faif/python-patterns
