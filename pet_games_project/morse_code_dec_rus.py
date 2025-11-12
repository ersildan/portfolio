d = {
     ".-": "А", "-...": "Б", ".--": "В", "--.": "Г", "-..": "Д", ".": "Е",
     "...-": "Ж", "--..": "З", "..": "И", ".---": "Й", "-.-": "К", ".-..": "Л",
     "--": "М", "-.": "Н", "---": "О", ".--.": "П", ".-.": "Р", "...": "С",
     "-": "Т", "..-": "У", "..-.": "Ф", "....": "Х", "-.-.": "Ц", "---.": "Ч",
     "----": "Ш", "--.-": "Щ", ".--.-": "Ъ", "-.--": "Ы", "-..-": "Ь",
     "...-...": "Э", "..--": "Ю", ".-.-": "Я", "-...-": " ",
     }

print()
print('Write the text in Morse code to decipher into Russian.'
      '\nType exit to exit the program.')

while True:
    try:
        text = input()
        if text == 'exit':
            break
        print()
        print(f"Transcript: {''.join([d[letter] for letter in text.split()]).title()}")
        print('Type "exit" to exit the program.')
    except:
        print("Use only Morse code.")
