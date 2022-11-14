

import pandas as pd
# file_name = pd.read_csv("file.csv") format of read_csv
data = pd.read_csv("transaction.csv")
data = pd.read_csv("transaction.csv",sep=";")

#summery of the data

data.info()

#Playing around with variables

var = {'name':'Dee', 'location':'South Africa'}

#Working with calculations

#Defining variables

CostPerItem = 11.73
SellingPricePerItem = 21.11
NumberOfItemsPurchased = 6

#Mathematical Operations on Tableau

ProfitPerItem = 21.11 - 11.73
ProfitPerItem = SellingPricePerItem - CostPerItem

ProfitPerTransaction = NumberOfItemsPurchased * ProfitPerItem
CostPerTransaction = NumberOfItemsPurchased * CostPerItem
SellingPricePerTransaction = NumberOfItemsPurchased * SellingPricePerItem


#CostPerTransaction Column Calculation

#CostPerTransaction = CostPerItem * NumberOfPurchases

#variable  = dataframe['column_name']


CostPerItem = data['CostPerItem']
NumberOfItemsPurchased = data['NumberOfItemsPurchased']
CostPerTransaction = CostPerItem * NumberOfItemsPurchased

#adding a new column to a data frame

data['CostPerTransaction'] = data['CostPerItem'] * data['NumberOfItemsPurchased']
#or
data['CostPerTransaction'] = CostPerTransaction

#SalesPerTransactions

data['SalesPerTransactions'] = data['SellingPricePerItem'] * data['NumberOfItemsPurchased']

#Profit calculations = sales- cost

data['ProfitPerTransaction'] = data['SalesPerTransactions'] - data['CostPerTransaction']

#markup calculations = (sales- cost) / cost

data['Markup'] = (data['SalesPerTransactions'] - data['CostPerTransaction']) / data['CostPerTransaction']

data['Markup'] = (data['ProfitPerTransaction']) / data['CostPerTransaction']

#Rounding Marking

roundmarkup = round(data['Markup'],2)

data['Markup'] = round(data['Markup'],2)

#combining data fields

my_name = 'Andrew'+'Aliseiko'
my_date = 'Day'+'-'+'Month'+'-'+'Year'

# my_date = data['Day'] + '-' 

#checking columns data type
print(data['Day'].dtype)

#change columns type
day = data['Day'].astype(str)
year = data['Year'].astype(str)

print(day.dtype)
print(year.dtype)

my_date = day + '-' + data['Month'] + '-' + year
data['date'] = my_date

#using iloc to view specific columns/rows

data.iloc[0] #view the row with index = 0
data.iloc[0:3] #first 3 rows
data.iloc[-5:] #last 5 rows

data.head(5) #brings in first 5 rows

data.iloc[:,2] #brings in all rows on the 2nd colum

data.iloc[4,2] #brings in 4th row, 2nd column

#using split to split the client_keyword field
#new_var = column.str.split('sep' , expand = True)

split_col = data['ClientKeywords'].str.split(',' , expand = True)

#creating new columns for the split columns in Client Keywords

data['ClientAge'] = split_col[0]
data['ClientType'] = split_col[1]
data['LenghtOfContract'] = split_col[2]

#using the replace function

data['ClientAge'] = data['ClientAge'].str.replace('[', '') 
data['LenghtOfContract'] = data['LenghtOfContract'].str.replace(']', '')
# data.drop(columns = ['ClienAge'], axis = 1, inplace=True) # deleting a column in dataframe

#using the lower function to change item to lowercase

data['ItemDescription'] = data['ItemDescription'].str.lower()

#how to merge files 

#bringing in a new dataset

seasons = pd.read_csv("2.4 value_inc_seasons.csv",sep=";")

#emerging files: merge_df = pd.merge(df_old, df_new, on = 'key')

data = pd.merge(data, seasons, on = 'Month')

#dropping columns

# df - df.drop('columnname', axis = 1) 1 - column 0 - row

data = data.drop('ClientKeywords' , axis = 1)
data = data.drop('Day' , axis = 1)

data = data.drop(['Year', 'Month'], axis = 1)


#export into CSV

data.to_csv('ValueInc_Cleaned.csv', index = False)