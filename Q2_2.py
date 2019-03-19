
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
        id='dropdown',
        options=[
            {'label': i, 'value': i} for i in dfcountry.Country.unique()
        ],
        value='Canada'
    ),
    dcc.Graph(id='bar_plot')
])

@app.callback(
    dash.dependencies.Output('bar_plot', 'figure'),
    [dash.dependencies.Input('dropdown', 'value')])

def barplot(country):
    name = dfcountry[dfcountry['Country']==country]

    return {
        'data': [
            go.Bar(
                x=name['Purpose'],
                y=name['Amount'],
                opacity=0.5,
                marker=dict(
                color='rgb(100, 170, 187)')
                )
        ],
        'layout': go.Layout(
            xaxis=dict(
            tickangle=0,
            tickfont=dict(
                size=11
                ),
            tickwidth=1
            )
        )
}

if __name__ == '__main__':
    app.run_server(debug=True)