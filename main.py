more = True


morse_code_dict = {
 "A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".", "F": "..-.", "G": "--.", "H": "....", "I": "..",
 "J": ".---", "K": "-.-", "L": ".-..", "M": "--", "N": "-.", "O": "---", "P": ".--.", "Q": "--.-", "R": ".-.", "S": "...",
 "T": "-", "U": "..-", "V": "...-", "W": ".--", "X": "-..-", "Y": "-.--", "Z": "--..", "0": "-----", "1": ".----",
 "2": "..---", "3": "...--", "4": "....-", "5": ".....", "6": "-....", "7": "--...", "8": "---..", "9": "----.",
 '.': ".-.-.-", ',': "--..--", '?': "..--..", "'": ".----.", '!': "-.-.--", ':': "---...", ';': "-.-.-.",
 '-': "-....-", '"': ".-..-.", '/': "-..-.", '(': "-.--.", ')': "-.--.-", '&': ".-...", '@': ".--.-.",
 '$': "...-..-", ' ': '/'
}


def convert_to_morse(text):
    morse_cod = [morse_code_dict[word.upper()] for word in text]
    code = ' '.join(morse_cod)
    print(f'Morse code = {code}')


def morse_to_normal(code):
    decode_text = []
    morse = code.split(' ')
    for mcode in morse:
        for key, value in morse_code_dict.items():
            if mcode == value:
                decode_text.append(key)
    final_code = ''.join(decode_text)
    print(f'Normal Text = {final_code}')


print('#---------------------Welcome to morse code converter-----------------------------#')

type_conversion = input('Enter 1 to convert normal text to morse code\n'
                        'Enter 2 to convert morse code to normal text\n'
                        'Any other answer than 1 or 2 will prompt the game to quit\n')
while more:
    correct = True
    if type_conversion == '1':
        normal_text = input('Please enter the text to be converted to morse code\n')
        convert_to_morse(normal_text)
    elif type_conversion == '2':
        morse_code = input('Please enter the text to be converted to morse code\n')
        morse_to_normal(morse_code)
    else:
        correct = False
        more = False
    while correct:
        from_ = 'Normal Text'
        to_ = 'Morse Code'
        if type_conversion == '2':
            from_ = 'Morse Code'
            to_ = 'Normal Text'
        cont = input(f'Would you like to convert {from_} to {to_}? If yes then enter "y" or else enter "n"\n')
        if cont.lower() == 'n':
            more = False
            correct = False
        elif cont.lower() == 'y':
            more = True
            correct = False
        else:
            print('You have provided wrong input. Please provide valid input')
