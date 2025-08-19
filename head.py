import pandas as pd

data = {
    'ID': [101, 102, 103, 104, 105, 106],
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva', 'Frank'],
    'Score': [85, 90, 78, 88, 92, 75]
}

df = pd.DataFrame(data)

print("Head of DataFrame:")
print(df.head(3))

print("\nTail of DataFrame:")

print(df.tail(3))

