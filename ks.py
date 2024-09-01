
file_name = "sum"

with open(file_name, "w") as file:
    file.write("10\n")
    file.write("20\n")
    file.write("30\n")
    file.write("40\n")
    file.write("50\n")

print(f"File '{file_name}' created with some numbers.")


total_sum = 0

with open(file_name, "r") as file:
    for line in file:
        number = int(line.strip())  
        total_sum += number

print(f"The sum of the numbers in the file '{file_name}' is: {total_sum}")