class Note:
    def __init__(self, height, long=False):
        self.height = height
        self.long = long

    def play(self):
        if self.long:
            print(self.height + '-о')
        else:
            print(self.height)

    def __str__(self):
        if self.long:
            return self.height + '-о'
        else:
            return self.height

note = Note('до')
note.play()  # Вывод: до
note = Note('ре', True)
note.play()  # Вывод: ре-о
note = Note('ми')
note.play()  # Вывод: ми
note = Note('фа', True)
note.play()  # Вывод: фа-о
note = Note('соль')
note.play()  # Вывод: соль
note = Note('ля', True)
note.play()  # Вывод: ля-о
note = Note('си')
note.play()  # Вывод: си


