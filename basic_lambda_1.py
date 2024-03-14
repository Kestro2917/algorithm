pairs = [(1,20), (3,10), (2,30)]
sorted_pairs = sorted(pairs, key=lambda x:x[1])
print("Sorted pairs based on the second element:", sorted_pairs)


numbers = [1,2,3,4,5]
squared_numbers = list(map(lambda x:x ** 2, numbers))
print("Squared numbers:", squared_numbers)

numbers = [1,2,3,4,5]
even_numbers = list(filter(lambda x:x % 2 == 0, numbers))
print("Even numbers:", even_numbers)


def apply_operation(x, y, operation):
	return operation(x,y)

result = apply_operation(10, 5, lambda x, y: x+y)
print("Result of addition:", result)

result = apply_operation(10, 5, lambda x, y: x-y)
print("Result of substraction:", result)

numbers = [1,2,3,4,5]
doubled_numbers = [(lambda x:x*2)(x) for x in numbers]
print("Doubled numbers using list comprehension:", doubled_numbers)

words = ["apple", "banana", "orange", "cherry"]
sorted_words = sorted(words, key=lambda x: len(x))
print("Words sorted based on length:", sorted_words)
