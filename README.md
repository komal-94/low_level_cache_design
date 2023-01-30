# LOW LEVEL CACHE DESIGN
I have implemented low level cache design in PYTHON.

There are three levels of code
1. For basic implementation check - *basic_low_level_cache_design.py*
2. For observer and decorator implementation check - *low_level_design_with_observer_and_decorator.py*
3. For observer, decorator and storage implementation check - *low_level_design_with_observer_and_decorator_and_storage.py*


### Design Patterns:

- **Factory Pattern:** To create objects without exposing the object creation logic to the client, a factory pattern will be used to create cache objects.
- **Decorator Pattern:** To extend the functionality of cache objects, a decorator pattern will be used.
- **Observer Pattern:** To notify cache objects about any changes, an observer pattern will be used.
### SOLID Principles:

- **Single Responsibility Principle:** The cache class will have a single responsibility, which is to cache the data.
- **Open/Closed Principle:** The cache class will be open for extension but closed for modification.
- **Liskov Substitution Principle:** The subclasses of the cache class will be interchangeable with their base class.
- **Interface Segregation Principle:** The cache class will be designed with multiple interfaces, to ensure that clients do not have to depend on methods they do not use.
 - **Dependency Inversion Principle:** The cache class will depend on abstractions, not on concrete implementations.

### Class Definitions:

- **Cache:** The main class that implements the cache functionality. It has two methods - get and put. The get method retrieves the data from the cache, and the put method adds data to the cache.
- **EvictionPolicy:** An abstract class that defines the eviction policy for the cache. The cache class will depend on this class to determine when to remove data from the cache.
- **LRUEvictionPolicy:** A concrete implementation of the eviction policy that implements the Least Recently Used (LRU) eviction policy.
- **CacheFactory:** A class that creates objects of the cache class.
- **Decorator:** A class that extends the functionality of the cache class.
- **Observer:** A class that is notified when data is added or removed from the cache.







The Decorator class is used to add new functionality to the Cache class without modifying its source code. This is useful if we want to add extra functionality to the cache, such as logging or monitoring, without changing the core code. The Decorator class implements the get and put methods of the Cache class and can be used to extend its behavior.

The Observer class is used to monitor changes to the cache. It allows objects to be notified of changes to the cache in real-time. This is useful if we want to implement a feature that requires us to be aware of changes to the cache, such as logging or performance monitoring. The Observer class defines a notify method that is called when the cache is updated. This method can be used to implement custom behavior in response to changes to the cache.










