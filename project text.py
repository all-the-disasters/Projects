#!python3
"""My solutions to projects from
https://github.com/karan/Projects#text"""
import fnmatch
import logging
import random
import time
from pathlib import Path


def fizz_buzz():
    """Write a program that prints the numbers from 1 to 100. But for multiples of three print “Fizz” instead
    of the number and for the multiples of five print “Buzz”. For numbers which are multiples of both three and five
    print “FizzBuzz”."""
    t = []
    for i in range(1, 101):
        if i % 15 == 0: t.append("fizzbuzz")
        elif i % 5 == 0: t.append("buzz")
        elif i % 3 == 0: t.append("fizz")
        else: t.append(str(i))
    print(" ".join(t))


def reverse_text(text="5G TEST MOCY SZCZECIN"):
    """Enter a string and the program will reverse it and print it out."""
    if text == "5G TEST MOCY SZCZECIN":
        text = input("Enter text that you want to reverse:\n")
    letters = [letter for letter in text]
    letters.reverse()
    print("".join(letters))
    return "".join(letters)  # makes you able to reuse this code more easily


def count_vowels():
    """Enter a string and the program counts the number of vowels in the text. For added complexity have it report a sum
    of each vowel found."""
    vowels = {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0, "y": 0, "all": 0}
    text = input("Provide text to check for vowels or click enter. ")
    if text == "":
        text = """Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore 
        et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea
        commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla 
        pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est 
        laborum."""
    for letter in text:
        if letter in vowels.keys():
            vowels[letter] += 1
            vowels["all"] += 1
    print(f"""There are {vowels["all"]} vowels in the text, including:
    {vowels["a"]} a
    {vowels["e"]} e
    {vowels["i"]} i
    {vowels["u"]} u
    {vowels["y"]} y.""")


def is_it_palindrome():
    """Checks if the string entered by the user is a palindrome. That is that it reads the same forwards as
    backwards."""
    text = input("Enter text to check if it's a palindrome! ").lower().replace(" ", "")
    if text == reverse_text(text):
        print("IS a palindrome ♥")
    else:
        print("is NOT a palindrome.")


def count_words():
    """Counts the number of individual words in a string. For added complexity read these strings in from a text file
    and generate a summary."""
    dir_ = Path(r"D:\Files\Documents")
    filenames = ""  # TODO: make a list of filenames from dir_
    string = open(random.choice(fnmatch.filter(filenames, "*.txt")), encoding="utf-16").read()
    count = len(string.replace("\n", " ").replace("  ", " ").strip().split(" "))
    print(f"There are {count} words in the provided text file.")


def text_editor():
    """Notepad style application that can open, edit, and save text documents. Optional: Add syntax highlighting and
    other features."""
    pass


def rss_feed_creator():
    """Given a link to RSS/Atom Feed, get all posts and display them."""
    pass


def quote_tracker():
    """A program which can go out and check the current value of stocks for a list of symbols entered by the user.
    The user can set how often the stocks are checked. For CLI, show whether the stock has moved up or down. Optional:
    If GUI, the program can show green up and red down arrows to show which direction the stock value has moved."""
    pass


def guestbook():
    """ A simple application that allows people to add comments or write journal entries. It can allow comments or not
    and timestamps for all entries. Could also be made into a shout box. Optional: Deploy it on Google App Engine
    or Heroku or any other PaaS (if possible, of course)."""
    pass


def simple_cipher():
    """Vigenere / Vernam / Ceasar Ciphers - Functions for encrypting and decrypting data messages. Then send them to a
    friend."""
    pass


def regex_query_tool():
    """A tool that allows the user to enter a text string and then in a separate control enter a regex pattern.
    It will run the regular expression against the source text and return any matches or flag errors
    in the regular expression."""
    pass


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG, format="LOG: %(message)s")
    logging.info("Start of the program.")


    def log_check(message, function):
        logging.debug(message)
        time.sleep(0.5)
        function()
        time.sleep(1)


    # log_check("Fizz buzz result:", fizz_buzz)
    log_check("Reversing user text result:", reverse_text)
    # log_check("Vowels count result:", count_vowels)
    log_check("Palindrome check result:", is_it_palindrome)
    # log_check("Words count result:", count_words)  # NOT READY YET
    logging.info("End of the program.")
