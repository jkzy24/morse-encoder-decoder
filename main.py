import json
import os
import time

# Create morse code dictionary by reading from json file
with open("morse-code.json", "r") as file:
    morse_dict = json.load(file)


# Write functions
def clear():
    """ Clears the console """
    os.system('clear')


def get_latin_char(morse_char):
    """ Returns corresponding latin character from morse character entered"""
    for latin_char in morse_dict:
        if morse_dict[latin_char] == morse_char:
            return latin_char


def word_to_morse(word):
    """ Takes an English word as input and returns word in morse code as string """
    chars = list(word)
    morse_chars = []
    for char in chars:
        try:
            morse_char = morse_dict[f"{char}"]
            morse_chars.append(morse_char)
        except KeyError:
            print(f"The character {char} is not supported in morse code. Restarting in 5 secs.")
            time.sleep(5)
            start()
    morse_word = " ".join(morse_chars)
    return morse_word


def morse_to_word(morse_word):
    """ Takes a morse word as input and returns word in latin alphabets as string """
    morse_chars = morse_word.split(" ")
    latin_chars = [get_latin_char(morse_char) for morse_char in morse_chars]
    try:
        latin_word = "".join(latin_chars)
        return latin_word
    except TypeError:
        print("This is not morse code. Please enter appropriate morse code. Restarting in 5 secs.")
        time.sleep(5)
        start()



def encoder(text):
    """ Encodes sentence in latin alphabets into morse code """
    # Parse text string into individual words as a list
    words = text.split(" ")

    # Create sentence in morse code after encrypting it word by word
    morse_sentence = [word_to_morse(word) for word in words]
    joined_morse = " / ".join(morse_sentence)

    # Return encoded morse code
    print(f"Your morse code is: {joined_morse}")


def decoder(text):
    """ Decodes morse code into English sentence"""
    # Parse text string into individual morse words as a list
    morse_words = text.split(" / ")

    # Create sentence in latin alphabets after decrypting it word by word
    latin_sentence = [morse_to_word(morse_word) for morse_word in morse_words]
    joined_latin = " ".join(latin_sentence)

    # Return decoded morse code
    print(f"Your decrypted morse code reads: {joined_latin}")


def start():
    """ Starts the Morse encoding or decoding programme """
    clear()

    decision = input("Do you want to encode or decode morse code? (Type encode or decode)\n").lower()
    if decision != "decode" and decision != "encode":
        print("Sorry, we don't offer this functionality. Restarting in 5 secs.")
        time.sleep(5)
        start()

    text = input(f"What do you want to {decision} in morse code?\n").lower()

    if decision == "encode":
        encoder(text)

    elif decision == "decode":
        decoder(text)

    continue_using = input("Do you want to continue? (Type yes or no)\n").lower()
    if continue_using == 'yes':
        start()
    else:
        print("Thanks for using. See you soon!")
        quit()


start()
