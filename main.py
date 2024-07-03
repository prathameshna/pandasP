import pandas as pd

# Create a dataframe
df = pd.DataFrame({'Name': ['John', 'Mary', 'Bob'], 'Age': [20, 25, 30]})

# Check if any value in the 'Age' column is greater than 25
print(df['Age'].any())

# Output: True


