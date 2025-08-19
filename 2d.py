import pandas as pd

data = [
    [101, 'Alice', 85],
    [102, 'Bob', 90],
    [103, 'Charlie', 78]
]

df = pd.DataFrame(data, columns=['ID', 'Name', 'Score'])

print(df)
