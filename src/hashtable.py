# '''
# Linked List hash table key/value pair
# '''


class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''

    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity

    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)

    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        hash = 5381

        for c in key:
            hash = (hash * 33) + ord(c)

        return hash

    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity

    def insert(self, key, value):
        '''
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Fill this in.
        '''
        # Get index from hash
        index = self._hash_mod(key)
        # If there isn't a value, add the value directly
        if self.storage[index] is None:
            self.storage[index] = LinkedPair(key, value)
        else:
            current = self.storage[index]
            while current is not None:
                if current.key == key:
                    current.value = value
                    break
                else:
                    if current.next is None:
                        current.next = LinkedPair(key, value)
                    else:
                        current = current.next

    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        index = self._hash_mod(key)

        current = self.storage[index]

        # If index is empty
        if current == None:
            return 'No key found.'
        # If there is only one LinkedPair
        elif current.next is None and current.key == key:
            self.storage[index] = None
        # Otherwise, find the key and remove
        else:
            prevNode = None
            nextNode = current.next
            while current is not None:
                if current.key == key:
                    if prevNode is None:
                        self.storage[index] = nextNode
                    else:
                        if nextNode:
                            prevNode.next = nextNode
                        else:
                            prevNode.next = None
                    break
                else:
                    if current.next is None:
                        return 'No key found'
                    else:
                        prevNode = current
                        current = current.next
                        nextNode = current.next

    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        index = self._hash_mod(key)

        current = self.storage[index]
        while current is not None:
            if current.key == key:
                return current.value
            else:
                current = current.next
        return None

    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        self.capacity *= 2
        new_storage = [None] * self.capacity

        for i in range(len(self.storage)):
            current = self.storage[i]

            while current is not None:
                index = self._hash_mod(current.key)
                if new_storage[index] is None:
                    new_storage[index] = LinkedPair(current.key, current.value)
                else:
                    new_storage[index].next = LinkedPair(
                        current.key, current.value)
                current = current.next

        self.storage = new_storage


if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
