'''
@Author: boczjs
@Date: 2020-05-27 21:28:06
@LastEditTime: 2020-05-28 18:06:43
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \myobject\dash_table.py
'''
import dash
import dash_core_components as dcc 
import dash_html_components as html 
#from dashapp import app as application
import pandas as pd 

df=pd.read_excel('e:\python_test\wd191216.xlsx',sheet_name='Sheet1')

def generate_table(dataframe,max_rows=10):
    return html.Table([
        html.Thead(
            html.Tr([html.Th(col) for col in dataframe.columns])
        ),
        html.Tbody([
            html.Tr([
                html.Td(dataframe.iloc[i][col] for col in dataframe.columns)
                
            ]) for i in range(min(len(dataframe),max_rows))
        ])
    ])

external_stylesheets=['https://codepen.io/chriddyp/pen/bWLwgP.css']

app=dash.Dash(__name__,external_stylesheets=external_stylesheets)

app.layout=html.Div(children=[
    html.H4(children='US Agriculture Exports (2011)'),
    generate_table(df)
])
if __name__=='__main__':
    app.run_server(debug=True)