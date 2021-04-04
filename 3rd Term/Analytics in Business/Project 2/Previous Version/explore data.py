# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 18:07:23 2021

@author: Mary
topic: " explore data"
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import datetime

import numbers


##########################
##Fill in the 2017 April Data
##########################
def get_filed_2017_from_2016():
    turbine_telemetry_Qian = pd.read_csv('turbine_telemetry.csv', parse_dates=[0], index_col=0)
    turbine_telemetry_Qian = turbine_telemetry_Qian.reset_index()
    turbine_telemetry_Qian.Timestamp = pd.to_datetime(turbine_telemetry_Qian.Timestamp)
    turbine_telemetry_Qian['Year'] = turbine_telemetry_Qian.Timestamp.dt.year
    turbine_telemetry_Qian['Month'] = turbine_telemetry_Qian.Timestamp.dt.month
    turbine_telemetry_Qian['Day'] = turbine_telemetry_Qian.Timestamp.dt.day
    turbine_telemetry_Qian['Hour'] = turbine_telemetry_Qian.Timestamp.dt.hour
    turbine_telemetry_Qian['Minute'] = turbine_telemetry_Qian.Timestamp.dt.minute
    turbine_telemetry_Qian['Second'] = turbine_telemetry_Qian.Timestamp.dt.second
    
    
    grouped_df = turbine_telemetry_Qian.groupby(['Year','Month'])
    grouped_df = grouped_df.agg({'Day': 'nunique'})
    grouped_df = grouped_df.reset_index()
    location = grouped_df.Year == 2017
    grouped_df.loc[location]
    # The data in April is missing
    
    grouped_df = turbine_telemetry_Qian.groupby(['Year','Month','Day'])
    grouped_df = grouped_df.agg({'Hour': 'nunique'})
    grouped_df = grouped_df.reset_index()
    location = (grouped_df.Year == 2017) & (grouped_df.Month == 4)
    grouped_df.loc[location]
    # The data for April 3rd and April 24th are partially missing, and the data for April 4th to April 23 are entirely missing
    
    # Fill in the missing data for April 3th to April 24.
    # Replace the missing data in 2017 by data in 2016
    masks = (turbine_telemetry_Qian.Year == 2016) &  (turbine_telemetry_Qian.Month == 4) & (turbine_telemetry_Qian.Day.between(3, 24, inclusive=True))
    data_2016_for_replacement = turbine_telemetry_Qian.loc[masks]
    data_2016_for_replacement.Year = 2017
    data_2016_for_replacement.Timestamp = data_2016_for_replacement.Timestamp + pd.offsets.DateOffset(years=1)
    data_2016_for_replacement
    
    turbine_telemetry_filing_in_3_24 = turbine_telemetry_Qian.append(data_2016_for_replacement)
    turbine_telemetry_filing_in_3_24

    # reprint all the data from 2017
    tt_17  = turbine_telemetry_filing_in_3_24.copy()
    mask17 = (tt_17.Year == 2017)
    tt_17  = tt_17[mask17]
    
    tt17 = tt_17.copy()
    tt17 = tt17.reset_index()
    plot_filled_data = tt17.plot.scatter('Timestamp', 'Power_kw')


    return tt17



##############################
##Brin all to xx:00 second and take the mean values
##############################
# all the data from 2017


def isnumber(x):
    return isinstance(x, numbers.Number)

def not_number_to_nan(row):
    power = row.Power_kw
    if isnumber(power):
        return power
    else: 
        return np.nan

def get_all_zero_seconds_avg(tt17):

    tt_17 = tt17.copy()
    tt_17 = tt_17.reset_index()
    tt_17.plot.scatter('Timestamp', 'Power_kw')
        
    tt_17.Timestamp = tt_17.Timestamp.map(lambda x: x.replace(second=0))
    tt_17["Power_kw"] = tt_17.apply( not_number_to_nan, axis =1)
    
    #tt17_na_num = tt17_mean_data.isna().sum()

    
    tt17_mean_data = tt17.groupby("Timestamp").mean()
    
    return tt17_mean_data

#######################
## Main
#######################


tt = pd.read_csv('turbine_telemetry.csv', parse_dates=[0], index_col=0)

tt17 = get_filed_2017_from_2016()

tt17_mean_data = get_all_zero_seconds_avg(tt17)


###################################3
#### Q1
###################################

##Assumptions

turbines = 500
turbines_operating = 0.8 ## assumption

orkney_households = 9240

#tt = tt17_mean_data.copy()
#tt = tt.reset_index()


###################################3
####  1st way
###################################

def calcucate_curtailed_energy_setpoint_based(tt):

    turbine_telemetry_filter_wind_power = tt.copy()
    turbine_telemetry_filter_wind_power.loc[turbine_telemetry_filter_wind_power.Wind_ms >= 30, "Power_kw"] = 0

    max_setpoints_per_wind = turbine_telemetry_filter_wind_power.groupby('Wind_ms')['Setpoint_kw'].max()

    turbine_telemetry_filter_wind_power = turbine_telemetry_filter_wind_power.merge( max_setpoints_per_wind, on = "Wind_ms")

    turbine_telemetry_filter_wind_power = turbine_telemetry_filter_wind_power.rename(columns = {"Setpoint_kw_x": "Setpoint_kw", "Setpoint_kw_y": "Max_possible_setpoint" }) 

    turbine_telemetry_filter_wind_power["Setpoint_delta"] = turbine_telemetry_filter_wind_power["Max_possible_setpoint"] - turbine_telemetry_filter_wind_power["Setpoint_kw"]


    turbine_telemetry_filter_wind_power["Power_curtailed"] = turbine_telemetry_filter_wind_power["Setpoint_delta"]
    turbine_telemetry_filter_wind_power.loc[ turbine_telemetry_filter_wind_power.Setpoint_kw > turbine_telemetry_filter_wind_power.Power_kw , "Power_curtailed"] = 0

    total_curtailed_kwh = turbine_telemetry_filter_wind_power["Power_curtailed"].sum()/60

    total_curtailed_energy = turbines * turbines_operating * total_curtailed_kwh

    return total_curtailed_energy, turbine_telemetry_filter_wind_power




