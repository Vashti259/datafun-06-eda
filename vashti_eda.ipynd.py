Name: Vashti Gambol
Project:  06 datafun eda with Jupyter Notebook
February 14th 2024
# Overview
A Data Analyst will be able to use some very important tools such as GitHub, Jupyter, Pandas Seaborn, Git,
and more. With VSCODE installed on their machine, they can do great things.

# Terminal Commands
py -m venv .venv
.\.venv\Scripts\Activate.ps1
py -m pip install jupyterlab pandas matplotlib seaborn
py -m pip freeze > requirements.txt

 # Import dependencies
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy

# Data Acquisition
# Load the dataset into a pandas DataFrame - adjust this process for your custom data
df = sns.load_dataset('iris')
df =pd. Dataframe (top20, columns= 'word', 'count'
def
  0  romeo   315
  1  thou    278
  2  juliet  190
  3  thy     170
  4 capulet  163
  5 nurse    149
  6 love     148
  7 thee     138
  8 lady     117 
  9 shall    110
 10 friar    105
 11 come      94
 12 mercutio  88
 13 lawrence  82
 14     good  80  axes=df.plot.bar(x='word , y='count', legend = Fasle)
 15  benvolio 79  import matplotlib.pyplot as plt
 16  tybalt   79  plt.gcf().tight_layout() 
 17  enter    75
 18     go    75
 19  night    73
                   
