import abc


class Cache:
    """
    Cache: The main class that implements the cache functionality. It has two methods - get and put.
    The get method retrieves the data from the cache, and the put method adds data to the cache.
    """
    def __init__(self, eviction_policy):
        self.data = {}
        self.eviction_policy = eviction_policy

    def put(self, key, value):
        self.data[key] = value
        self.eviction_policy.notify_put(key)

    def get(self, key):
        val = self.data.get(key)

        if val:
            self.eviction_policy.notify_get(key)

        return val


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
    def __init__(self, cache, size):
        super().__init__(cache)
        self.size = size
        self.queue = []

    def notify_get(self, key):
        self.queue.remove(key)
        self.queue.append(key)

    def notify_put(self, key):
        if len(self.queue) >= self.size:
            self.evict()

        self.queue.append(key)

    def evict(self):
        key = self.queue.pop(0)
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


class Observer:
    """
    Observer: A class that is notified when data is added or removed from the cache.
    """
    def __init__(self, cache):
        self.cache = cache

    def notify(self, key):
        pass


# Note: This is just an example
if __name__ == '__main__':
    print("Low level cache design implementation")
    eviction_policy = LRUEvictionPolicy(None, 3)
    cache = CacheFactory.create_cache(eviction_policy)
    eviction_policy.cache = cache

    cache.put("A", 1)
    cache.put("B", 2)
    cache.put("C", 3)
    print(cache.get("A")) # 1
    cache.put("D", 4)
    print(cache.get("B")) # None
