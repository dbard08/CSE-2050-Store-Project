from entry import Entry

class HashMapping:
    """Mapping ADT using buckets and hashing"""
    def __init__(self, size = 2):
        """create empty buckets and start with 0 pairs """
        self.size = size
        self.buckets = []
        for i in range(size):
            self.buckets.append([])
        self.count = 0

    def put(self, key, value):
        """add new pair or update value if key exists"""
        bucket = self.buckets[hash(key) % self.size]
        for entry in bucket:
            if entry.key == key:
                entry.value = value
                return
        bucket.append(Entry(key, value))
        self.count += 1
        if self.count > self.size:
            self.rehash()

    def get(self, key):
        """return value for key"""
        bucket = self.buckets[hash(key) % self.size]
        for entry in bucket:
            if entry in bucket:
                if entry.key == key:
                    return entry.value
        raise KeyError(key)

    def __contains__(self, key):
        """return True is key is stored"""
        bucket = self.buckets[hash(key) % self.size]
        for entry in bucket:
            if entry.key == key:
                return True
        return False

    def __len__(self):
        """return number of stored pairs """
        return self.count

    def rehash(self):
        """double table size and reinsert entires"""
        old_buckets = self.buckets
        self.size = self.size * 2
        self.buckets = []
        for i in range(self.size):
            self.buckets.append([])
        for bucket in old_buckets:
            for entry in bucket:
                self.buckets[hash(entry.key) % self.size].append(entry)