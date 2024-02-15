## This is a Datafun-06-eda Notebook Project
 Documentation: README.md
Notebook: vashti_eda.ipynb

## Overview

 A Data Analyst will be able to use  some very important tools such as GitHub, 
 Jupyter, some Python Library tools plus Git, 
 and more with VSCODE installed on their machine.

 ## Import Dependencies
 
 import matplotlib.pyplot as plt
 import pandas as pd
 import seaborn as sns

  ## Data Acquisition
  
 #Load the dataset into a pandas DataFrame - adjust this process for your custom data
df = sns.load_dataset('iris')
 Inspect first rows of the DataFrame
print(df.head())
 Inspect histogram by numerical column
df['sepal_length'].hist()
 Inspect histograms for all numerical columns
df.hist()
Show all plots
plt.show()
















