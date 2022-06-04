import random
import time
import _thread

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

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
    
    def set_ans(self, ans):
        self._ans = ans
    
    def get_ans(self):
        return self._ans
    
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
    options = q.opts()
    print(*options, sep="\t")
    try:
        # _thread.start_new_thread(input_timer, (interval,))
        ans = int(input())
        if ans > 0 and ans <= len(options):
            q.set_ans(options[ans-1])
        else:
            raise ValueError
        
    except ValueError as e:
        print("wrong input")
        q.set_ans(None)
    print(q.get_remarks())
    return q

def display_summary(summary):
    x = []
    right = []
    wrong = []
    fig, ax = plt.subplots()
    ind = np.arange(len(summary))
    width = 0.35
    for name in summary:
        x.append(name)
        t, f = 0, 0
        for q in summary[name]:
            if q.get_ans() == q.result():
                t+=1
            else:
                f+=1
        right.append(t)
        wrong.append(f)
    ax.bar(ind, right, width, bottom=0, label='right')
    ax.bar(ind + width, wrong, width, bottom=0, label='wrong')
    ax.set_title('Scores by user')
    ax.set_xticks(ind + width / 2, labels=x)
    ax.legend()
    ax.autoscale_view()
    plt.show()
            
            

            

def main():
    itvl, total_questions = 0, 3
    summary = {}
    while True:
        print(summary)
        display_summary(summary)
        u = get_user_info()
        if u == "exit":
            break
        print(f"Each question must be answered in {itvl} seconds.\nTotal questions {total_questions}\nGame will start in..")
        for i in range(3):
            print(3-i)
            time.sleep(1)
        for i in range(total_questions):
            g = game(interval = 3)
            try:
                summary[u].append(g)
            except:
                summary[u] = [g,]
    
    
    


    

if __name__ == "__main__":
    main()

    
