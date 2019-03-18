
import plotly.plotly as py
import plotly.graph_objs as go
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
df = pd.read_csv("subset.csv")


app = dash.Dash()
# Question 2 (a)
by_purpose = df.groupby('coalesced_purpose_name').aggregate({"commitment_amount_usd_constant":"sum"})
by_purpose.reset_index(inplace=True)
by_purpose.columns = ['Purpose','Amount']


app.layout = html.Div([
    dcc.Graph(
        id='life-exp-vs-gdp',
        figure={
            'data' :[
                go.Bar(
                    x=by_purpose['Purpose'],
                    y=by_purpose['Amount'],
                    text=by_purpose['Amount'],
                    textposition = 'outside',
                    textfont={'size':14},
                    opacity=0.8,
                    marker={
                        'color':'rgb(100,170,187)',
                        'line': {'width': 0.5, 'color': 'white'}
                            }
                        )
                    ]
                }
            )
    ])

if __name__ == '__main__':
    app.run_server(debug=True)