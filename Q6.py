while True:
    try:
        new_text = ""
        first_text = input('Введите ваш текст: ')
        uslovie = True
        for bukva in first_text:
            if bukva == ' ':
                new_text += ' '
                continue
            if uslovie:
                new_text += bukva.upper()
                uslovie = False
            else:
                new_text += bukva.lower()
                uslovie = True
        print(new_text)
    except EOFError:
        break
    break
