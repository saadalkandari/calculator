## Fork & Clone

Repeat the same steps in the previous task to fork and clone this repository into your `python` directory: [this repository](https://github.com/JoinCODED/calculator).

---

## Task 

In this task you'll be creating a calculator. You'll ask the user for 3 inputs: two numbers, and a mathematical operation. Then you will print the result of the operation to the user.

Example:

```
Enter the first number: 4
Enter the second number: 6
Choose the operation (+, -, /, *): *
The answer is 24
```

In this example, the user inputs the first number `4`, the second number `6`, and the operation `*`.

## Steps:
1. Ask the user for 3 inputs:  two numbers and an operation.
2. Validate user input.
	- If the user's inputs were not numbers, print to the user that the numbers were invalid. For example if the user enters letters instead of numbers. (Hint: [String methods](https://www.w3schools.com/python/python_ref_string.asp) can help.)
	- If the operation the user entered was not any of the options (`+`, `-`, `*`, or `/`), print to the user that the operation is not valid.
3. If the user entered valid numbers and a valid operation, perform the calculation and print it to the user.
4. Run the tests and make sure they pass by running the following command on macOS `python3 test.py` (`python test.py` on Windows)
5. Add and commit `calculator.py`, then push to Github.
   
