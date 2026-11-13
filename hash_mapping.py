from entry import Entry

class HashMapping:

    def __(self, size = 2):
        self.size = size
        self.buckets = []
        for i in range(size):
            self.buckets.append([])
        self.count = 0

    def put(self, key, value):
        bucket = self.bucket[hash(key) % self.size]
        for entry in bucket:
            if entry.key == key:
                entry.value = value
                return
            bucket.append(Entry(key, value))
            self.count += 1
            if self.count > self.size:
                self.reheash()

    def get(self, key):
        bucket = self.buckets[hash(key) % self.size]
        for entry in bucket:
            if entry in bucket:
                if entry.key == key:
                    return entry.value
        raise KeyError(key)

    def __contains__(self, key):
        bucket = self.buckets[hash(key) % self.size]
        for entry in bucket:
            if entry.key == key:
                return True
        return False

    def __len__(self):
        return self.count

    def rehash(self):
        old_buckets = self.buckets
        self.size = self.size * 2
        self.buckets = []
        for i in range(self.size):
            self.buckets.append([])
        for bucket in old_buckets:
            for entry in bucket:
                self.buckets[hash(entry.key) % self.size].append(entry)