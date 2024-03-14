words = ["apple", "banana", "orange", "cherry"]
sorted_words = sorted(words, key= lambda x:len(x))
print("Sorted words by length:", sorted_words)

numbers = [1,2,3,4,5,6,7,8,9,10]
even_numbers = list(filter(lambda x:x %2 == 0, numbers))
print("Even numbers:", even_numbers)

celsius_temperatures = [0,10,20,30,40]
fahrenheit_temperatures = list(map(lambda x: (x * 9/5) + 32, celsius_temperatures))
print("Fahrenheit temperatures:", fahrenheit_temperatures)

sentences = ["Hello world", "Python is awesome", "lambda functions are cool"]
last_words = list(map(lambda x:x.split()[-1], sentences))
print("Last words:", last_words)

power_function = lambda x, n: x ** n
result = power_function(2,3)
print("Result:", result)
