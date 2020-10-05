import pandas as pd
import plotly.express as px
df=pd.read_csv("C:/Users/priyanka/Documents/My Received Files/covid-data-for-class.csv")
fig=px.bar(df,x='Deaths**', y='Active Cases*')
fig.show()
