# Reading a csv

import pandas as pd

dataset = pd.read_csv("https://raw.githubusercontent.com/amankharwal/Website-data/master/articles.csv", encoding='latin1')
#print(dataset.head())

dataset["Number of Words"] = dataset["Article"].apply(lambda n: len(n.split()))
print(dataset.head())

# pandas library doesn't have method for counting words in text
# find length of text by splitting complete text
# now count no of words in column