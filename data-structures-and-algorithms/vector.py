class Vector:
    def __init__(self,d):
        self._coords = [0]*d
    def __len__(self):
        return len(self._coords)
    
    def __getitem__(self,j):
        return self._coords[j]

    def __setitem__(self,j,val):
        self._coords[j] = val

    def __add__(self,other):
        if(len(self) != len(other)):
            raise ValueError('dimensions does not match')
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] + other[j]
        return result

    def __eq__(self,other):
        return self._coords == other._coords
    
    def __ne__(self,other):
        return not self == other
    
    def __str__(self):
        return '<' + str(self._coords)[1:-1] + '>'
v = Vector(5) # construct five-dimensional <0, 0, 0, 0, 0>
v[1] = 23 # <0, 23, 0, 0, 0> (based on use of setitem )
v[-1] = 45 # <0, 23, 0, 0, 45> (also via setitem )
print(v[4]) # print 45 (via getitem )
u=v+v # <0, 46, 0, 0, 90> (via add )
print(u) # print <0, 46, 0, 0, 90>
total = 0
for entry in v: # implicit iteration via len and getitem
    total += entry