from bs4 import BeautifulSoup

import requests
#part 1
r  = requests.get("https://python.org/")
soup = BeautifulSoup(r.text,"html.parser")
text=soup.get_text()
print(text)

#part 2

list_of_words=text.split(" ")

#part 3

set_words=set(list_of_words)
set_remove=(['are','is','of', 'and', 'if'])
set_final=set_words.difference(set_remove)
print(set_final)

#part 4

pro=list_of_words.count("programmers.")
pandas=list_of_words.count("Pandas")
prdt=list_of_words.count("product")
py=list_of_words.count("Python")


#part 5

import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

objects = ('programmers', 'pandas', 'product', 'python')
y_part = np.arange(len(objects))
occurence = [pro,pandas,prdt,py]

plt.bar(y_part, occurence, align='center', alpha=0.5)
plt.xticks(y_part, objects)
plt.ylabel('Usage')
plt.title('words occurence')

plt.show()












