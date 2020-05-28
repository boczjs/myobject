'''
@Author: boczjs
@Date: 2020-05-27 20:24:58
@LastEditTime: 2020-05-27 21:23:59
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \myobject\dash_test.py
'''

import dash
import dash_core_components as dcc 
import dash_html_components as html 

external_stylesheets=['https://codepen.io/chriddyp/pen/bWLwgP.css']

app=dash.Dash(__name__,external_stylesheets=external_stylesheets)
colors={'background':'#111111','text':'red'}

app.layout=html.Div(style={'backgroundColor':colors['background']},children=[html.H1(children='Hello Dash',
    style={'textAlign':'center','color':colors['text']}),

    html.Div(children='''
        Dash:A web appliction framework for Python''',style={
            'textAlign':'center',
            'color':colors['text']
        }),
        dcc.Graph(
            id='example-graph',
            figure={
                'data':[
                    {'x':[1,2,3],'y':[4,1,2],'type':'bar','name':'SF'},
                    {'x':[1,2,3],'y':[2,4,5],'type':'bar','name':u'Montreal'},
                ],
                'layout':{
                    'title':'Dash Data Visualization',
                    'plot_bgcolor':colors['background'],
                    'paper_bgcolor':colors['background'],
                    'font':{'color':colors['text']}
                }
            }
        )
        ])


if __name__=='__main__':
    app.run_server(debug=True)

