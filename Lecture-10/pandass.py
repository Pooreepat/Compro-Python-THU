import pandas as pd

data = {'Name': ['Alice','Bob','Charlie'],
        'Age': [25,30,35],
        'City': ['New York','LosAngeles','Chicago']
        }

df = pd.DataFrame(data)
print("DataFreame:\n", df)

average_age = df['Age'].mean()
print("\nAverage Age:", average_age)

filtered_df = df[df['Age']>28]
print("\nFiltered DataFrame (Age > 28):\n", filtered_df)

df['Salary'] = [50000,60000,70000]
print("\nDataFreme with Salary colum:\n", df)