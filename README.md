## Fork & Clone

Repeating the same steps to fork and clone from the previous task, fork and clone [this repository](https://github.com/JoinCODED/calculator) in your `python` directory.

---

## Task 

In this task you'll be creating a calculator. You'll ask the user for two numbers and the mathematical operation and then print the result of that operation.

Example:

```
Enter the first number: 4
Enter the second number: 6
Choose the operation (+, -, /, *): *
The answer is 24
```

In this example, the user inputs the first number `4`, the second number `6`, and the operation `*`.

## Steps:
1. Ask the user for the two numbers and operation.
2. Validate user input.
	- If the user's inputs were not numbers, print to the user that the numbers were invalid. For example if the user enters letters instead of numbers. (Hint: [String methods](https://www.w3schools.com/python/python_ref_string.asp) can help.)
	- If the operation the user entered was not any of the options (`+`, `-`, `*`, or `/`), print to the user that the operation is not valid.
3. If the user entered valid numbers and a valid operation, perform the calculation and print it to the user.
4. Add and commit `calculator.py`, then push to Github.
