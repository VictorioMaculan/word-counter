import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter


def count_words(path: str):
    '''
    Count the most used words in a text file.
    '''
    with open(path) as file:
        file_content = file.read()
    file_content = file_content.split()
    
    words = dict(Counter(file_content))
    words_series = pd.Series(words)
    words_series.sort_values(ascending=False, inplace=True)
    
    return words_series


if __name__ == "__main__":
    ipsum = count_words('lorem_ipsum.txt').head(5)

    graph = plt.bar(ipsum.index, 
                    height=ipsum.values)
    plt.bar_label(graph, 
                  labels=ipsum.values)
    
    plt.show()
    