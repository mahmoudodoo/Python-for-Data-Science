
# Basic Data Analysis with Pandas
import pandas as pd

# Creating a simple DataFrame
data = {'Name': ['John', 'Anna', 'Peter', 'Linda'],
        'Age': [28, 34, 29, 32],
        'City': ['New York', 'Paris', 'Berlin', 'London']}
df = pd.DataFrame(data)

# Display the DataFrame
print(df)

# Basic statistics
print("\nBasic Statistics:")
print(df.describe())
