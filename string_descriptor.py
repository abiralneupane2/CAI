from collections import Counter
import re
import pandas as pd
import matplotlib.pyplot as plt

def get_tuple(text):
    text = re.findall("[a-zA-Z]", text.lower())
    return Counter(text)

def main():
    inp = input("Enter a string:\n")
    cntr = get_tuple(inp)
    print(list(cntr.items()))
    if len(cntr) == 26:
        print("All alphabets are present") 
    else:
        print("All alphabets are not present\n")
    print("Descriptive statistics\n")
    s  = pd.Series(cntr,index=cntr.keys())
    print(s)
    print("Total unique characters", s.count())
    print("Total characters", s.sum())
    print("Median of character count", s.median())
    print("Mean character count", s.mean())
    print("Standard deviation", s.std())
    print("Most occuring ", s.idxmax(), s.max())




    s.plot.bar(xlabel="letter", ylabel="count")
    plt.show()


    

if __name__ == "__main__":
    main()