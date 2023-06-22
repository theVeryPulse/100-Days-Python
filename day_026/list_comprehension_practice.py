# list comprehension examples
# each elements + 1
a_list = [1, 2, 3]
b_list = [n + 1 for n in a_list[::-1]]
print(b_list)

# each element * 2
c_list = [2 * n for n in range(1, 4)]
print(c_list)

# each element to upper case
d_list = ['Alex', 'Beth', 'Caroline']
e_list = [name.upper() for name in d_list]


# dictionary comprehension example
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
s_list = sentence.split()
result = {word: len(word) for word in s_list}
print(result)


# convert celsius to fahrenheit
weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}
weather_f = {day: (temp_c * 9/5) + 32 for (day, temp_c) in weather_c.items()}  # use .items() to get both key and value
print(weather_f)