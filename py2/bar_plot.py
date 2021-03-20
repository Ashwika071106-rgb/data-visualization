import pandas as pd
import plotly.express as px

df = pd.read_csv("py2/data.csv")

fig = px.bar(df,x = "Country", y = "InternetUsers")
fig.show()

