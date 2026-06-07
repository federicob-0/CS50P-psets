class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self.size = 0

    def __str__(self):
        return "🍪" * self.size

    def deposit(self, n):
        if not n and n != 0:
            raise ValueError("Missing deposit amount")
        elif not isinstance(n, int):
            raise ValueError("Deposit amount must be an int")
        elif n < 0:
            raise ValueError("Deposit amount must be a non-negative int")
        elif (self.size + n) > self.capacity:
            raise ValueError("Too many deposited, jar capacity exceeded")
        self.size += n

    def withdraw(self, n):
        if not n and n != 0:
            raise ValueError("Missing withdraw amount")
        elif not isinstance(n, int):
            raise ValueError("Withdraw amount must be an int")
        elif n < 0:
            raise ValueError("Withdraw amount must be a non-negative int")
        elif n > self.size:
            raise ValueError("Too many removed, jar size was smaller")
        self.size -= n

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        if not capacity and capacity != 0:
            raise ValueError("Missing jar capacity")
        elif not isinstance(capacity, int):
            raise ValueError("Jar capacity must be an int")
        elif capacity < 0:
            raise ValueError("Jar capacity must be a non-negative int")
        self._capacity = capacity
        return self._capacity

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, n):
        if not n and n != 0:
            raise ValueError("Missing size value")
        elif not isinstance(n, int):
            raise ValueError("Size value must be an int")
        elif n < 0:
            raise ValueError("Size value must be a non-negative int")
        self._size = n
        return self._size
