class LeftParagraph:
    def __init__(self, width):
        self.width = width
        self.line = ''

    def add_word(self, word):
        if len(self.line) + len(word) > self.width:
            print(self.line)
            self.line = word
        else:
            self.line += ' ' + word

    def end(self):
        print(self.line)


class RightParagraph:
    def __init__(self, width):
        self.width = width
        self.line = ''

    def add_word(self, word):
        if len(self.line) + len(word) > self.width:
            print(self.line.rjust(self.width))
            self.line = word
        else:
            self.line += ' ' + word

    def end(self):
        print(self.line.rjust(self.width))


lp = LeftParagraph(8)
lp.add_word('abc')
lp.add_word('defg')
lp.add_word('hi')
lp.add_word('jklmnopq')
lp.add_word('r')
lp.add_word('stuv')
lp.end()
print()
rp = RightParagraph(8)
rp.add_word('abc')
rp.add_word('defg')
rp.add_word('hi')
rp.add_word('jklmnopq')
rp.add_word('r')
rp.add_word('stuv')
rp.end()
print()
