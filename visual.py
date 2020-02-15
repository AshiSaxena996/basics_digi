from reader import count_each_vowel
import matplotlib.pyplot as plt


def vowels_bar(file):
    results= count_each_vowel(file)
    print(results)
    x= results.keys()
    h= results.values()
    c= ['blue', 'yellow', 'black']   #color for regions can be given aswell by color=c in param....not necessary but
    plt.bar(x,h,color=c)           #x,h are required param...h is height= y axis
    plt.show()

file = 'data/Richardson_Clarissa.txt'
vowels_bar(file)