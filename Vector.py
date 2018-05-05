# Define Vector class

class Vector(object):
    def __init__(self, coord): # store the passed coordinates as a tuple in the attribute
        try:
            if coord != None:
                self.coord = tuple(coord) # Store Coordinates
                self.length = len(coord) # Store the dimensionality
            else:
             raise ValueError
                
        except ValueError:
            raise ValueError("Coordinates must be supplied")
            
        except TypeError:
            raise TypeError("Coordinate Type must be iterable")
            
    def __str__(self): # Convert the vector to string Format
        return "Vector : {}".format(self.coord)
    
    def add(self, vectors): # add vectors in simple way
        addition = []

        for i in range(0, self.length):
            addn = self.coord[i]
            for j in range(0, len(vectors)):
                addn += vectors[j].coord[i]
            addition.append(addn)
            
        addition = [ ]
        
        return Vector(addition)
    
    def subtract(self, vectors): # subtract vectors in simple way
        subtraction = []

        for i in range(0, self.length):
            subtn = self.coord[i]
            for j in range(0, len(vectors)):
                subtn -= vectors[j].coord[i]
            subtraction.append(subtn)
            
        
        return Vector(subtraction)
    
    def multiply_scalar(self, scalar): # add vectors in simple way
        multipln = []

        for i in range(0, self.length):            
            multipln.append(self.coord[i] * scalar)
        
        return Vector(multipln)
    
def testVector(verbose):
    v1 = Vector([1.3,2.5])
    v2 = Vector([2,3])
    v3 = Vector([3,-2])
    
    if verbose:print("Addition :", v1.add([v2,v3]))
    
    if verbose:print("Subtraction :", v1.subtract([v3]))
    
    if verbose:print("Multiplication :", v1.multiply_scalar(5))
    
def main(argsv):
    testVector(verbose=argsv[0])
    
if __name__ == "__main__":
    argsv = [True]
    main(argsv)

            
            
            