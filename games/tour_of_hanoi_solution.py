class Tower:

    def __init__(self):
        self.counter = 0

    def hanoi(self, n, a, c, b):
        if n == 1: 
            self.counter += 1
            print('{0}->{1}'.format(a, b))
        else:
            self.hanoi(n -1, a, b, c)
            self.hanoi(1, a, c, b)
            self.hanoi(n-1, b, c, a)


print("displays the solution of tower of hanoi problem")

def take_input():
    while True:
        try:
            inp = int(input("Size of tower"))
        except:
            print("Enter suitable value")
    tower = Tower()
    tower.hanoi(inp,"a", "c", "b")

if __name__ == '__main__':
    take_input()