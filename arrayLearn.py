
import array as arr

l = [1, 2, 3, 4, 5,]

a = arr.array('i', l)
print("Initial Array: ")
for i in a:
	print(i, end=" ")

Sliced_array = a[3:8]
print("\nSlicing elements in a range 3-8: ")
print(Sliced_array)

a[1] = 5
for i in a:
	print(i,end =' ')
