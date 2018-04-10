class hashtable:
    """Implementation of a basic hash table"""
    def __init__(self,size):
        """hash table is intitalized with a certain size
        which determines the number of slots in the table"""
        self.size = size
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def put(self, key, data):
        """Given a key and a piece of data, the function
        utilizes a hash function to encrypt and store the data
        at a certain location in the hash table. If that location
        is already full, the values are rehashed to find a new
        storage location."""
        hashvalue = self.hashfunction(key,len(self.slots))

        if self.slots[hashvalue] ==None:
            self.slots[hashvalue] = key
            self.data[hashvalue] = data
        else:
            if self.slots[hashvalue] == key:
                #replaces data
                self.data[hashvalue] = data
            else:
                nextslot = self.rehash(hashvalue, len(self.slots))
                while self.slots[nextslot] != None and self.slots[nextslot] != key:
                    nextslot = self.rehash(nextslot, len(self.slots))
                if self.slots[nextslot] == None:
                    self.slots[nextslot] = key
                    self.data[nextslot] = data
                else:
                    self.data[nextslot] = data

    def hashfunction(self,key,size):
        """A basic hash function which returns a 
        value equal to the remainder of the key divided
        by the size of the hash table"""
        return key%size
    
    def rehash(self,oldhash,size):
        """A simple change to the hash function which offsets
        the storage location by 1"""
        return (oldhash + 1) % size

    def get(self,key):
        """Utilizes a key to return the data stored in
        the hash table. Returns None if no data is found."""
        startslot = self.hashfunction(key,len(self.slots))
        data = None
        stop = False
        found = False
        position = startslot
        while self.slots[position] != None and not found and not stop:
            if self.slots[position] == key:
                found = True
                data = self.data[position]
            else:
                position=self.rehash(position,len(self.slots))
                if position == startslot:
                    stop = True
        return data

    def __getitem__(self,key):
        return self.get(key)
    
    def __setitem__(self, key,data):
        self.put(key,data)


