'''
***PART 2***

Write a program that prompts the user to enter a number. The program then prints "Hunter" the number of times the user entered. Use a while loop.

Example of what should appear when the program runs:

Times to print: 3
Hunter
Hunter
Hunter

'''

num = int(input("Times to print: ")) #num = times to print
printed = 0
if num > 0:
  while printed < num:
    print ("Hunter ")
    printed += 1
elif num <= 0:
  print ("Sorry! I can only print a positive number of times.")

