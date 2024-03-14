squared_numbers = [x ** 2 for x in range(10)]
print("Squared_numbers:", squared_numbers)


even_numbers = [x for x in range(10) if x%2 == 0]
print("Even numbers:", even_numbers)

pairs = [(x,y) for x in range(3) for y in range(3)]
print("Pairs:", pairs)

words = ["apple", "banana", "orange", "cherry"]
word_lengths = [len(words) for word in words]
print("Words lengths:", word_lengths)


labels = ["even" if x % 2 == 0 else "odd" for x in range(10)]
print("Labels:", labels)


numbers = [x ** 2 if x % 2 == 0 else x ** 3 for x in range(10)]
print("Numbers:", numbers)


uppercase_letters = [chr(x) for x in range(65,91)]
print("Uppercase letters:", uppercase_letters)

squares_of_even = [x ** 2 for x in range(1,11) if x%2 == 0]
print("Squares of even numbers:", squares_of_even)


list1 = [1,2,3]
list2 = ['a','b','c']
combined_list = [(x,y) for x in list1 for y in list2]
print("Combined lists:", combined_list)


primes = [x for x in range(2,101) if all(x%y != 0 for y in range(2,int(x ** 0.5)+1))]
print("Prime numbers:", primes)

words = ["apple", "banana", "orange", "cherry", "kiwi", "pear"]
long_words = [word for word in words if len(word) > 3]
print("Words with more than three characters:", long_words)

list1 = [1,2,3]
list2 = [4,5,6]
sums = [x+y for x,y in zip(list1, list2)]
print("Sums of corresponsing elements:", sums)
