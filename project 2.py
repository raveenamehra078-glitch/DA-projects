# DAY  4 !!!

# project 1

# pandas((pip install pandas )in terminal for installing pandas in vs code)


import pandas as pd
# df = pd.DataFrame([11,22,33], columns=['Col_Name'])
# print(df)

# print(type(df))

data={
    'Name': ['Harsh Yadav','Harsh','Anjali','Ranee','Raveena'],
    'Age': [16,17,18,19,55],
    'Salary':[90000,70000,50000,30000,-15000]
    }
df = pd.DataFrame(data)
#print(df)


# print(df.head(2))

#print(df.tail)
#print(df.shape)
#print(df.columns)
df.rename(columns={'Salary': 'Monthly_Salary'}, inplace=True)
# print(df)
#print(df.info())
#print(df.describe())

# df.to_csv('Test_data.csv',index=False)
# load_df=pd.read_csv('Test_data.csv')
# print(load_df)


# print(df[('Name')])
#print(df[('Name','Monthly_Salary')])

#print(df.loc[df.Name=='Harsh Yadav'])

# df_age_filter=df[df['Age']>=18]
# print(df_age_filter)

#print(df[(df['Age']>=18) &  (df['Monthly_Salary']>=50000)])

#print(df.where(df['Age']>=18))
# print(df.where(df['Age']>=18, other='Not Eligible'))

df['Team']=['CEO','HR','CTO',"DA",'Chef']
# print(df)

df['Bonus'] = df['Monthly_Salary']*0.20
#print(df)

df.loc[len(df)]=['Yash',21,21000,'IT',2000]
#print(df)

df.loc[0, 'Monthly_Salary']=100000
#print(df)

df.loc[df.Name=='Raveena','Monthly_Salary']=-30000
#print(df)

df= df.drop(df[df.Name == 'Yash'].index)
df.drop(1,axis=0)
#print(df)

df.drop('Bonus',axis=1, inplace=True)
#print(df)

df.rename(columns={'Monthly_Salary':'Salary'},inplace=True)
# df.sort_values('Salary')
#print(df)

#df.sort_values('Salary')

df['DOJ']=['2024-01-01','2024-01-15','2024-03-28','2024-03-03','2024-03-28']
#print(df)

#print(df['DOJ'].dtype)
df['DOJ']= pd.to_datetime(df['DOJ'])
df['Month']=df['DOJ'].dt.month

#print(df)

# print(df['DOJ'].dtype)

#df['DOJ']= pd.Timedelta(days=90)

#Handling Missing Values

#print(df)

#print(df.isnull())

# print(df.loc[df.Name=='Risabh','Salary'] = np.nan)

# print(df.isnull())

# print(df.isnull().sum())

# print(df.fillna(0))

# print(df.loc[df.Name=='Risabh','Salary'] = 30000)

#print(df['Month'].value_counts())

#print(df[df['Month']==1].value_counts())

# project 2


#numpy
#matplotlib
#seaborn

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
#1. Numpy - Create random data
np.random.seed(42)
data = np.random.randn(100)
df = pd.DataFrame({
    'Values':data,
    'category':np.random.choice(['A','B','C'],size=100)
})
print("First 5 rows of DataFrame:")
print(df.head())

#3.Matplotlib - Basic Plot
plt.figure(figsize=(6,4))
plt.plot(df['Values'], label='Values')
plt.title("Matplotlib Line Plot")
plt.xlabel("Index")
plt.ylabel("Values")
plt.legend()
plt.show()

#4. Seaborn - Advanced Visualization
plt.figure(figsize=(6,4))
sns.displot(df['Values'], kde=True)
plt.title("Seaborn Histogram with KDE")
plt.show()

#5. Seaborn - Boxplot by category
plt.figure(figsize=(6,4))
sns.boxplot(x='Category',y='Values', data=df)
plt.title("Boxplot by Category")
plt.show()


# project 3
import seaborn as sns 
import matplotlib.pyplot as plt
import numpy as np

data=[11,14,33,44,55,67,11,23,34,65,64,44,44,65,56,12,23,43,69,1,2,34,45]
plot=['histogram','KERNAL_DENSITY']
for plots in plot:
    if plots =='Histogram':
        sns.histplot(data)
        plt.title("Histogram chart")
        plt.show()
    elif plots =='KERNAL_DENSITY':
        sns.kdeplot(data)
        plt.title("KERNAL_DENSITY")
        plt.show()

data=[11,14,33,44,55,67,11,23,34,65,64,44,44,65,56,12,23,43,69,1,2,34,45]
plot=['histogram','KERNAL_DENSITY']
for plots in plot:
    if plots =='Histogram':
        sns.histplot(data)
        plt.title("Histogram chart")
        plt.show()
    elif plots =='KERNAL_DENSITY':
        sns.kdeplot(data)
        plt.title("KERNAL_DENSITY")
        plt.show()
data1=[11,14,33,44,55,67,11,23,34,65,64,44,44,65,56,12,23,43,69,1,2,34,45]
data2=[11,14,3,14,25,67,31,23,64,65,64,84,44,65,56,0,23,43,69,1,2,34,45]
data3=[11,14,3,4,5,67,31,3,64,5,4,84,44,65,56,0,23,43,69,1,2,34,45]
group=[data1,data2,data3]
sns.violinplot(data=group)
plt.title("example of violin plot")
plt.show()

