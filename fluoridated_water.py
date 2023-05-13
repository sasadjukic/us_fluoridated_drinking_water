
import pandas as pd 
from data import usa_data 

def get_fluoridated_water_dataframe(data: pd.DataFrame) -> pd.DataFrame:
    '''get the right survey question'''
    poverty = data[data['question'] == 'Population served by community water systems that receive fluoridated drinking water']
    return poverty 

def get_us_states_only(data: pd.DataFrame) -> pd.DataFrame:
    '''get only 50 US states + DC'''
    states = data.loc[
                        (data['locationdesc'] != 'United States') &
                        (data['locationdesc'] != 'Puerto Rico') &
                        (data['locationdesc'] != 'Guam') &
                        (data['locationdesc'] != 'Virgin Islands')
                    ]

    return states

def get_us_nationwide(data: pd.DataFrame) -> pd.DataFrame:

    nationwide = data[data['locationdesc'] == 'United States']
    return nationwide

def get_flo_water_for_2018(poverty: pd.DataFrame) -> pd.DataFrame:
    '''get poverty data for 2018 (the last year with info)'''
    fw_2018 = poverty[poverty['yearstart'] == 2018]
    return fw_2018

flo_water = get_fluoridated_water_dataframe(usa_data)
states = get_us_states_only(flo_water)
flo_water_2019 = get_flo_water_for_2018(states)
nationwide = flo_water_2019[['yearstart', 'locationabbr', 'datavaluealt']]
usa = get_us_nationwide(flo_water)

