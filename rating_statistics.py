import statistics
import collections

import matplotlib.pyplot as plt

def take_input(name):
    ratings = []
    for i in range(20):
        while True:
            try:
                inp = int(input(f"Product {i}: "))
                if inp <= 5 and inp >= 0:
                    ratings.append(inp)
                    break
                else:
                    raise Exception("Rating must be between 0 and 5.")
            except Exception as e:
                print(str(e))

    return ratings

def display_statistics(data):
    for std in data:
        print(f"Statistics of rating by {data[std]}:\n\n")
        print("Mean:", statistics.mean(data[std]))
        print("Median:", statistics.median(data[std]))
        print("Mode:", statistics.mode(data[std]))
        print("Variance:", statistics.variance(data[std]))
        print("Standard deviation:", statistics.stdev(data[std]))
        print("Minimum rating:", min(data[std]), f"for product_{data[std].index(min(data[std]))}")
        print("Maximum rating:", max(data[std]), f"for product_{data[std].index(max(data[std]))}")
        print("Frequencies of rating:")

        c = collections.Counter(data[std])
        print("rating", "frequency")
        for key, value in c.items():
            print(key, '\t', value)
        
def draw_bar_diagram(data, name):
    c = collections.Counter(data[name])
    plt.bar(c.keys(), c.values())
    plt.show()
         
        

if __name__ == '__main__':
    data = {}
    name = input("Enter your name: ")
    data[name] = take_input(name)
    display_statistics(data)
    draw_bar_diagram(data, name)