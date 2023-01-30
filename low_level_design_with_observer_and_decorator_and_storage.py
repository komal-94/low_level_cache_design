import abc


class Cache:
    """
    Cache: The main class that implements the cache functionality. It has two methods - get and put.
    The get method retrieves the data from the cache, and the put method adds data to the cache.
    """
    def __init__(self, eviction_policy):
        self.data = {}
        self.eviction_policy = eviction_policy
        self.observers = []

    def put(self, key, value):
        self.data[key] = value
        self.eviction_policy.notify_put(key)

        for observer in self.observers:
            observer.notify(key)

    def get(self, key):
        val = self.data.get(key)

        if val:
            self.eviction_policy.notify_get(key)

        return val

    def add_observer(self, observer):
        self.observers.append(observer)


class Storage:
    def __init__(self):
        pass

    def append(self, key):
        pass

    def remove(self, key):
        pass

    def pop(self, index):
        pass

    def __len__(self):
        pass


class ListStorage(Storage):
    def __init__(self):
        self.data = []

    def append(self, key):
        self.data.append(key)

    def remove(self, key):
        self.data.remove(key)

    def pop(self, index):
        return self.data.pop(index)

    def __len__(self):
        return len(self.data)


class EvictionPolicy(abc.ABC):
    """
    EvictionPolicy: An abstract class that defines the eviction policy for the cache.
    The cache class will depend on this class to determine when to remove data from the cache.
    """
    def __init__(self, cache):
        self.cache = cache

    @abc.abstractmethod
    def notify_get(self, key):
        pass

    @abc.abstractmethod
    def notify_put(self, key):
        pass

    @abc.abstractmethod
    def evict(self):
        pass


class LRUEvictionPolicy(EvictionPolicy):
    """
    LRUEvictionPolicy: A concrete implementation of the eviction policy that implements
     the Least Recently Used (LRU) eviction policy.
    """
    def __init__(self, cache, size, storage):
        super().__init__(cache)
        self.size = size
        self.storage = storage

    def notify_get(self, key):
        self.storage.remove(key)
        self.storage.append(key)

    def notify_put(self, key):
        if len(self.storage) >= self.size:
            self.evict()

        self.storage.append(key)

    def evict(self):
        key = self.storage.pop(0)
        self.cache.data.pop(key)


class CacheFactory:
    """
    CacheFactory: A class that creates objects of the cache class.
    """
    @staticmethod
    def create_cache(eviction_policy):
        return Cache(eviction_policy)


class Decorator:
    """
    Decorator: A class that extends the functionality of the cache class.
    """
    def __init__(self, cache):
        self.cache = cache

    def put(self, key, value):
        self.cache.put(key, value)

    def get(self, key):
        self.cache.get(key)


class LoggingDecorator(Decorator):
    def put(self, key, value):
        print(f"Puting key:{key} value:{value}")
        self.cache.put(key, value)


class Observer:
    """
    Observer: A class that is notified when data is added or removed from the cache.
    """
    def __init__(self, cache):
        self.cache = cache

    def notify(self, key):
        pass


class LoggingObserver(Observer):
    def notify(self, key):
        print(f"Cache changed:{key}")


# Note: This is just an example
if __name__ == '__main__':
    print("Low level cache design implementation with observer, decorator and storage class:")
    eviction_policy = LRUEvictionPolicy(None, 3, ListStorage())
    cache = CacheFactory.create_cache(eviction_policy)
    eviction_policy.cache = cache

    logging_decorator = LoggingDecorator(cache)
    logging_observer = LoggingObserver(cache)
    cache.add_observer(logging_observer)
    logging_decorator.put("A", 1)
    logging_decorator.put("B", 2)
    logging_decorator.put("C", 3)
    logging_decorator.put("D", 4)

# Output:
# Low level cache design implementation with observer, decorator and storage class:
# Puting key:A value:1
# Cache changed:A
# Puting key:B value:2
# Cache changed:B
# Puting key:C value:3
# Cache changed:C
# Puting key:D value:4
# Cache changed:D
