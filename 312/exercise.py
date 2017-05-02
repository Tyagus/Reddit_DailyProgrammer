# /r/dailyprogrammer -> Challange #312
# Description:
# Given an integer, 
# find the next largest integer using ONLY the digits 
# from the given integer.
# https://www.reddit.com/r/dailyprogrammer/comments/67q3s6/20170426_challenge_312_intermediate_next_largest/
# Code: Tiago Ribeiro

# import time for performance
import time
start_time = time.time()

# Helper function to get an int from a list of int
def intFromList(numList):
	s = map(str, numList)
	s = ''.join(s)
	s = int(s)
	return s

# Gets all the permutations in a list using Heap Permutations algorithm
def heapPermutations(number):

	listAlg = map(int, str(number))
	allPermutations = []

	def Heap(list, n, size):

		if(size == 1):
			allPermutations.append(intFromList(list))

		for i in range(size):
			Heap(list, n, size-1)

			if(size%2==1):
				temp = list[0]
				list[0] = list[size-1]
				list[size-1] = temp
			else:
				temp = list[i]
				list[i] = list[size-1]
				list[size-1] = temp

	Heap(listAlg, len(listAlg), len(listAlg))
	return allPermutations

# Value that will store the solution
solution = 0

# Get input
number = input("Input Number: ")

# Get all the permutations
list = (heapPermutations(number))

# Sort the permutations
list.sort()

# Returns the next number after the input
for i in range(len(list)):
	if(list[i]==number and (i+1) < len(list)):
		solution = list[i+1]

print ("The solution is: ", solution)
print ("The running time was: ", "--- %s seconds ---" % (time.time() - start_time))
print ("--End--")
end = input("Press a key to end the program...")

