__author__ = 'vitor'


class PhoneConverter():
    _str_input = ""
    _str_converted = ""
    alphabet_dict = {'A': '2',
                 'B': '2',
                 'C': '2',
                 'D': '3',
                 'E': '3',
                 'F': '3',
                 'G': '4',
                 'H': '4',
                 'I': '4',
                 'J': '5',
                 'K': '5',
                 'L': '5',
                 'M': '6',
                 'N': '6',
                 'O': '6',
                 'P': '7',
                 'Q': '7',
                 'R': '7',
                 'S': '7',
                 'T': '8',
                 'U': '8',
                 'V': '8',
                 'W': '9',
                 'X': '9',
                 'Y': '9',
                 'Z': '9',
                 '-': '-',
                 ' ': ' ',
                 '0': '0',
                 '1': '1',
                 '2': '2',
                 '3': '3',
                 '4': '4',
                 '5': '5',
                 '6': '6',
                 '7': '7',
                 '8': '8',
                 '9': '9',
                 '\n': ''
                 }

    def __init__(self, phone=None):
        if phone is not None:
            self.str_input = phone

    #Limpa a variável que contém a conversão e seta a variável de entrada
    def set_input(self, phone):
        self._str_converted = ""
        self._str_input = phone

    def convert(self, phone=None):
        self.str_converted = ""

        if phone is not None:
            self.str_input = phone

        for char in self.str_input:
            self.str_converted += self.find_char(char)

        return self.str_converted


    # Procura o caracter no dicionário e caso não existe retorna a string #ERROR e imprime um aviso
    def find_char(self, char):
        try:
            return self.alphabet_dict[char.upper()]
        except KeyError:
            print('\nALERT: char ' + char + ' does not exist in dictionary.')
            return '#ERROR'










