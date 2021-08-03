# -*- coding: utf-8 -*-
"""
Created on Sun Aug  1 12:27:21 2021

@author: daryl
"""
#Importing Libraries
import pandas as pd
import plotly.express as px
import dash
import dash_table
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

app = dash.Dash(__name__)
app.title = "India Population"

# =============================================================================
# Reading Dataset and Grouping by States
df = pd.read_csv('./data/india-districts-census-2011.csv')
dff = df.groupby('State name', as_index=False)[['Population', 'Male', 'Female']].sum()
# =============================================================================

# =============================================================================
# Creating App Layout
app.layout = html.Div([
    # Creating Datatable
    html.Div([
        dash_table.DataTable(
            id='datatable_id',
            data=dff.to_dict('records'),
            columns=[
                {"name": i, "id": i, "deletable": False, "selectable": False} for i in dff.columns
            ],
            editable=False,
            filter_action="native",
            sort_action="native",
            sort_mode="multi",
            row_selectable="multi",
            row_deletable=False,
            selected_rows=[],
            page_action="native",
            page_current= 0,
            page_size= 10,
            style_cell_conditional=[
                {'if': {'column_id': 'State name'},
                 'width': '25%', 'textAlign': 'center'},
                {'if': {'column_id': 'Population'},
                 'width': '25%', 'textAlign': 'center'},
                {'if': {'column_id': 'Male'},
                 'width': '25%', 'textAlign': 'center'},
                {'if': {'column_id': 'Female'},
                 'width': '25%', 'textAlign': 'center'},
            ],
        ),
    ], className='row'),

    # Creating Bar and Pie charts
    html.Div([
        html.Div([
            html.H3('District-wise Population'),
            dcc.Graph(id='linechart'),
        ],className='six columns'),

        html.Div([
            html.H3('State-wise Population'),
            dcc.Graph(id='piechart'),
        ],className='six columns'),

    ], className='row center'),
])
# =============================================================================


# =============================================================================
# Creating Callback and Plotting Graph data
@app.callback(
    [Output('piechart', 'figure'),
     Output('linechart', 'figure')],
    [Input('datatable_id', 'selected_rows')]
)

def update_data(chosen_rows):
    if len(chosen_rows)==0:
        df_filterd = df[df['District name'].isin(list(df.loc[df["State name"] == df["State name"][0]]["District name"]))]
    else:
        df_filterd = dff[dff.index.isin(chosen_rows)]

    pie_chart=px.pie(
            data_frame=df_filterd,
            names='State name',
            values="Population",
            hole=.3,
            labels={'State':'State'}
            )

    #extract list of chosen States
    list_chosen_states=df_filterd['State name'].tolist()
    df_line = df[df['State name'].isin(list_chosen_states)]

    line_chart = px.bar(
            data_frame=df_line,
            x="District name",
            y=["Male", "Female"],
            labels={'District name':'Districts', 'Population':'Population'},
            )
    line_chart.update_layout(uirevision='foo')

    return (pie_chart,line_chart)
# =============================================================================

if __name__ == '__main__':
    app.run_server(debug=True)