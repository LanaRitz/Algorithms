class LinearProbingHashTable:
    def __init__(self, size, initial_data=None):
        self.size = size
        self.table = [None] * size
        self.keys = [None] * size
        if initial_data:
            self.initialize_with_values(initial_data)

    def initialize_with_values(self, data):
        for key, value in data:
            self.insert(key, value)

    def hash_function(self, key):
        return key % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        for i in range(self.size):
            probe_index = (index + i) % self.size
            if self.keys[probe_index] is None or self.keys[probe_index] == key:
                self.table[probe_index] = value
                self.keys[probe_index] = key
                return
        raise Exception("Hash table is full!")

    def lookup(self, key):
        index = self.hash_function(key)
        for i in range(self.size):
            probe_index = (index + i) % self.size
            if self.keys[probe_index] == key:
                return self.table[probe_index]
            if self.keys[probe_index] is None:
                return None
        return None

    def delete(self, key):
        index = self.hash_function(key)
        for i in range(self.size):
            probe_index = (index + i) % self.size
            if self.keys[probe_index] == key:
                self.table[probe_index] = None
                self.keys[probe_index] = None
                return True
            if self.keys[probe_index] is None:
                return False  
        return False

    def __str__(self):
        return str(list(zip(self.keys, self.table)))


#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
import time

initial_data = [
    (1, "value1"),
    (11, "value11"),
    (21, "value21"),
    (2, "value2"),
    (12, "value12")
]

print("Хеш-таблица:")
hash_table = LinearProbingHashTable(10, initial_data)
print(hash_table)

# insert
print("\nВставляем дополнительные элементы:")
start_time = time.time()
hash_table.insert(10, "value10")
hash_table.insert(13, "value13")
end_time = time.time()
print("Хеш-таблица после вставки:")
print(hash_table)
print(f"Время на вставку двух элементов: {end_time - start_time:.6f} секунд")

# search
print("\nИщем элементы:")
start_time = time.time()
value1 = hash_table.lookup(1)
value11 = hash_table.lookup(11)
value3 = hash_table.lookup(3)
end_time = time.time()
print("Значение по ключу 1:", value1)
print("Значение по ключу 11:", value11)
print("Значение по ключу 3:", value3)
print(f"Время на поиск трех элементов: {end_time - start_time:.6f} секунд")

# delete
print("\nУдаляем элемент с ключом 21:")
start_time = time.time()
hash_table.delete(21)
end_time = time.time()
print("Хеш-таблица после удаления ключа 21:")
print(hash_table)
print(f"Время на удаление элемента: {end_time - start_time:.6f} секунд")

print("\nИщем удаленный элемент с ключом 21:")
start_time = time.time()
deleted_value = hash_table.lookup(21)
end_time = time.time()
print("Результат поиска:", deleted_value)
print(f"Время на поиск удаленного элемента: {end_time - start_time:.6f} секунд")