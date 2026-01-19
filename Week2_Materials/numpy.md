* NumPy in a linear algebra library
* NumPy arrays are how we will use this library
* NumPy arrays can be: vectors or matricies
    * Vectors are 1-d arrays
    * Matricies are 2-d arrays

Functions and Attributes to remember:
* np.array() - creates an n-dimensional array from a list or tuple
* np.arange(start,stop,step) - creates an array with values evenly spaced by the step size
* np.linspace(start,stop,interval) - creates an array with specified number of evenly spaced values over a given interval
* np.random.rand() or np.random.randint() - generates arrays with random numbers which are useful for simulations or data augmentation
* np.min(array)
* np.max(array)
* np.mean(array)
* np.dot(array1, array2) - performs matrix multiplication (dot product) between two arrays
* .shape - shape of array
* .ndim - dimensions of array
* .dtype - data type
* .size - total number of elements of an array

Array Manipulations to remember:
* np.reshape(array, new_shape) - change the shape of an array without modifying its data
* np.transpose(array) or np.T(array) - transpose the array
* np.concatenate((array1, array2), axis=...) - joints two or more arrays along specified axis (axis=0 is row, axis=1 is column)

**This list is not exhaustive**