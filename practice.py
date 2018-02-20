##README
##
##*Pandas libray is used in this program*
##
##This will take input as a csv file, in same format that was given in
##the problem statement and with the same file name. In case other file is to
##be given as input then that can be changed in the very first line of the code.
##
##As sample output it will print the total number and names of unique persons
##and will also return a csv file ('Unique_IDs.csv') with the same info
##of them. Also, to identify entries from the main dataset, there original row
##number is also given in the updated list.
##
##Output will show a warning about changing values in dataframe but thats ok.

File_name = 'Deduplication Problem - Sample Dataset.csv'
Output_File = 'Unique_IDs.csv'

import pandas as pd

df = pd.read_csv(File_name)

def match(name1,name2):
	arr1=[0 for i in range(len(name1))]
	arr2=[0 for i in range(len(name2))]

	for i in range(len(name1)):
		for j in range(len(name2)):
			if name1[i]==name2[j]:
				arr1[i],arr2[j]=[1,1]
	for i in range(len(name1)):
		for j in range(len(name2)):
			if len(name1[i])<3 or len(name2[j])<3:
				if name1[i][0]==name2[j][0] and arr1[i]+arr2[j]<1:
					arr1[i],arr2[j]=[1,1]
	if sum(arr1)==len(arr1) or sum(arr2)==len(arr2):
		#print(name1,name2,'same')
		return 0
	else:
		#print(name1,name2,'not same')
		return 1

df.sort_values(['dob','gn'],inplace =True)
row_number = [i for i in range(1,len(df)+1)]
df['row']=row_number

first = []
last = []

for i in df.index:
    first.append(df['fn'][i].split())
    last.append(df['ln'][i].split())

full_name = []

for i in range(len(first)):
    full_name.append(first[i]+last[i])

df['name']=full_name
df['unique']=[1 for i in range(len(df))]

count = 0

for i in df.index:
    if df['unique'][i]== 0:
        continue

    count+=1
    for j in range(i+1,len(df)):
        if df['unique'][j]== 0:
            continue
        if df['dob'][j]!=df['dob'][i] or df['gn'][j]!=df['gn'][i]:
            break
        df['unique'][j]=match(df['name'][i],df['name'][j])
    print(df['fn'][i]+" "+df['ln'][i])


for i in df.index:
    if df['unique'][i]==0:
        df.drop(i,inplace=True)
del df['unique'],df['name']

df.sort_values('row',inplace=True)
df.set_index('row',inplace=True)
df.to_csv(Output_File)



##SAMPLE OUTPUT
##
##
##Output of this code will be
##
##WILLIAM SMITH JR
##WILLIAM ROTHMEYER JR
##WILLIAM ASBY JR
##WILLIAM SALTER JR
##ROY MICHAELSON JR
##HARRIET FUNARO JONES
##DARL GRIFFIN JR
##CLIFFORD GRIFFIN JR
##CLARENCE GRIFFIN JR
##HAROLD MUSTAPHA JR
##HAROLD HOUGHTON JR
##HAROLD MELVIN JR
##HAROLD CHAVAS JR
##HAROLD MICHAELSON JR
##HAROLD SMITH JR
##HAROLD FAGEN JR
##GEORGE FAGEN JR
##DARH GRIFFIN JR
##WILLIAM BLAND JR
##RONALD CLARK
##DONALD CLARK
##ROY MICHAELSON JR
##ROBERT MICHAELSON JR
##BOB MICHAELSON JR
##JACK MICHAELSON JR
##HAROLD LARSON JR
##JOHN CLARK
##DARL GRIFFIN JR
##OWEN MUSTAPHA JR
##OWAN MUSTAPHA JR
##ADDISON GALETICH JR
##JOHN CLARK
##JOHN MICHAELSON JR
##ROY MICHAELSON JR
##JOHN LIND JR
##JOHN CAIN JR
##WILLIAM BLAND JR
##WILLIAM SHAFFER JR
##WILLIAM BLAND III
##BILL BLAND JR
##JOHN MICHAELSON JR
##JOHN MICHAELSON JR
##JAMES MICHAELSON JR
##JACK MICHAELSON JR
##ADDISON J HANNA
##WILLIAM BLAND JR
##WILLIAM SHAFFER JR
##THOMAS DUNCAN JR
##ROY CARLSON JR
##RON CARLSON JR
##ROY DUNCAN JR
##ROY MICHAELSON
##LAWRENCE HOUGHTON JR
##LAWRENCE LIND JR
##KENNETH LIND JR
