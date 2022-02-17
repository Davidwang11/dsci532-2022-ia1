from dash import Dash, html, dcc, Input, Output
import altair as alt
from vega_datasets import data


# Read in global data
stocks = data.stocks()

# Setup app and layout/frontend
app = Dash(__name__,  external_stylesheets=['https://codepen.io/chriddyp/pen/bWLwgP.css'])
app.layout = html.Div([
    html.Iframe(
        id='line',
        style={'border-width': '0', 'width': '100%', 'height': '400px'}),
    dcc.Dropdown(
        id='symbol-widget',
        value='AAPL',  
        options=[{'label': col, 'value': col} for col in stocks['symbol'].unique()])])

# Set up callbacks/backend
@app.callback(
    Output('line', 'srcDoc'),
    Input('symbol-widget', 'value'))
def plot_altair(symbol):
    chart = alt.Chart(stocks[stocks['symbol']==symbol]).mark_line().encode(
        x='date',
        y='price',
        tooltip='symbol').interactive()
    return chart.to_html()

if __name__ == '__main__':
    app.run_server(debug=True)