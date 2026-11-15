"""
1) Add the file and topic details.
   a) Mention the file name as `02-not-xor-shifts.py`.
   b) Mention the topic as "NOT, XOR, Left Shift, Right Shift".
   c) Introduce the program as a way to understand more bitwise operators.

2) Ask for a number.
   a) Ask the user to enter a number.
   b) Suggest example values like 5 or 12.
   c) Convert the input into an integer.

3) Ask for a left shift prediction.
   a) Explain that left shift doubles the number.
   b) Ask the user to guess the result of `n << 1`.
   c) Store the user's guess.

4) Demonstrate the NOT operator.
   a) Pause before showing the NOT example.
   b) Print the binary form of 12.
   c) Use `~12` to flip the bits.
   d) Use `& 0xFF` to show the result inside 8 bits.

5) Demonstrate the XOR operator.
   a) Pause before showing the XOR example.
   b) Use `12 ^ 10` to perform bitwise XOR.
   c) Explain that XOR gives 1 when the bits are different.

6) Demonstrate left shift.
   a) Pause before showing the left shift example.
   b) Use `n << 1` to shift bits one place left.
   c) Show that this multiplies the number by 2.
   d) Print the user's original guess.

7) Demonstrate right shift.
   a) Pause before showing the right shift example.
   b) Use `n >> 1` to shift bits one place right.
   c) Show that this divides the number by 2.

8) Display the final results.
   a) Show the output of NOT, XOR, left shift, and right shift.
   b) Help the user compare how each bitwise operator changes the number.
"""

n = int(input("Enter a number (like 5 or 12): "))
user_left_shift_guess = int(input(f"Guess the result of {n} << 1 (left shift): "))
input("Press Enter to see the NOT operation example...")

binary_12 = bin(12)[2:]
not_result = ~12 & 0xFF
print(f"Binary of 12: {binary_12}")
print (f"~12 = {not_result} (in decimal, showing only the last 8 bits)")

input("Press Enter to see the XOR operation example...")
xor_result = 12 ^ 10
print(f"12 ^ 10 = {xor_result} (in decimal)")

input("Press Enter to see the left shift operation example...")
left_shift_result = n << 1
print(f"{n} << 1 = {left_shift_result} (in decimal)")

input("Press Enter to see the right shift operation example...")
right_shift_result = n >> 1
print(f"{n} >> 1 =")
