from collections import deque

class LRU:
    def __init__(self,capacity ):
        self.max_capacity = capacity
        self.current_capacity = 0
        self.lru_deque = deque()

    def get(self, key):
        #Find it in the deque (N)
        for each_key, each_val in self.lru_deque:
            if each_key == key:
                self.lru_deque.remove(each_key,each_val)
                self.lru_deque.appendleft((each_key,each_val))
                return each_val

    def set(self, key, val):
        current_key, current_val = self.key_in_deque(key):
        if current_key:
            self.lru_deque.remove((current_key, current_val))
            self.lru_deque.appendleft((current_key, val))
        else:
            self.appendleft((key,val))
