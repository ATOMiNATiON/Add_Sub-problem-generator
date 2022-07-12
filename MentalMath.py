#------------------------------------------------------------------------------
# Created by Adam Wu on 7/10/2022
# Simple Mental Math program
# MentalMath.py
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
# imports
#------------------------------------------------------------------------------
import random

#------------------------------------------------------------------------------
# Functions
#------------------------------------------------------------------------------

def num_generator(digits):
	if digits == 1:
		d = random.randint(-9,9)
		return d
	else:
		new_d = "9" * digits
		num = int(new_d)
		d = random.randint(-num, num)

		if len(new_d) == len(str(abs(d))):
			return d
		else:
			# use recursion
			return num_generator(digits)
# end num_generator()

def form_dig(probs):
	g = []
	for i in range(len(probs)):
		com_num = f'{probs[i]:,}'
		g.append(com_num)
	return g
# end form_dig()

def prob_gen(numbers, digits):

	while True:
		A = []
		while len(A) != numbers:
			x = num_generator(digits)
			A.append(x)
			answer = sum(A)
			if answer > 0:
			    continue
			else:
			    A.clear()
		if answer > 0:
			return A
		else:
			continue
# end prob_gen()

#------------------------------------------------------------------------------
def main():

   while True:

 	   num = input("Enter the # of digits (press enter to quit): ")
 	   if num == "":
 	    	break

 	   digits = int(num)
 	   numbers = int(input("Enter the # of numbers: "))
 	   probs = prob_gen(numbers, digits)
 	   print()

 	   h = form_dig(probs)
 	   for i in range(len(h)):
 	     	print("{0:>7}".format(h[i]))


 	   answer = sum(probs)
 	   user_ans = int(input(" Answer: "))
 	   if user_ans == answer:
 	   	print("Correct!\n")
 	   else:
 	   	print(f"You are incorrect, the answer is {answer}\n")
# end main()

# conditional statement--------------------------------------------------------
if __name__=='__main__':
	main()
#------------------------------------------------------------------------------
