"""
1) Add the file and topic details.
   a) Mention the file name as `03-parity-bits.py`.
   b) Mention the topic as "Parity Check and Counting Bits".
   c) Introduce the program as a way to check even or odd numbers using bits.

2) Explain the parity idea.
   a) Show that the last bit decides if a number is even or odd.
   b) Explain that last bit 0 means even.
   c) Explain that last bit 1 means odd.
   d) Pause the program before running the examples.

3) Check even and odd numbers.
   a) Use a for loop with numbers 2, 3, 4, 5, 8, and 9.
   b) Use `n & 1` to check the last bit.
   c) Print odd when the last bit is 1.
   d) Print even when the last bit is 0.

4) Ask for a number.
   a) Ask the user to enter a number.
   b) Suggest example values like 13 or 7.
   c) Convert the input into an integer.

5) Prepare to count 1 bits.
   a) Store the user's number in `temp`.
   b) Use `temp` so the original number `n` stays unchanged.
   c) Pause before starting the bit-counting loop.

6) Drop bits using right shift.
   a) Use a while loop while `temp` is greater than 0.
   b) Print the current binary form of `temp`.
   c) Use `temp & 1` to show the last bit.
   d) Use `temp >>= 1` to shift bits right by one place.

7) Count the total 1 bits.
   a) Use `bin(n)` to get the binary form of the original number.
   b) Use `.count('1')` to count how many 1s are present.
   c) Print the total number of 1 bits in the number.
"""