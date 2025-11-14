#create a list of even numbers between 2 and 20 (inclusive)
even_numbers = list(range(2, 21, 2))

# append 22 to the list
even_numbers.append(22)

# remove the smallest number 
even_numbers.remove(min(even_numbers))

# calculating the sum of the remaining numbers
total_sum = sum(even_numbers)

# calculate the average
average_value = total_sum / len(even_numbers)

# print the results
print(f"Numbers: {even_numbers}")
print(f"Sum: {total_sum}")
print(f"Average: {average_value:.2f}")