# Python Calculator

This is a command-line calculator I built in Python for Module 3. You type in a math operation and two numbers, and it gives you the answer. It keeps running until you type `exit`.

It can add, subtract, multiply, and divide. If you type something wrong or try to divide by zero, it tells you what went wrong instead of crashing.

## What you need

- Python 3.10 or newer
- Git

## How to set it up

Clone the repo and go into the folder:

```
git clone https://github.com/atharhanjra/assignment3.git
cd assignment3
```

Make a virtual environment and turn it on:

```
python3 -m venv venv
source venv/bin/activate
```

Install what the project needs:

```
pip install -r requirements.txt
```

## How to use it

Start the calculator:

```
python3 main.py
```

Then type an operation and two numbers, like this:

```
add 5 3
Result: 8.0
```

The operations are `add`, `subtract`, `multiply`, and `divide`. Type `exit` when you're done.

If you type something it doesn't understand, like `add five three` or `divide 5 0`, it shows an error message and lets you try again.

## How the code is organized

- `app/operations/` has the `Operations` class, which does the actual math
- `app/calculator/` has the loop that asks for input and prints results
- `tests/` has all the tests
- `main.py` starts the program

## Running the tests

```
pytest tests --cov=app --cov-report=term-missing
```

This runs all the tests and shows how much of the code they cover. The goal is 100%.

## GitHub Actions

Every time I push to GitHub, the tests run automatically. If a test fails or coverage drops below 100%, the build fails.