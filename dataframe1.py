import pandas as pd

# Read data from CSV file and create a DataFrame
df = pd.read_csv('DATA.csv')

# Display a list of all columns
column_list = df.columns.tolist()
print("List of all columns:")
print(column_list)

# Display data in the order of columns present
df_reordered = df[column_list]
print("Data in order of columns present:")
print(df_reordered)

print("HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHhead 15 rows")
print("start ______________________________________________________")
print(df.head(15)) #starting


print("END ______________________________________________________")
print(df.tail(15)) #ending
print("count ______________________________________________________")
print(df.count())



# Fill NaN values with the mean of each column
df_filled = df.fillna(df.mean())

# Display the DataFrame with filled NaN values
print(df_filled)