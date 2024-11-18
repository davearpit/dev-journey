class HashMap:
    def __init__(self, size):
        self.size = size
        self.hash_table = [[] for _ in range(self.size)]

    def insert(self, key, value):
        hashed_key = hash(key) % self.size

        bucket = self.hash_table[hashed_key]

        found_key = False
        for pos, el in enumerate(bucket):
            record_key, record_val = el
            if record_key == key:
                found_key = True
                break

        if found_key == True:
            bucket[pos] = (key, value)
        else:
            bucket.append((key, value))

        self.hash_table[hashed_key] = bucket
        return
    
    def get(self, key):
        hashed_key = hash(key) % self.size

        bucket = self.hash_table[hashed_key]

        found_key = False
        for pos, el in enumerate(bucket):
            record_key, record_val = el

            if record_key == key:
                found_key = True
                break

        if found_key == True:
            return record_val
        else:
            return 'No Record with the given key'
        
    def delete(self, key):
        hashed_key = hash(key) % self.size

        bucket = self.hash_table[hashed_key]

        found_key = False
        for pos, el in enumerate(bucket):
            record_key, record_val = el

            if record_key == key:
                found_key = True
                break
        
        if found_key == True:
            bucket.pop(pos)
            self.hash_table[hashed_key] = bucket
            return 
        else:
            return "No such element exists"

    def __repr__(self):
        return "".join(str(item) for item in self.hash_table)