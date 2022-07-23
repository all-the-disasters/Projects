!#python3
"""My solutions to projects from https://github.com/karan/Projects#text"""


def fizz_buzz():
    t = [i for i in range 100 if i % 5 != 0 & i % 3 != 0 elif i % 15 == 0 i = "fizzbuzz" elif i % 5 == 0 i = "buzz" else i = "fizz"]
    print(result for result in t)


def reverse_text(text):
    return "".split(text).join("")


if __name__ == '__main__':
    print("Fizz buzz result:\n")
    fizz_buzz()
    print("/n/nReversing provided text result:")
    reverse_text(input("Enter text to reverse and click enter."))
    print("/n/nEnd of testing.")
