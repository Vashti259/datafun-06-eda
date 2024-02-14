# This is a Datafun-06-eda Notebook Project
This is a Datafun-06-eda Notebook Project
Documentation: README.md
Notebook: vashti_eda.ipynb
February 14,2024

# Overview
A Data Analyst will be able to use  some very important tools such as GitHub, Jupyter,
some Python Library tools plus Git, and more with VSCODE installed on their machine.

# Dependencies
jupyterlab
pandas
matplotlib
seaborn

# Data Acquisition
## Load the dataset into a pandas DataFrame - adjust this process for your custom data
df = sns.load_dataset('iris')
# Inspect first rows of the DataFrame
print(df.head())

Data Distribution for Numerical Columns
# Inspect histogram by numerical column
df['sepal_length'].hist()
# Inspect histograms for all numerical columns
df.hist()
# Show all plots
plt.show()

Initial Data Distribution for Categorical Columns
# Inspect value counts for all categorical columns
for col in df.select_dtypes(include=['object', 'category']).columns:
# Display count plot
    sns.countplot(x=col, data=df)
    plt.title(f'Distribution of {col}')
    plt.show()

   jupyter Notebook / Python cell example:
# Inspect value counts for all categorical columns
for col in df.select_dtypes(include=['object', 'category']).columns:
    # Display count plot
    sns.countplot(x=col, data=df)
    plt.title(distribution of {col}')
    plt.show()

# Show all plots
plt.show()
df.hist()


