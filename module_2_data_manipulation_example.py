
import pandas as pd

# Sample DataFrame
data = {'Name': ['John', 'Anna', 'Peter', 'Linda'],
        'Age': [28, 34, 29, 32],
        'City': ['New York', 'Paris', 'Berlin', 'London']}
df = pd.DataFrame(data)

# Display the DataFrame
print(df)

# Basic Data Filtering
filtered_df = df[df['Age'] > 30]
print(filtered_df)
