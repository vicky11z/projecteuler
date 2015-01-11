#Problem 1: Multiples of 3 and 5

"""If we list all the natural numbers below 10 that are multiples of 
3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 100"""

class naturalNumbersIterator():
	#uses a generator to list natural numbers beginning with START
	def __init__(self, start, end):
		self.start = start #takes in a starting natural number
		self.end = end #takes in an ending natural number

	def __iter__(self):
		next_number = self.start
		while next_number < self.end:
			yield next_number
			next_number += 1
	
def multiples(lst, mul):
	#takes in a list of numbers and a multiple to pare the list down
	result = []
	for num in lst:
		if num % mul == 0:
			result.append(num)
	return result


def remove_duplicates(lst1, lst2):
	#combines two lists, removing the duplicates
	lst = lst1 + lst2
	rm = set(lst)
	return list(rm)

one = naturalNumbersIterator(1, 1000)
natural_ones = list(one)
#get a list of natural numbers from 1 to 1000

m_threes = multiples(natural_ones, 3)
m_fives = multiples(natural_ones, 5)
#create two separate lists: one for multiples of 3, one for multiples of 5

final_list = remove_duplicates(m_threes, m_fives)
#combine and remove duplicates from the two lists

answer = sum(final_list)
#sum the list to reach the answer