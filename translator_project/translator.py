from deep_translator import GoogleTranslator

def translate_from_file():
    translated= GoogleTranslator(source='auto'),
    target('english').translate_file('path/to/your/file')

def translate_from_text():
    
    user_text= str(input('insert your text: '))
    translated= GoogleTranslator(source='auto',
                                 target='en').translate(user_text)
    print(translated)

input_from_user= str(input("what do you want to do? a) Translate from file or b)insert text?  "))

if input_from_user == 'a':
    translate_from_file()
elif input_from_user == 'b':
    translate_from_text()