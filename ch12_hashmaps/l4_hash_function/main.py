class HashMap:
    def key_to_index(self, key):
        """
        Convert a string key into a valid array index using a simple hash function.

        Steps:
        1. Sum the Unicode values (ord) of every character in the key
        2. Take that sum modulo self.size to get an index in range [0, self.size-1]

        Args:
            key: The string key (e.g., username)

        Returns:
            int: Index where this key should be stored / looked up
        """
        total = 0
        for char in key:
            total += ord(char)
        return total % len(self.hashmap)


    # don't touch below this line

    def __init__(self, size):
        self.hashmap = [None for i in range(size)]

    def __repr__(self):
        buckets = []
        for v in self.hashmap:
            if v != None:
                buckets.append(v)
        return str(buckets)