###################################3
#### 2nd way : curtailed = (possible power - island demand - export)*t
###################################

def get_wind_power_relation(tt):
    # how to figure out what's the the smallest speed necessary to produce power
    v_min = tt[(tt.loc[:, 'Power_kw'] >= 5.)].loc[:, 'Wind_ms'].quantile(0.1) # 10% quantile
    
    
    #df = pd.read_csv('turbine_telemetry.csv', parse_dates=[0], index_col=0)
    df = tt.query('Setpoint_kw==900').copy()
    
    # remove data points when the wind speed is fast enough for power production but there is no power;
    df.loc[((df.Wind_ms >= v_min) & (df.Power_kw.abs() <= 1e-5))] = np.nan
    
    # remove all missing values from the dataframe
    df = df.dropna(0, inplace=False)
    
    #####################################
    ## select bin locations
    #####################################
    wmax_ = df[df.Power_kw == df.Power_kw.quantile(0.90)].Wind_ms.quantile(0.5)
    wmax  = df.Wind_ms.max()
    
    
    bins = np.arange(0, wmax, .2)
    
    # group data by bins
    df['bins'] = pd.cut(df.Wind_ms, bins) #
    
    df_ = df[['Power_kw', 'bins']].groupby('bins')
    power_med = df_.quantile(0.5)
    power_med['q10'] = df_.quantile(0.1)
    power_med['q90'] = df_.quantile(0.9)
    
    
    # pretty good replication of the power vs wind profile
    plot_power = power_med.plot(rot=45)
    
    
    df['bins'].isna().sum()
    bin_nan = df[df["bins"].isna()]
    
    #####################################
    # look-up table mean and standard deviation
    #####################################
    
    # group data by bins
    cuts = pd.cut(df.Wind_ms, bins)
    gp_  = df.Power_kw.groupby(cuts) # iterator
    
    lutm = gp_.mean()
    luts = gp_.std()
    
    # convert to an interval index
    lutm.index = pd.IntervalIndex(lutm.index)
    luts.index = pd.IntervalIndex(luts.index)
    # this is the basis of our look-up table
    
    
    # round power to nearest 5 watts == 0.05 kW
    lutm = lutm.round(2)
    
    # set final power output to 900
    lutm.loc[wmax_:] = 900
    
    # make zero interval open at both ends to cover zero wind speed
    lutm.loc[pd.Interval(0,.2, closed='right')] = 0 
    
    
    #####################################
    # extend range to gusts of wind that are greater than max operating speed (25m/s) but of short duration
    #####################################
    #lutm.loc[pd.Interval(wmax_, 50, closed='right')] = 900
    #lutm.loc[pd.IntervalIndex.get_indexer_non_unique(lutm.loc[pd.Interval(25, 50)])] = 0


    
    # compare lookup table with data
    plt.figure(figsize=(15,5))
    s = plt.step(lutm.index.right, lutm, color='r')
    plt.legend(s, ['look-up table'], loc='upper left')
    
    #########################################
    gp = df
    mask = (gp.index.year == 2017)
    gp_17 = gp[mask]
    
    
    possible_power = [ 0 if pd.isnull(bini) else lutm[bini] for bini in gp_17.bins  ]
    gp_17 = gp_17.assign(Max_power_available = possible_power)
    

    return gp_17,lutm


#####################################
### Calculate the demand
#####################################

def get_demand_data():
    
    demand = pd.read_csv('residential_demand.csv', parse_dates=[0], index_col=0)
    mask   = (demand.index.year == 2017)
    demand = demand[mask]
    
    demand["Mean_demand"] = demand["Demand_mean_kw"]/demand["N_households"]

    return demand

def calculate_curtailed_energy_mean_demand(gp_17, demand):
    
    gp_17 = gp_17.reset_index()
    gp_17["Timestamp"] = gp_17["Timestamp"].apply(lambda x: pd.Timestamp.replace(x,second=0) )
    gp_17 = gp_17.set_index("Timestamp")
    
    
    curtailed = gp_17.join(demand, how = "outer")
    curtailed = curtailed.drop(columns = ["N_households","Demand_mean_kw", "Wind_ms", "bins"])
    curtailed.index.sort_values()
    
    
    curtailed['Mean_demand']   = curtailed['Mean_demand'].interpolate(method='linear')
    curtailed["island_demand"] = curtailed["Mean_demand"]*orkney_households
    
    
    curtailed_power = curtailed.copy()
    curtailed_power["power_excess"] = turbines_operating*turbines*curtailed["Max_power_available"] - curtailed["island_demand"] - 40000
    curtailed_power = curtailed_power.drop(columns = ["Power_kw","Setpoint_kw", "Max_power_available","Mean_demand", "island_demand"])
    
    curtailed_power.loc[curtailed_power['power_excess'] < 0, 'power_excess'] = 0
    
    total_curtailed_energy_kwh = curtailed_power["power_excess"].sum()/60

    return total_curtailed_energy_kwh, curtailed_power



total_curtailed_energy_1way, turbine_telemetry_filter_wind_power = calcucate_curtailed_energy_setpoint_based(tt17_mean_data)
gp_17,lutm = get_wind_power_relation(tt17_mean_data)
demand = get_demand_data()
total_curtailed_energy_2nd, curtailed_power = calculate_curtailed_energy_mean_demand(gp_17, demand)


