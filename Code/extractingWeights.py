import pandas as pd

df = pd.read_csv("masterFile.csv")


dfWeighted = pd.DataFrame(columns=['Destination', 'Source', 'Weight', 'Label'])
# x = df.loc[(df['Destination'] == 756080279056293888) & (df['Source'] == 2467062384)] 
# print(x.index.tolist()) #prints the index of the above match

i = 0	#acting as an index for dfWeighted
for index, row in df.iterrows():
	if (index % 100000 == 0):
		dfWeighted.to_csv('masterFileWeighted.csv', index=False)
	
	if (index == 0): #If the index of the masterFile is 0, I copy the first row to the weightedFile
		dfWeighted.at[index, 'Destination'] = row['Destination']
		dfWeighted.at[index, 'Source'] = row['Source']
		dfWeighted.at[index, 'Label'] = row['Label']
		dfWeighted.at[index, 'Weight'] = 1
		i += 1	

	else:
		x = dfWeighted.loc[(dfWeighted['Destination'] == row['Destination']) & (dfWeighted['Source'] == row['Source'])] #If a match exists

		xList = x.index.tolist()

		if (len(xList) == 0): # If no matches were found, a new entry is created.
			dfWeighted.at[i, 'Destination'] = row['Destination']
			dfWeighted.at[i, 'Source'] = row['Source']
			dfWeighted.at[i, 'Label'] = row['Label']
			dfWeighted.at[i, 'Weight'] = 1
			i += 1

		else: #change only relevant columns
			dfWeighted.at[xList[0], 'Label'] += ' ' + row['Label']
			dfWeighted.at[xList[0], 'Weight'] += 1

dfWeighted.to_csv('masterFileWeighted.csv', index=False)
















