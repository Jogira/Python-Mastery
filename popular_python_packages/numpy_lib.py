import numpy as np

array = np.array([[1,2,3],[4,5,6]])
print(array.shape)
print(array)

zeroarray = np.zeros((3,4), dtype=int)
print(zeroarray)

onesarray = np.ones((3,4), dtype=int)
print(onesarray)

randarray = np.random.random((3,4))
print(randarray)
print(randarray[0,0])

print(randarray > 0.2)
print(randarray[randarray> 0.2])

print(np.sum(randarray))
print(np.floor(randarray))
print(np.ceil(randarray))


first = np.array([1,2,3])
second = np.array([1,2,3])
print(first + second)
print(first + 2)

dims_in = np.array([1,2,3])
dims_cm = dims_in * 2.54
print(dims_cm)

#VS this way of doing it. 
dimensions_inch = [1,2,3]
dimensions_cm = [x * 2.54 for x in dimensions_inch]
print(dimensions_cm)

