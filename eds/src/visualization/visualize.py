import pandas as pd
import numpy as np

import dash
dash.__version__
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

import sys
sys.path.insert(1, '../data/')
from get_data import get_john_hopkins_data
from process_JH_data import store_relational_JH_data

sys.path.insert(1, '../features/')
from build_features import pd_result_large_final

import plotly.graph_objects as go

import os



print(os.getcwd())

get_john_hopkins_data()
store_relational_JH_data()
pd_result_large_final()

df_input_large = pd.read_csv('../../data/processed/COVID_final_set.csv', sep = ';')

fig = go.Figure()

app = dash.Dash()
app.layout = html.Div([
    
    dcc.Markdown('''
                 
    # Applied Data Science on COVID-19 data
    '''),
    
    dcc.Markdown('''
    ## Multi-select country for visualization
    '''),
    
    dcc.Dropdown(
        id = 'country_drop_down',
        options = [{'label': each, 'value': each} for each in df_input_large['country'].unique()],
        value = ['US', 'Germany', 'Italy'],  #Pre selected countries
        multi = True
        ),
    
    dcc.Markdown('''
                ## Select Timeline of confirmed COVID-19 cases or the approximated doubling time
    '''),
    
    dcc.Dropdown(
        id = 'doubling_time',
        options = [
            {'label': 'Timeline confirmed', 'value' : 'confirmed'},
            {'label': 'Timeline confirmed Filtered', 'value': 'confirmed_filtered'},
            {'label': 'Timeline doubling rate', 'value': 'confirmed_DR'},
            {'label': 'Timeline doubling rate filtered', 'value': 'confirmed_filtered_DR'},
        ],
        value = 'confirmed',
        multi = False
        ),
    
    dcc.Graph(figure = fig, id = 'main_window_slope')
  ])
                
@app.callback(
    Output('main_window_slope', 'figure'),
    [Input('country_drop_down', 'value'),
    Input('doubling_time', 'value')])

def update_figure(country_list, show_doubling):
    
    if 'DR' in show_doubling:
        my_yaxis = {'type': "log",
                    'title': 'Approximated doubling rate over 3 days'
                    }
    else:
        my_yaxis = {'type': "log",
                    'title': 'confirmed infected people (source: john hopkins csse, log-scale'
                    }
    
    traces = []
    for each in country_list:
        
        df_plot = df_input_large[df_input_large['country'] == each]
        
        if show_doubling == 'doubling_rate_filtered':
            df_plot = df_plot[['state','country','confirmed','confirmed_filtered','confirmed_DR','confirmed_filtered_DR','date']].groupby(['country','date']).agg(np.mean).reset_index()
        else:
            df_plot = df_plot[['state','country','confirmed','confirmed_filtered','confirmed_DR','confirmed_filtered_DR','date']].groupby(['country','date']).agg(np.sum).reset_index()
        
        
        traces.append(dict(x = df_plot.date,
                           y = df_plot[show_doubling],
                           mode = 'markers+lines',
                           opacity = 0.9,
                           name = each
                          )
                      )
    return {
        'data': traces,
        'layout': dict (
            width = 1280,
            height = 720,
            
            xaxis = {'title': 'Timeline',
                     'tickangle': -45,
                     'nticks': 20,
                     'tickfont': dict(size = 14, color = "#7f7f7f"),
                     },
            yaxis = my_yaxis
            )
        }

if __name__ =='__main__':
    
    app.run_server(debug = True, use_reloader = False)
    
    
    
    
            
