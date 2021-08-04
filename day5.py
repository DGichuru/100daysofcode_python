"""#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level
# password = ""

# for char in range(1, nr_letters + 1):
#   password += random.choice(letters)

# for char in range(1, nr_symbols + 1):
#   password += random.choice(symbols)

# for char in range(1, nr_numbers + 1):
#   password += random.choice(numbers)

# print(password)

#Hard Level
password_list = []

for char in range(1, nr_letters + 1):
  password_list.append(random.choice(letters))

for char in range(1, nr_symbols + 1):
  password_list += random.choice(symbols)

for char in range(1, nr_numbers + 1):
  password_list += random.choice(numbers)

print(password_list)
random.shuffle(password_list)
print(password_list)

password = ""
for char in password_list:
  password += char

print(f"Your password is: {password}")"""

"""#average height
student_heights = [180, 124, 165, 173, 189, 169, 146]

sum_heights = 0
students_number = 0

for n in range(0 , len(student_heights)):
   student_heights[n] = int(student_heights[n])

for height in student_heights:
    sum_heights += height
for student in student_heights:
    students_number += 1

result = round(sum_heights / students_number)


print(f"The average is :{result}")"""

"""scores = input("Enter the test scores \n").split()

student_scores = [78, 65, 89, 86, 55, 91, 64, 89]

for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])

hig
hest_score = 0
for score in student_scores:
    if score > highest_score:
        highest_score = score

print(highest_score)
"""
"""total = 0

for num in range(0 , 100 + 1, 2):
    total += num


print(f"The total is:{total}") """
    
"""for num in range(1, 101):
    if (num % 3 == 0) and (num % 5 == 0):
        print('Fizz Buzz')
        continue
    elif (num % 3 == 0):
        print('Fizz')
        continue
    elif (num % 5 == 0):
        print('Buzz')
        continue
    else:
        print(num)
"""
"""fruits = ["Apple", "Peach", "Pear"]
for fruit in fruits:
  print(fruit)
  print(fruit + " Pie")
print(fruits)"""
