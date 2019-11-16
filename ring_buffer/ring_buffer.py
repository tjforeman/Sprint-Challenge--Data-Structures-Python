class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity

  def append(self, item):
    
    self.storage[self.current] = item

    if self.current is None:
      return None 

    if self.capacity > self.current:
      self.current += 1

    if self.current >= self.capacity:
      self.current = 0


  def get(self):

    if self.storage[self.current] is not None:
      return self.storage

    else:
      return self.storage[:self.current]

    
    # return self.storage