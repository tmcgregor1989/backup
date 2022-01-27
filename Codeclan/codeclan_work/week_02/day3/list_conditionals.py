
# numbers = range(1, 11)
# evens_squared = []
# print(numbers)
# print(evens_squared)

# for number in numbers:
#     if number % 2 == 0:
#         evens_squared.append(number * number)

# print(evens_squared)


# evens_squared = [expression for item in list if conditional]



# evens_squared = [number * number for number in range(1, 11) if number % 2 == 0]

# print(evens_squared)





# Using single list comprehension, and the following list:

# task_loops.py

ages = [5, 15, 64, 27, 84, 26]
# Return a list of only the odd ages.

odd_ages = [number for number in ages if number % 2 != 0]

print(odd_ages)




# Using single list comprehension, and the following list:

# task_loops.py

chicken_names = ["Hen Solo", "Cluck Norris", "Hennifer Lopez", "ChewPekka", "Feather Locklear"]
# Return a list with chickens whose name is more than 10 characters
# Return a list of chickens whose name starts with the letter H

long_names = [chicken for chicken in chicken_names if len(chicken) > 10]
print(long_names)

h_names = [chicken for chicken in chicken_names if chicken[:1] == "H"]
print(h_names)



# Part 3
# ======

# Using a single list comprehension, and the following list:

# task_loops.py

words = ["The", "quick", "brown", "fox", "jumped", "over", "the", "lazy", "dog"]
# Build a new list, with the first letter from each word
# Convert each letter to lower case
# Expected output: ["t", "q", "b", "f", "j", "o", "t", "l", "d"]

# Hint: Strings in Python work as if they were a tuple full of characters. How would you get the first element from a tuple or list?

first_letters = [str.lower(word[0]) for word in words]
print(first_letters)