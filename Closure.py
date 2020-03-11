# An example of a closure that stores the value of x and the function pw.
# It remembers the value of x when it was defined and uses that x in the pw function
def power(x):
    def pw(y):
        return y ** x
    return pw


# Create objects that store a different value of x, but call the same pw function
square = power(2)
cube = power(3)
power10 = power(10)
testNum = 3


# Test the objects created above
print("The square of {} is {}".format(testNum, square(testNum)))
print("The cube of {} is {}".format(testNum, cube(testNum)))
print("The power10 of {} is {}".format(testNum, power10(testNum)))
