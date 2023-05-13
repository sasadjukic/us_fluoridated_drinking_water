
import pandas as pd 
import matplotlib.pyplot as plt 
from fluoridated_water import usa 

def get_nationwide_averages(data: pd.DataFrame) -> pd.DataFrame:
    '''sort dataframe by years in ascending order'''

    return data.sort_values(by=['yearstart'])

def display_nationwide_averages_by_year(us_data: pd.DataFrame) -> None:
    '''display line chart of usa avregaes in fluoridated water in community water systems'''

    year = us_data['yearstart'].tolist()
    values = us_data['datavaluealt'].tolist()

    color = '#e9d28d'
    bg_color = '#2c3333'
    line_color = '#ffffff'

    fig, ax = plt.subplots()
    plt.plot(
             year, 
             values, 
             marker='o',
             linestyle = 'solid',
             color = line_color
            )

    fig.patch.set_facecolor(bg_color)
    ax.set_facecolor(bg_color)

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_color(color)
    ax.spines['left'].set_color(color)

    plt.xticks(color=color)
    plt.yticks(color=color)

    ax.set_xticks([2012, 2014, 2016, 2018])
    plt.ylim(71, 75)

    for index, value in enumerate(values):
        plt.text(
            index,
            value,
            f'{str(value)}%',
            ha = 'center',
            position = ((2*index)+2012, value+0.15),
            fontweight = 'bold',
            fontsize = 12.5,
            color = color
        )

    plt.show()


sorted_values_by_year = get_nationwide_averages(usa)
display_nationwide_averages_by_year(sorted_values_by_year)