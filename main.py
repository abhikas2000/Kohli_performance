import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df=pd.read_csv("dataset.csv")


def show_pie_plot(df,key):
    count=df[key].value_counts()
    counts_values=count.values
    counts_labels=count.index
    fig=plt.figure(figsize=(10,7))
    plt.pie(counts_values,labels=counts_labels)
    plt.show()

#--------------------Number of matches he has played at different positions
positions=df["Pos"].unique()
print(positions)

df["Pos"]=df["Pos"].map({    #to change numbers to text
    1.0:"Batting at 1",
    2.0:"Batting at 2",
    3.0:"Batting at 3",
    4.0:"Batting at 4",
    5.0:"Batting at 5",
    6.0:"Batting at 6",
    7.0:"Batting at 7"
})


show_pie_plot(df,"Pos")

#--------------------Number of matches against different opposition
show_pie_plot(df,"Opposition")


#--------------------Number of matches at different grounds
show_pie_plot(df,"Ground")

#--------------------Total 6s at different positions
gb=df.groupby("Pos")["6s"].sum()
print(gb)
values=gb.values
label=gb.index
plt.figure(figsize=(10,7))
plt.bar(label,values,color="green",width=0.4)
plt.show()

#--------------------Total runs scored with different countries
gb=df.groupby("Opposition")["Runs"].sum()
print(gb)
values=gb.values
label=gb.index
plt.figure(figsize=(10,7))
plt.bar(label,values,color="blue",width=0.4)
plt.show()

#--------------------Number of centuries scored by him in 1st and 2nd innings
centuries=df.query("Runs>=100").groupby("Inns")["Runs"].count()
print(centuries)

values=centuries.values
label=centuries.index
plt.figure(figsize=(10,7))
plt.pie(values,labels=label)
plt.show()

#--------------------Calculate the dismissal of kohli
show_pie_plot(df,"Dismissal")


#--------------------max runs against every countries
max_runs=df.groupby("Opposition")["Runs"].max()
value=max_runs.values
label=max_runs.index
plt.figure(figsize=(11,8))
plt.bar(label,value,color="#f6546a",width=0.3)
plt.show()