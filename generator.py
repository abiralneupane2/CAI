import random

class Generator:
    _score = 0
    _REMARKS = {
        'positive' : ['Very good!', 'Well done!', 'Correct'],
        'negative' : ['Try Again', 'Nice Try'],
        }

    def __init__(self, a, b, o):

        '''
        a, b are two integers
        o may be any value from operators enum
        '''

        self.a = a
        self.b = b
        self.o = o

    def result(self):

        '''
        returns result according to selection of o
        '''


        match self.o:
            case 'ADD':
                return self.a + self.b
            case 'MUL':
                return self.a * self.b
            case 'DIV':
                try:
                    return self.a / self.b
                except ZeroDivisionError:
                    return 'inf'
            case 'SUB':
                return a > b ? self.a - self.b : self.b - self.a

    def __str__(self):

        '''
        String representation according to requirement.
        '''

        match self.o:
            case 'ADD':
                return str(self.a) + " added to " + str(self.b) + " is "
            case 'MUL':
                return str(self.a) + " times " + str(self.b) + " is "
            case 'DIV':
                return str(self.a) + " over " + str(self.b) + " is "
            case 'SUB':
                return str(self.a) + " subracted from " + str(self.b) + " is "


    def get_positive_remarks(self):
        '''
        random positive remarks from _REMARKS dictionary
        '''

        return random.choice(self._REMARKS['positive'])
    
    def get_negative_remarks(self):
        '''
        random negative remarks from _REMARKS dictionary
        '''
        return random.choice(self._REMARKS['negative'])

    def add_score(self):
        self._score = self._score + 1

    def get_score(self):
        return self._score
    
    


            

    