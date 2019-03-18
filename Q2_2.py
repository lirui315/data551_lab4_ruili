
import plotly.plotly as py
import plotly.graph_objs as go
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
df = pd.read_csv("subset.csv")



countries = ['Australia','Austria','Belgium','Brazil','Canada','Chile','Colombia',
                                           'Cyprus','Denmark','Estonia','Finland','France','Germany','Greece','India',
                                           'Ireland','Italy','Japan','Korea','Kuwait','Latvia','Luxembourg','Netherlands',
                                           'New Zealand','Norway','Portugal', 'Saudi Arabia','Slovak Republic', 'Slovenia',
                                           'Spain', 'Sweden', 'Switzerland','Taiwan','Thailand','United Arab Emirates',
                                           'United Kingdom','United States']
dfcountry = df[df['donor'].isin(countries)]
dfcountry.columns = ['Country', 'Amount','Purpose']


# Question 2 (b)
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    dcc.Dropdown(
        id='my-dropdown',
        options=[
            {'label': i, 'value': i} for i in dfcountry.Country.unique()
        ],
        value='Canada'
    ),
    dcc.Graph(id='bar_plot')
])

@app.callback(
    dash.dependencies.Output('bar_plot', 'figure'),
    [dash.dependencies.Input('my-dropdown', 'value')])

def barplot(country):
    name = dfcountry[dfcountry['Country']==country]

    return {
        'data': [
            go.Bar(
                x=name['Purpose'],
                y=name['Amount'],
                textposition='outside',
                textfont=dict(
                size=12,
                color='black'
                ),
                marker=dict(
                color='rgb(100, 170, 187)')
                )
        ],
        'layout': go.Layout(
            xaxis=dict(
            tickangle=0,
            tickfont=dict(
                size=10.5
                ),
            tickwidth=1.2
            ),
            title='Donation Amount by Purposes',
            titlefont=dict(
                size=16
                )
        )
}

if __name__ == '__main__':
    app.run_server(debug=True)