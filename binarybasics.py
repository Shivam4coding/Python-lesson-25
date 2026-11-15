"""
1) Add the file and topic details.
   a) Mention the file name as `01-bits-and-binary.py`.
   b) Mention the topic as "Bits and Binary Numbers, AND and OR".
   c) Introduce the program as a way to understand binary and bitwise operators.

2) Ask for a number.
   a) Ask the user to enter a number.
   b) Suggest example values like 5 or 12.
   c) Convert the input into an integer.

3) Ask for a binary prediction.
   a) Ask the user to guess the binary form of the number.
   b) Store the user's guess.

4) Show the binary form.
   a) Pause the program before showing the answer.
   b) Use `bin(n)` to convert the number into binary.
   c) Use `[2:]` to remove the `0b` prefix.
   d) Print the decimal number and its binary form.
   e) Print the user's original guess.

5) Demonstrate the AND operator.
   a) Pause before showing the AND example.
   b) Print the binary forms of 12 and 10.
   c) Use `12 & 10` to perform bitwise AND.
   d) Explain that AND gives 1 only when both bits are 1.

6) Demonstrate the OR operator.
   a) Pause before showing the OR example.
   b) Use `12 | 10` to perform bitwise OR.
   c) Explain that OR gives 1 when at least one bit is 1.

7) Display the final results.
   a) Show the decimal output of the AND operation.
   b) Show the decimal output of the OR operation.
   c) Help the user compare how both bitwise operators work.
"""

n = int(input("Enter a number (like 5 or 12): "))
user_guess = input("Guess the binary form of the number: ")
input("Press Enter to see the binary form...")
binary_form = bin(n)[2:]

print(f"The decimal number {n} in binary is: {binary_form}")
print(f"Your guess was: {user_guess}")

binary_12 = bin(12)[2:]
binary_10 = bin(10)[2:]

input("Press Enter to see the AND operation example...")
and_result = 12 & 10
print(f"Binary of 12: {binary_12}")
print(f"Binary of 10: {binary_10}")
print(f"12 & 10 = {and_result} (in decimal)")

input("Press Enter to see the OR operation example...")
or_result = 12 | 10
print(f"12 | 10 = {or_result} (in decimal)")