#project 4
# ==============================
# IMPORT LIBRARIES
# ==============================
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Seaborn style
sns.set()

# ==============================
# NUMPY (Numerical Operations)
# ==============================
print("----- NUMPY -----")

arr = np.array([10, 20, 30, 40, 50])
print("Array:", arr)

print("Mean:", np.mean(arr))
print("Sum:", np.sum(arr))
print("Max:", np.max(arr))
print("Min:", np.min(arr))

arr2 = np.arange(1, 10).reshape(3, 3)
print("2D Array:\n", arr2)

# ==============================
# PANDAS (Data Handling)
# ==============================
print("\n----- PANDAS -----")

data = {
    "Name": ["A", "B", "C", "D", "E"],
    "Marks": [85, 90, 78, 92, 88],
    "Age": [20, 21, 19, 22, 20]
}

df = pd.DataFrame(data)

print("DataFrame:\n", df)

print("\nDescribe:\n", df.describe())

# ==============================
# SEABORN VISUALIZATION
# ==============================
print("\n----- SEABORN -----")

# Line Plot
plt.figure()
sns.lineplot(x="Name", y="Marks", data=df)
plt.title("Marks Line Chart")
plt.show()

# Bar Plot
plt.figure()
sns.barplot(x="Name", y="Marks", data=df)
plt.title("Marks Bar Chart")
plt.show()

# Scatter Plot
plt.figure()
sns.scatterplot(x="Age", y="Marks", data=df)
plt.title("Age vs Marks")
plt.show()

# Histogram
plt.figure()
sns.histplot(df["Marks"], kde=True)
plt.title("Marks Distribution")
plt.show()

# Box Plot
plt.figure()
sns.boxplot(x="Marks", data=df)
plt.title("Box Plot of Marks")
plt.show()

# ==============================
# HEATMAP (Correlation)
# ==============================
plt.figure()
corr = df.corr(numeric_only=True)
sns.heatmap(corr, annot=True)
plt.title("Correlation Heatmap")
plt.show()

# project 5
# ==============================
# IMPORT LIBRARIES
# ==============================
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# ==============================
# NUMPY (Numerical Operations)
# ==============================
print("----- NUMPY -----")

# Create array
arr = np.array([10, 20, 30, 40, 50])
print("Array:", arr)

# Basic operations
print("Mean:", np.mean(arr))
print("Sum:", np.sum(arr))
print("Max:", np.max(arr))
print("Min:", np.min(arr))

# Reshape array
arr2 = np.arange(1, 10).reshape(3, 3)
print("2D Array:\n", arr2)

# ==============================
# PANDAS (Data Handling)
# ==============================
print("\n----- PANDAS -----")

# Create DataFrame
data = {
    "Name": ["A", "B", "C", "D", "E"],
    "Marks": [85, 90, 78, 92, 88],
    "Age": [20, 21, 19, 22, 20]
}

df = pd.DataFrame(data)

# Display data
print("DataFrame:\n", df)

# Basic operations
print("\nHead:\n", df.head())
print("\nInfo:")
print(df.info())

print("\nDescribe:\n", df.describe())

# Filtering
print("\nStudents with Marks > 85:\n", df[df["Marks"] > 85])

# Add new column
df["Grade"] = ["B", "A", "C", "A", "B"]
print("\nUpdated DataFrame:\n", df)

# ==============================
# MATPLOTLIB (Visualization)
# ==============================
print("\n----- MATPLOTLIB -----")

# Line Plot
plt.figure()
plt.plot(df["Name"], df["Marks"])
plt.title("Marks Line Chart")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.show()

# Bar Chart
plt.figure()
plt.bar(df["Name"], df["Marks"])
plt.title("Marks Bar Chart")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.show()

# Scatter Plot
plt.figure()
plt.scatter(df["Age"], df["Marks"])
plt.title("Age vs Marks")
plt.xlabel("Age")
plt.ylabel("Marks")
plt.show()

# Histogram
plt.figure()
plt.hist(df["Marks"])
plt.title("Marks Distribution")
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.show()

# project 6

import seaborn as sns
import matplotlib.pyplot as plt 
import pandas as pd
data={'advertisement':[1,2,3,4,6,7,9,10],
     'sales':[5,8,7,8,10,11,12,22],
     'temerature':[22,21,33,35,36,37,39,40]}
df=pd.DataFrame(data)
sns.scatterplot(x="advertisement",y="sales",data=df)
plt.show()

sns.scatterplot(x="advertisement",y="sales",data=df)
plt.title("advertisement and sales scattering chart")
plt.show()
data={'advertisement':[1,2,3,4,6,7,9,10],
     'sales':[5,8,7,8,10,11,12,22],
     'temerature':[22,21,33,35,16,21,20,20]}
coorelation_matrix=df.corr()
sns.heatmap(coorelation_matrix,annot=True,cmap='coolwarm',fmt='.2f')
plt.show()