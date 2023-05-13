
import pandas as pd 
import plotly.express as px 

from fluoridated_water import nationwide 

def display_fluoridated_water_map(nation: pd.DataFrame) -> None:
    '''display USA color map showing states and where they fit in the percentage range of fluoridated water system''' 
    fig = px.choropleth(
                        nation, 
                        locations='locationabbr',
                        locationmode='USA-states',
                        scope='usa',
                        color='datavaluealt',
                        range_color=[0, 100],
                        color_continuous_scale=['#ffffff', '#fdfdde', '#ece3b4', '#e9d28d', '#d7b54f', '#c88a31', '#925806']
          ).update_layout(
                        template='none',
                        plot_bgcolor='#2C3333',
                        paper_bgcolor = '#2C3333'
          )

    fig.show()

display_fluoridated_water_map(nationwide)