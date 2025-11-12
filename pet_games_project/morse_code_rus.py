d = {' ': '-...-', 'Ё': '.', 'А': '.-', 'Б': '-...', 'В': '.--', 'Г': '--.',
     'Д': '-..', 'Е': '.', 'Ж': '...-', 'З': '--..', 'И': '..', 'Й': '.---',
     'К': '-.-', 'Л': '.-..', 'М': '--', 'Н': '-.', 'О': '---', 'П': '.--.',
     'Р': '.-.', 'С': '...', 'Т': '-', 'У': '..-', 'Ф': '..-.', 'Х': '....',
     'Ц': '-.-.', 'Ч': '---.', 'Ш': '----', 'Щ': '--.-', 'Ъ': '--.--',
     'Ы': '-.--', 'Ь': '-..-', 'Э': '..-..', 'Ю': '..--', 'Я': '.-.-',
     '!': '', '?': '', '@': '', '#': '', '$': '', ',': ''
     }

print('ENG: Write a text in Russian to encrypt it in Morse Code.'
      '\nType exit to exit the program.')

while True:
    try:
        text = input()
        if text == 'exit':
            break
        print()
        print(f"Transcript: {' '.join([d[l] for l in text.upper()])}")
        print('Type "exit" to exit the program.')
    except KeyError:
        (print('Use only Russian letters.'))
