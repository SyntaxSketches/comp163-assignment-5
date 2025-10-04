current_number = int(input("Enter starting number: "))
step_count = 0

print("Sequence:", end=" ")
while current_number != 1:
    print(current_number, end=" ")

if current_number % 2 == 0:
        current_number = current_number // 2
else:
        current_number = (current_number * 3) + 1
        
    step_count += 1
print(current_number)
print("Steps:", step_count)

#challenge 2

if number <= 1:
    print(f"{number} is not prime (not greater than 1).")
else:
    print(f"Testing divisors from 2 to {number - 1}...")
is_prime = True
for divisor in range(2, number):
        if number % divisor == 0:
            print(f"{number} is not prime (divisible by {divisor}).")
            is_prime = False
            break  

if is_prime:
        print(f"{number} is prime!")

#challenge three

print("Multiplication Table:")
print("    ", end="")
for col in range(1, 11):
    print(f"{col:4}", end="")
print()


for row in range(1, 11):
print(f"{row:2}", end="  "
for col in range(1, 11):
        product = row * col
        print(f"{product:4}", end="")
    print() 


