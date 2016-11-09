#start with imports
import pandas as pd
from matplotlib import pyplot as plt

#create empty list of years
years=[]

#use a loop to search in lines of our file ELECTION_ID
#create newvar to split each line in python
#year is going to be equal to the first variable in each line
#years is going to be the list of every year
for line in open("ELECTION_ID"):
    newvar=line.strip().split()
    year=newvar[0]
    years.append(year)

#create an empty list for files
files = []

#create a list of the .csv files, naming them with every element in the list of years (years)
for y in years:
    files.append(y + ".csv")

#create an empty list for dataframes
dataframes=[]

#use a loop to search for every element in files
#use a loop to search for every element in years
#pandas
for f in files:
    for y in years:
        header = pd.read_csv(f, nrows = 1).dropna(axis = 1)
        d = header.iloc[0].to_dict()
        df = pd.read_csv(f, index_col = 0, thousands = ",", skiprows = [1])
        df.rename(inplace = True, columns = d) # rename to democrat/republican
        df.dropna(inplace = True, axis = 1)    # drop empty columns
        df["Year"] = y
        dataframes.append(df[["Democratic", "Republican", "Total Votes Cast", "Year"]])

#create republican share column in dataframe
m= pd.concat(dataframes)
m["Republican Share"]=m["Republican"]/m["Total Votes Cast"]


#Create the graph
m[m.index == "Accomack County"].plot(x="Year", y="Republican Share", kind="hist").get_figure().savefig('accomack_rep.png')
