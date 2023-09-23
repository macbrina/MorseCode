MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..',
    'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', '1': '.----',
    '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    '0': '-----', '.': '.-.-.-', ',': '--..--', '?': '..--..', '!': '-.-.--',
}


def morse_to_text(morse_code):
    morse_to_char = {morse: char for char, morse in MORSE_CODE_DICT.items()}
    words = morse_code.split('   ')
    word_text = ''

    for word in words:
        word_strings = word.split()

        for i, word_string in enumerate(word_strings):
            if i == 0:
                word_text += morse_to_char.get(word_string, '').upper()
            elif i != 0:
                word_text += morse_to_char.get(word_string, '').lower()
            else:
                print(f"Skipping invalid Morse code: {word_string}")
        word_text += ' '
    return word_text.strip()


def text_to_morse(text):
    text_strings = ''
    for char in text:
        if char in MORSE_CODE_DICT:
            text_strings += MORSE_CODE_DICT[char] + '  '
        else:
            text_strings += ' '
    return text_strings.strip()


system_on = True

while system_on:
    choice = input(
        "Enter 1 to convert string to morse code or 2 to convert morse code to string or 'exit' to stop: ").lower()
    if choice == "1":
        letters = input("Enter the string to convert: ").upper()
        new_text = text_to_morse(letters)
        print(new_text)
    elif choice == "2":
        morse_codes = input("Enter the morse code to convert: ")
        new_code = morse_to_text(morse_codes)
        print(new_code)
    elif choice == "exit":
        print("Thank you for using. Goodbye")
        exit()
    else:
        print("You entered an invalid number, please try again")
