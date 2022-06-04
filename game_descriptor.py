import random
import time
import _thread

OPERATIONS = {
    0: 'ADD',
    1: 'MUL',
    2: 'DIV',
    3: 'SUB'
}



_REMARKS = {
        'positive' : ['Very good!', 'Well done!', 'Correct'],
        'negative' : ['Try Again', 'Nice Try'],
        }

class Generator:
    _ans = None

    def __init__(self, a, b, o):

        '''
        a, b are two integers
        o may be any value from operations enum
        '''

        self.a = a
        self.b = b
        self.o = o

    def result(self):

        '''
        returns result according to selection of o
        '''


        if self.o == 'ADD':
            return self.a + self.b
        elif self.o == 'MUL':
            return self.a * self.b
        elif self.o == 'DIV':
            try:
                return int(self.a / self.b)
            except ZeroDivisionError:
                return 'inf'
        elif self.o == 'SUB':
            return self.a - self.b
        else:
            raise ValueError("Invalid operation type")

    def __str__(self):

        '''
        String representation according to requirement.
        '''

        if self.o == 'ADD':
            return str(self.a) + " added to " + str(self.b) + " is "
        elif self.o == 'MUL':
            return str(self.a) + " times " + str(self.b) + " is "
        elif self.o == 'DIV':
            return str(self.a) + " over " + str(self.b) + " is "
        elif self.o == 'SUB':
            return str(self.a) + " subracted from " + str(self.b) + " is "
        else:
            raise ValueError("Invalid operation type")

    
    def opts(self):
        r = self.result()
        opts = [r]
        if self.o == 'SUB':
            a, b = -50, 50
        elif self.o == 'MUL':
            a, b = 0, 400
        else:
            a, b = 0, 50
        
        while len(opts)<3:
            opts.append(random.randint(a, b))
            list(set(opts))
        random.shuffle(opts)
        return opts


    
    def get_remarks(self):
        '''
        random positive or negative remarks from _REMARKS dictionary
        '''
        if self.result() == self._ans:
            
            return random.choice(_REMARKS['positive'])
        return random.choice(_REMARKS['negative'])
    
    def ans(self, ans):
        self._ans = ans
    
def input_timer(interval=3):
    time.sleep(3)
    raise ValueError

def get_user_info():
    name = input("Enter your name: ")
    return name

def game(interval):
    a, b, c = random.sample(range(0, 20), 3)
    q = Generator(a, b, OPERATIONS[c % len(OPERATIONS)])
    print(q)
    print(*q.opts(), sep="\t")
    try:
        _thread.start_new_thread(input_timer, (interval,))
        ans = int(input())
        if ans > 0 and ans < 5:
            q.ans(q.result()[ans])
        else:
            raise ValueError
        
    except ValueError as e:
        print("wrong input")
        q.ans(None)
    print(q.get_remarks())
    return q

def main():
    itvl, total_questions = 3, 10
    summary = []
    u = get_user_info()
    print(f"Each question must be answered in {itvl} seconds.\nTotal questions {total_questions}\nGame will start in..")
    for i in range(3):
        print(3-i)
        time.sleep(1)
    for i in range(total_questions):
        time.sleep(itvl)
        g = game(interval = 3)
        summary.append(g)
    
    


    

if __name__ == "__main__":
    main()

    
