# Implement Vector applications from scratch
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
    
    def add(self, vectors): # add vectors in simple and list compprehension way
#        addition = []
#
#        for i in range(0, self.length):
#            addn = self.coord[i]
#            for j in range(0, len(vectors)):
#                addn += vectors[j].coord[i]
#            addition.append(addn)
            
        addition = self.coord   
        for v in vectors:
            addition = [x+y for x, y in zip(addition, v.coord)] # Use List complerehension
        
        return Vector(addition)
    
    def subtract(self, vectors): # subtract vectors in simple and list comrehension way
#        subtraction = []
#
#        for i in range(0, self.length):
#            subtn = self.coord[i]
#            for j in range(0, len(vectors)):
#                subtn -= vectors[j].coord[i]
#            subtraction.append(subtn)
#            
        
        subtraction = self.coord   
        for v in vectors:
            subtraction = [x-y for x, y in zip(subtraction, v.coord)] # Use List complerehension
        
        return Vector(subtraction)
    
    def multiply_scalar(self, scalar): # scalar multiplication vectors in simple and list comprehension way
#        multipln = []
#
#        for i in range(0, self.length):            
#            multipln.append(self.coord[i] * scalar)
#        
        
        multipln = self.coord
        multipln = [x*scalar for x in self.coord]
        return Vector(multipln)
    
    def magnitude(self): # magnitude of vector in simple and list comrehension way
       
#        magsquare = 0
#        for x in self.coord:
#            magsquare += x**2
 
        magsquare = [x**2 for x in self.coord] # List comprehension way
           
        return (sum(magsquare)**0.5)
    
    def normalize(self): # normalization of vector
       
        try:
            
            magnitude = self.magnitude()
            return self.multiply_scalar(1/magnitude)

        except ZeroDivisionError:
            raise ValueError("Zero Vector cannot be normalized")


    
def testVector(verbose):
    v1 = Vector([1.3,2.5])
    v2 = Vector([4,3])
    v3 = Vector([3,-2])
    v4 = Vector([-2,2])
    v5 = Vector([0,0])
    
    if verbose:print("Addition :", v1.add([v2,v3]))
    
    if verbose:print("Subtraction :", v1.subtract([v3]))
    
    if verbose:print("Multiplication :", v1.multiply_scalar(5))
    
    if verbose:print("Maganitude :", v2.magnitude())
    
    if verbose:print("Normalized :", v2.normalize())
    
    if verbose:print("Normalized :", v4.normalize())
    
    if verbose:print("Normalized :", v5.normalize())
    
def main(argsv):
    testVector(verbose=argsv[0])
    
if __name__ == "__main__":
    argsv = [True]
    main(argsv)

            
            
            