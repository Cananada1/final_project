import dash
import dash_html_components as html
import dash_core_components as dcc
import plotly.graph_objs as go
import pandas as pd



############Read in the Federal Reserve Data from Local Host#####
df = pd.read_csv(r'C:\Python\Python Project\FREDData.csv')

##### Clean the Data (CPI Data starts too early)

rename_map = {
    'DATE':    'Date',
    'IRLTLT01USM156N':  '10_Year_Yield',
    'CPIAUCSL_PC1':  'Consumer Price Index'}

df.rename(columns=rename_map, inplace=True)

df = df[df["10_Year_Yield"] != '.']

######Create Line Chart ####
tenyear = go.Scatter(
        x = df['Date'],
        y = df['10_Year_Yield'],
        mode = 'lines',
        name = 'US 10yr Treasury Yield'


)
cpidata = go.Scatter(
    x = df['Date'],
    y = df['Consumer Price Index'],
    mode = 'lines',
    name = 'Consumer Price Index'
)

fullchart = [cpidata,tenyear]


mylayout = go.Layout(
    title='Inflation and Treasury Yields',
    xaxis={'title':'Time'},
    yaxis={'title':'Percent'}
    )

fig =go.Figure(data=fullchart, layout = mylayout)


######### Dash App ###########

app = dash.Dash()
server = app.server

app.layout = html.Div(children=[
    html.H1('Comparison of 10yr and CPI'),
    dcc.Graph(
        id='First Project',
        figure=fig
    )]
)

if __name__ == '__main__':
    app.run_server()
