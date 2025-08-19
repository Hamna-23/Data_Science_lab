import pandas as pd

data = {
    'ID': [101, 102, 103],
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Score': [85, 90, 78]
}

df = pd.DataFrame(data)

print(df)
