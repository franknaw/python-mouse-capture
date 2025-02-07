
# import libraries for data manipulation
import numpy as np
import pandas as pd

# import libraries for data visualization
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('./foodhub_order.csv')

# drive.mount('/content/drive')

# print(f"Tail: {df.tail()}")
# print(f"iloc: {df.iloc[:5]}")

# View first 5 rows
# print(f"Head: {data.head(5)}")

# 1 How many rows and columns are present
print(f"1:\n There are {data.shape[0]} rows and {data.shape[1]} columns.")

# 2 What are the datatypes of the different columns
print(f"2:\n {data.dtypes}")
# print(f"2. foo {data.info(verbose=False, show_counts=False)}")
# print(f"2. foo {data.info(verbose=True, show_counts=True)}")


# print(f" {data.isnull().any(axis = 1).sum()}")

# missing_values = data.isnull()
# print(f"3:\n {missing_values.sum()}")
print(f"3:\n {data.isnull().sum()}")
# Replace values
# data["Gender"].fillna('', inplace=True)

# Check the statistical summary of the data. What is the minimum, average, and maximum time it takes for food to be prepared once an order is placed?
foo = data[['food_preparation_time']].agg(['min', 'mean', 'max'])
print(f"4:\n {foo}")

# `axis=0`: Sums the column values
# `axis=1`: Sums the row values
# print(data[["rating"]].sum(axis=0))
ratings = (data[["rating"]] == "Not given").sum(axis=0)
print(f"5:\n {ratings}")

# goo = data.loc[data['rating'] == "Not given", 'rating'].sum()
# print(goo)


# fee = data.query("rating == 'Not given'").sum()
# print(fee)

# fee = data.groupby('rating')['Not given'].sum()[1]
# print(fee)






# foo = data.set_index("food_preparation_time").groupby(data.index).agg(['min', 'max', 'mean'])
# print (foo)
#
# foo2 = (data.set_index("food_preparation_time")
#            .select_dtypes(np.number)
#            .stack()
#            .groupby(level=0)
#            .agg(['min','max','mean']))
# print (foo2)
