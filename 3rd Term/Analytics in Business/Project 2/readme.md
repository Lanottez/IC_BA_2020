<br><div align="center"> By Group A3: </div>
<div align="center"> Jiaqi Chen, Yuxi Fu, Jiaxuan Lyu, Maria Tsotalou, Qian Zhang </div>

## 1. Summary


The purpose of this report is to provide an analysis and evaluation of the value for rolling out the Heat Smart Orkney Demand Response(DR) Scheme across the Orkney Isles. This report will pay particular attention to two sections: the first section is to calculate the amount of curtailed energy reduced from different levels of DR penetration based on the provided turbine and residential dataset, and the second section is to analyze the financial and commercial viability of this project. The financial viability is assessed by combining sensitivity analysis of our assumptions and the corresponding Net Present Value(NPV) calculations under different scenarios of levels of DR penetration.  The results of the analysis showed that the total amount of curtailed energy is sufficient to cover the seasonal household electricity demand during the whole year when curtailed energy is available and there is a positive linear relationship between the level of DR penetration and the amount of curtailed energy saved. 90% DR penetration is the best scenario according to our research and the project’s payback period in the program is around 5 years under exponential distribution. In conclusion, the DR scheme would help reduce the amount of wind energy curtailment  and the HSO project would be financially viable and has sufficient value for Kaluza to invest within the 10 investment period if Kaluza and wind turbine owners can ensure the programme is well promoted to encourage households to join the programme at an exponential rate to achieve the quicker payback period.

## 2. Introduction


Orkney is an archipelago of around 20 populated islands in the Northeastern coast of Scotland. It was the first part of the country to have an automatic smart grid and is a net exporter of renewable generation to Scotland.  There are currently over 500 wind turbines on the island. Due to the island's windy condition, they produce a sizable amount of wind energy; however, they have a limited capacity connector to the mainland through a 40MW cable. Thus, if the connector reaches full capacity, curtailment of the wind energy is needed to balance out the system, which leads to significant revenue loss for owners of wind turbines in Orkney.

'Heat Smart Orkney' (HSO) is a Scottish Government funded project that could potentially provide a solution to the problem. The project aims to install electric storage heaters into participating households' homes as a secondary heating device. Residential Demand Response(DR) is controlled using heating devices to reduce curtailed energy.  When switched on, it will consume some of the energy that would have otherwise been curtailed. This presents a commercial opportunity to increase revenue from generators, increase access to cleaner energy for households and financially benefit Kaluza from the installations of the controlled devices. Thus, this report will analyse the reduction in total yearly curtailed energy from different levels of DR penetration and assess the financial viability of the project in terms of net value to ensure it is a sustainable solution to the problem in the long run, for it to be attractive for all the stakeholders involved.


> There are a few key hypotheses for our analysis. Firstly, we hypothesise that the higher the level of DR penetration, the larger the decrease in total curtailed energy. If there are more households with the electric heaters installed, there would be a higher use of the wind output that would have been curtailed, thus reducing the amount of total curtailment. Moreover, we also predict that net value would be higher for higher DR penetration rates. To test our hypotheses, we would first calculate total yearly curtailment using a supply and demand approach. For different levels of DR penetration, the amount of curtailed energy used is calculated. After this, the project's overall net value is calculated, which would give an insight into whether the project is sustainable and financially viable.

## 3. Technologies and techniques


### 3.1   Data cleaning




The first step in our analysis is to idenify which data will be used and perform an appropriate data cleaning. 

Initially we explore both the demand and turbine datasets. As we have demand data only for the 2017, we will use the corresponding turbine data in order to be able to compare our available energy production with the demand.
It is observed that there are missing data for April 2017. More specifically, the data for April 3rd and April 24th are partially missing, while the data for April 4th to April 23 are entirely missing. In order to overcome this problem, the missing data in 2017 are filled in with the data from the same dates at 2016 as a proxy.

With an inspection, it is conluded that the turbine data have been collected with a step of approximately 1 min between consecutive samples.
In order to have a matching timestamp to the the residential demand data set we convert the turbine dataset timestamp to hh:mm:00, essentialy by converting all "seconds" values to zero. In the rare case that more than one measurements were present during the same minute we take the avergage of these measurements. 

For the residential demand data, we have the mean demand based on a specific sample. Based on the demographics for Orkney islands the number of housedholds is 10,385. Consequently we are considering a constant number of households with fluxuation in the mean demand based on the given data. 


### 3.2  Calculation of total yearly curtailment

To calculate the total yearly curtailment, a number of assumptions is made:

**Orkney islands currently have 500 wind turbines**

We currently have data on one proxy turbine in Orkney. There are currently over 500 wind turbines on the islands (Has Orkney Had Enough of Wind Farms?, 2018); thus, we would scale our calculations for 500 wind turbines and assume the same curtailment level across all the turbines.

**When the wind speed exceeds 25m/s, the turbine will be shut down**

From an engineering perspective, when the storm control system is deactivated, the turbine would shut down when an average wind speed of 25 m/s in the 10-minute-mean is reached as a safety measure. In our analysis, we considered the 25 m/s as a threshold and above that wind speed we make the assumption of zero energy production for the turbines.

**The capacity ratio of all wind turbines is 50%**

In order to calculate the maximum available power, except for the relationship between wind-speed and power, it is necessary to know what is the maximum capacity of all the turbines, since it is not reasonable to consider that all the 500 turbines will constantly operate concurrently due to maintance and other issues.  
Among the various suggestions for a capacity ratio we chose to assume a capacity ratio of 0.5. We use this ratio as a reference to scale appropriately the total potential produced energy.

**The total energy consumed in Orkney equals the household consumption plus export energy**

We assume that for the wind energy produced in Orkney there are two consumption streams, the household consumption and the ability to export to the Mainland up to 40MW of the total energy produced.

**The number of households in Orkney in 2017 is 10,385**

According to the National Records of Scotland, the number of households in the islands is 10,385 thus this is the number that would be used in our calculations.

**The curtailment calculation**

Under these assumptions, we filtered the data and used the following supply and demand  equation to approach the calculation of the total yearly curtailment:

*Curtailed Energy = Total Potential Energy - Household Demanded Energy- Exported Energy*

Energy = Power*time

The calculations for the total curtailed energy are based on binning the wind speed and calculating the power that it should have been produced with no curtailment under this wind speed. The wind-power relationship as well as the approximation of the real measurements are depicted on the figure below. We observe that this method gives very close results to the true measured values. 

![](https://drive.google.com/uc?export=view&id=1Yxgu9Xzpb4EFg9N8TBIDmPWJYptX3wN5)


![]( https://drive.google.com/uc?export=view&id=1Ek1Mt_a-pflc31bdAOlWVqRQcyMOPedw)


Taking into account the above relationship the total potential power is calculated based on the data available for 2017, after the data cleaning has been made. In order to calculate the total amount of power generated at each moment we should multiply with the number of turbines and rescale in order to take into account that not all turbines operate concurrently, due to maintance and other issues. 

The household demanded power at different times is calculated based on the mean demand that is given on the data multiplied with the numbr of households. It is noted that in order to calculate the demand between the given measurements, which have a step of half an hour we use a linear interpolation. 

The maximum Exported Power is constant at 40MW.

Finally at each time step we calculate the 
Total Potential Power - Househld demanded power - Maximum Exported Power, add all the positive values and multiply with 1/60 since we have one step every minute, in order to take the curtailed energy in Kwh.


### 3.3  Reduction in curtailment from Different DR penetration
The next step is to analyse the reduction of the total curtailed energy for different levels of DR penetration. For the analysis, a few additional assumptions are made:

**The average yearly electricity KWh consumption figure for Orkney is 8,193kwh per household**

This figure is according to the Scottish Government’s Energy in Scotland figures published in 2016 [* Paul M, Iain S.(2016)* ] As a result, we normalised and adjusted the load data to allow average demand usage in our calculation perfectly meet the actual Orkney residential electricity usage, while still remaining the shape of original "demand_mean_kw" line.

**All households in Orkney were using gas heaters before participating in the DR scheme**

An Assumption we have made is that all the households that enter the DR programme in Orkney use gas heaters before. This means that switching heating system to DR system will not cause reduction in electricity usage due to reduction in electricity demand of ordinary heater. As a result, the DR system will increase electricity demand exactly to average standard's household heating electricity usage. 



**The energy deamand for heating purposes is calculated based on the average residential daily electricity usage pattern in UK**

To calculate the electricity demand usage for the DR program, we have applied the average household electricity demand usage pattern on top of our prementioned estimated Orkney's total residential electricity demand [*Safdar, M. et al. (2019)*]. This will generate how much energy is required for the DR system per household. For simplicity, in our main model, we assumed the heater is used throughout the year due to Orkney island's low temperature. We also test a downside that the heaters only operate in winter. Those will be explained in more details in the result session. 

![](https://drive.google.com/uc?export=view&id=1UhohyOO8lRFHlyFya_jS8qjKZuSl5gq1)


**To calculate the energy saving of the DR system at different penetration levels, we assume that the heater will be auto charged/discharged hourly to meet the electricity demand for heating**

To calculate the increase in electricity demand due to the DR system's implementation, we assume a proportion of households that will join the program each year while the population remains unchange. For those residents that join the DR scheme, their hourly required electricity usage for heating will be equal to our estimated residential electricity usage amount, which we discussed in the previous session.

We also assume that at the start of each hour, while there is available curtailed energy, the DR sytem will start to charge electricity from the grid, and stop charging after it meets its heating energy requirement of that hour. If there is no curtailed electricity from the grid, the DR system will not charge any power. As such, our DR system demand will perfectly match the residential electricity usage unless there is no available curtailed energy in that period. Below is a graph representation of how our charging method fits the residential electricity usage (penetration level =100%). The gap between the two lines in the graph is due to lack of available curtailment energy during that charging period.  

![](https://drive.google.com/uc?export=view&id=1A2i-7rmqhxckPLJkkl12eBCyzdExz-uO)

We acknowledge that by shifting the charging period flexibily, the gap between the actuall electricity saving and the residential curtailment requirements can be further minimised. This could lead to a better estimation of the project's financial NPV and IRR result. Consequently, although we did not include this analysis here, we recommend that the analysis of the impact that the charging ability has on the revenue can be included during the future detailed analysis of the project.

### 3.4 Financial Viability

The analysis above demonstrates the potential curtailed energy that could be utilised if this DR system would be implemented based on data in 2017. However, in order to make our statement persuasive for the stakeholders, we need to prove that the project is financially viable for all involved parties.

To estimate the total value that might be generated from an Orkney wide DR scheme over the next ten years, we make the following necessary assumptions. First, since over the past decades the net migration of Orkney Islands is minimal according to the official migration report(General Register Office for Scotland.), we assume that for the next decade the number of household stays stable. Second, the wholesale and retail prices of electricity and the gas price are assumed to be identical over the next ten years as they was in 2017.  Third, we duplicate the predicted demand of electricity of curtailed energy in 2017 to the next ten years, assuming that the demand of curtailed energy is identical over the next ten years as they were in 2017. 

To make this project sustainable, we should consider not only the financial benefits for Kaluza, the DR solution supplier, but also the benefirs for the wind generators and residential consumer. Our goal is to assess whether there are sufficient net value, after the deduction of implementation costs, in order for the project to be attractive to all parties involved.

As the wind generators are selling energy that was curtailed at the wholesale price, the generators are guaranteed to make additional financial benefits. However, the residential consumers who join in this DR program switch from using gas for heating to using electricity, and the cost of using electricity to heat is much higher than the cost of using gas to heat. Therefore, in order for the the DR program to be attractive to the consumers, there is a need to fully reimburse their loss. Moreover, to motivate the local residents to join in this DR program, we provide 10% of the electricity price as subsidy for the residential household, so they could have a financial benefit by joining. Therefore, the additional profit which the generators make will be used to subsidize the loss of households first and motivate them to stay in the program as well.

The rest of those additional profits, after reimbursing the loss of households, will be divided into two parts. We make the following assumptions: the first part will be the 10% of the remaining profit, which stays with the generators so they could have a financial benefit by joining in this DR program, while the second part, which is the 90% of the remaining profit, would be the financial benefit of the DR solution supplier. 

Also, we take the cost into consideration by designing a simplified cost structure. Based on our cost structure for the DR solution supplier, there are fixed costs per installation of control equipment for each household, and rest of costs, which have been amortized over time since the same infra-structure supports other functions in the company, are simplified into a variable cost per month for each household. We assume that the fixed cost is deducted at the beginning of each year, and the value is the fix cost per installment multiplied by the predicted number new households who will join in this program each year. Considering the possible damage or loss of control equipments, the fixed cost is increased by 20%. 

In this initial analysis we proposed three possible scenarios about the degree of penetration after ten years: in the best scenario, the final degree of penetration is 90%; in the average scenario, the final degree of penetration is 75%; in the worst scenario, the final degree of penetration is 50%. Moreover, in all three scenarios, we assume two possible distributions of the growth of penetration degree. The first one is linear distribution, as the growth degree of penetration in every year is identical; The second one is exponential distribution, as the degree of penetration increases faster at the beginning and slows down later. We aim to assess the financial viability for the DR solution supplier under all six scenarios in order to make a comprehensive prediction.  
It is noted though that a more careful analysis based on market analytics and  simulations's techniques shuould be taken place in order to accurately predict the growth of degree of penetration.

To assess the financial viability preciously, we used the NPV, a popular technique for capital budgeting and investment planning to analyze the profitability of a projected investment. Since the above revenue and costs are calculated monthly, we take the discount rate into consideration and calculate the net-present-value, the sum of all present values of all future cash flow, to analyze the profitability of this project in all six scenarios of DR penetration. We also aim to find the break-even point of the duration required in order to answer the question of how long the DR solution suppliers need to endure net loss until they could earn revenue.

### 3.5 Commerical Value

Moreover, the benefit of this project is assessed not only in terms of financial benefit to Kaluza, but also in terms of social and environmental benefits to the broad community. By switching a very large portion of energy consumption from using gas to using energy generated by wind, we could significantly reduce the carbon emission. Therefore, we aim to assess the amount of carbon emissions reduction during this ten years under the different scenarios of the DR program penetration. Moreover, to emphasize the amount of carbon emission that could be reduced by adapting the DR program, we also calculate the equivalent amount of carbon emission that is generated by driving an average passenger vehicle. We aim to assess that the carbon emission in terms of carbon emissions per mile from average passenger vehicle and the carbon emissions per average passenger vehicle driving each year.

##4. Results

## 4.1 Total curtailed energy


The normalised load for the island is depicted on this figure. This is the normalised average demanded power based on the aggregation of daily information. It can be easily observed that the demand follows a seasonality trend; higher load during the winter and lower load during the spring and summer. 

![](https://drive.google.com/uc?export=view&id=1ax_Xi7nfoHLinGwV8OIIGHJ1XeFtsqbQ)

The available power after the normalisation and aggregation of the data on a daily basis, as well as the power that is curtailed during the 2017 is depicted on the next two figures. It is observed that the power is curtailed during the whole year. 

![](https://drive.google.com/uc?export=view&id=1LPE6IU1RDyphwLtSpczT5_83nJXnmmgV)


![](https://drive.google.com/uc?export=view&id=1EyWJ6nAskgwLRp7Tp_-4KAi9XsV6bh5p)


A total amount of approximately 343372 MWh has been curtailed during 2017.

This initial inspection indicates that energy-wise the project is feasible. However, it is important to investigate the economic aspects.

### 4.2 Saved curtailment energy by DR program

#### 4.2.1 There is a perfectly linear relationship between  the curtailed energy saving and the level of DR penetration:


From our analysis, our results shows there is a positive linear relationship between the level of DR penetration and the amount of curtailed energy saved. We do not observe changes in slop gradient as DR penetration level increases, as the marginal increase in curtailed energy saving stays the same as DR penetration increase, and we do not see this slope changes as penetration level changes. As the number of households joining the program increases, the amount of electricity demand for heating by these households also increases, and the saved curtailed energy increases correspondingly by the same amount.



![](https://drive.google.com/uc?export=view&id=11WiMRGFRN1pwNOfsL9KYujF3320ldp_p)


#### 4.2.2 The DR system electricity usage occupies only a small percentage of the total wind curtailment energy
Indeed, for each 10% increase in the DR penetration, the curtailment energy saving will correspondingly increase by 1GWh per year. This number does not shift as the penetration level varies. It is because the current available curtailed energy is much higher than the required DR program demand. Besides, under our calculations, even 100% DR penetration only requires around 50% of this unused energy.

The graph below shows the daily sum of curtailed wind energy and the daily sum of DR electricity demand at 100% and 10% penetration. This graph suggests that available electricity curtailment of wind generator in 2017 is much less than household demand for heating from the DR system. 

The gap between available curtailed energy and actual demand usage gradually reduces from 3pm in the afternoon until midnight, which also makes sense intuitively. In an average day of the year, wind speeds remain relatively stable at different hours, however residential electricity demand increases at night. As at every point in time, electricity supply should perfectly meet demand, an increase in residential electricity demand at night will reduce curtailment energy of wind. Nevertheless, we still saw a big difference between unexploited wind curtailed energy and DR scheme electricity demands.


![](https://drive.google.com/uc?export=view&id=1V_-wZQekbNuqZX9pAWUpkvqPR8wEpS1m)


#### 4.2.3 Energy saved from DR program is slightly less than actual residential electricity demand 

Even though there is a tremendous amount of unexploited wind energy available for the DR scheme, actual energy savings from the program is still slightly less than actual residential heating demand. Also from session above, we know that this gap does not vary as DR penetration growth. In the graph below, it presents the daily residential heating electricity demand, and how much our DR system can provide throughout the year. We can see that under our current charging/discharging assumptions, the DR heating system can not fully meet residential electricity demands. This is mainly happened during mid of the day, and around eveing electricity demand peak hours around 7pm.

![](https://drive.google.com/uc?export=view&id=1tp8AzHd4F4zBHYv6T3y7r_sDwduh2SbQ)

Under further analysis, we find that this lack of support of our DR system is primely due to period of time that no wind curtailment energy available. Note that in graph below, the blue line (which represent amount of time that DR system cannot fully support residential heating electricity usage) and the red line （which represent there is no available curtailed energy from the grid）has perfectly meet each other. This varified our analysis that no curtailment energy available due to charging period is the main driver for lack of electricity to fully support residential heating. This problem might leads to customers' unhappiness, however could be simpily solved by better charging methods. Further analysis on improving charging behaviour is recommonded.  

![](https://drive.google.com/uc?export=view&id=1z0a8f04l7CXykMYG5msUmErFUEHH_asB)

Also, from the green line above, which represents total time of period that the wind turbines are not generating at all. We can see that around 33% (22/65) of the time that there is no surplus curtailment energy which due to wind turbines turn off, whereas the rest 66% should represent period of time that total generation is less than the max electricity export capability plus residential electricity usage.


#### 4.2.4 Seasonal impact of energy saving from curtailment:

The diagram below shows there are significant seasonal impact of energy saving of curtailment. As you can see October, November, December as well as January have higher energy saving compare to other months of the year. This result is what we have expected as consumers tend to switch on electrical heaters more often in winter.  

![](https://drive.google.com/uc?export=view&id=1ze_wnYDC67-K4-4axnC88mxMsTRLnGi3)


However, our assumption states that consumers use electric heaters throughout the entire year. If we assume consumers only uses electric heaters for two coldest months of the year (December and January). Then the revenue generated by this project will potentially be reduced by 70%. Hence, this may indicate 70% of the revenue of our project may be unstable.
 
![](https://drive.google.com/uc?export=view&id=1OYxQBIkW3J7VeBAoplFzQhtLzE5XWJDr)

### 4.3 Financial Viability Analysis

In both the scenario below, we assess the cumulative discounted cash flow over the next year with the following values stays the same: the total number of households, the wholesale and retail electricity prices, the gas price, the estimated demands of electricity generated by wind power.   

### 4.3.1 Scenario 1: Linear Distribution

In the scenario 1, we assumed three possible degrees of penetration after ten years from today: 50%, 75%, 90%, and the increase of degrees of penetration follows a linear distribution, We draw the corresponding lines of discounted cash flow for each possible degree penetration. From the line charts, we could see that under all three possible predictions of the degree of penetration, the net discounted cash flow becomes positive at approximately year 9, or more preciously, 108 months. However, while the predicted final degree of penetration is 90%, the loss is larger during the first few years, but the revenue is also larger after the NPV becomes positive. This result makes sense, since while the degree of penetration is larger, more revenue is deducted because of the new installment. However, after the NPV becomes positive, the revenue increases faster since as more households join in this program, the monthly and yearly revenue is also larger. Meanwhile, the prediction that the NPVs under all three assumptions become positive at the same moment also make senses, since our revenue model and cost structure is simplified and all relations are linearly depended. 

![](https://drive.google.com/uc?export=view&id=1ekjE7yWylzKQna71-B-CgHUcMiLnq0o-)

#### 4.3.2 Scenario 2: Exponential Distribution 

In the second scenario 2, we make the same assumption of possible degree of penetration after ten years, but we assume the increase of degree of penetration follows an exponential distribution, as the number of household who join in this DR program is larger in the beginning but slows down after. The line chart shows two identical patterns as the line chart in scenario 1: that while the predicted final degree of penetration is 90%, the loss is larger during the first few years, but revenue is also larger after the NPV becomes positive, and that the NPVs under all three assumptions becomes positive at the same moment, and the possible explanation behind the pattens is also identical as it is in scenario 1. However, in this scenario, the net discounted cash flow becomes positive at approximately year 5, or more preciously, 58 months, and the revenue at year 10 is much larger than the revenue at year 10 in scenario 1. 

![](https://drive.google.com/uc?export=view&id=1cwaMoNp26vrA900kYsBrln4Nt4iiF5RW)

### 4.4 Commercial Value Analysis
The chart below shows that, under the three scenarios of predicted degree of penetration after 10 years, how many energy that are originally supported by gas is now supported by wind power generator each year. This amount of saved curtailment could reduce the carbon emission significantly. According to the report of the Intergovernmental Panel on Climate Chance IPCC, the CO2 equivalent produced per kWh of wind energy is 8g to 20g, while the CO2 equivalent produced by gas is estimated to be between 270g to 910g[Wiser, R., & Yang, Z. (2018, March).]. Therefore, in the best scenario, where the predicted degree of penetration is 90% after ten years, we could save 8908 MWh that is originally generated by gas to be generated by wind power, and that is equivalent to 2333Mg to 7928Mg of carbon emission, which is significant. By estimation, the CO2 emissions per mile from average passenger vehicle driving a mile is 404gram.[U.S. Environmental Protection Agency. (2018, March)] Therefore, if we take the average of the possible carbon emission and divide it by the estimtaed CO2 emissions per mile, it is approximately equivalent to 12,698,019 miles driven by an average passenger vehicle. If we take assumtption that average passenger vehicle drives 12,000 mile for a year, then adapting this project helps to reduce the carbon emission of 1058 average passenger vehicles every year. 
![](https://drive.google.com/uc?export=view&id=1IXrfmPc54YnrdtdBpMMe87jKmHnBSreQ)

# 5. Discussion


The results indicate that total wind energy curtailment in 2017 is 72717 MWh. For the HSO Demand Response scheme to be attractive for all stakeholders involved, the aim is to decrease the total curtailment in 2017 as much as possible to ensure the project has sufficient net value. Our analysis suggests a positive trend, where an increase in the number of households participating in the scheme would increase the amount of saved curtailment. Moreover, the revenue analysis results also support this trend as the penetration rate with the highest returns in 10 years is the 90% rate. As we discussed in section 4.3, the project’s payback period is approximately 9 years for scenario 1 and 5 years under scenario 2. According to a report by Mckinsey&co, energy and environmental (EE) investments on average have a payback period of around 5 years (Capturing the full electricity efficiency potential of the UK, 2012). Thus, scenario 2 of the penetration rate growth following an exponential distribution has a payback period closer to this average figure. This result suggests that for the HSO project to be financially viable and has sufficient value for Kaluza to invest, within the 10 investment period, Kaluza and wind turbine owners would need to ensure the programme is well promoted to encourage households to join the programme at an exponential rate to achieve the quicker payback period.


We predict that a key hypothesis is a positive relationship between the level of DR penetration and the amount of curtailed energy saved. In line with the hypothesis, results in section 4.2.1 illustrate a positive linear relationship; thus, the hypothesis is correct. However, some caveats should be noted where the analysis relies on some key assumptions. We assumed that all households have the same energy consumption trends all year round; hence a 1% increase in DR penetration would result in the same marginal increase across all penetration levels, resulting in a perfect linear trend. In reality, each household is likely to have different consumption patterns; thus, the marginal household joining the DR scheme is unlikely to increase curtailed energy consumption by the same amount. The positive relationship should still holds, but the slope would not be perfectly upward sloping.
Moreover, another hypothesis supported by the results is that the project's total net value is higher for higher levels of DR penetration. This is true for both scenarios discussed in section 4.3. The financial analysis is based on a simplified costs structure. More comprehensive cost data is needed for further analysis which would help improve the accuracy of the calculations.

**5.1 Recommmendation**

From the report's results section, it is evident that the DR scheme would help reduce the amount of wind energy curtailment and the financial analysis suggests the project has sufficient net value for investment. Under scenario 2, the growth rate of penetration rate across the ten years grows exponentially, giving a payback period of around five years for 90%, 70% and 50% penetration rates. As the 90% penetration rate results in the highest revenue level, our suggestion is for Kaluza to invest in the project and aim for the 90% penetration rate. As the penetration rate grows exponentially to achieve the payback period of 5 years, Kaluza needs to ensure the project is well promoted for all households to be aware of the benefits of the project for household participation rate to be fast-growing and reach 90% penetration within ten years where the total revenue for Kaluza in 10 years is approximately £400,000.



**5.2 Strengths and limitations of the analysis**

Strengths:

1. Comprehensive analysis: Using the available data, we analysed the curtailment problem from a multidimensional angle where we explored the curtailments under different months and times of the day. The financial analysis also considers multiple scenarios.

2. As mentioned in section 3.3, for our demand analysis, we normalised and adjusted the load data to ensure average demand usage meets the electricity usage of households in Orkney and also took into account the average household electricity demand for heating. This would ensure the demand is representative of a ‘proxy’ household in Orkney and would avoid any overestimations of demand.



Limitations:
1.	Currently there are some household electricity demands which cannot be satisfied due to the lack of curtailed energy. Since we don’t consider the energy shifting by collecting curtailed energy from specific charging period for later usage in our report, shifting charging period flexibly may minimized the gap between actual electricity saving and residential curtailment requirement. It’s meaningful to analyze revenue impact of charging ability in the future project, which can also provide better estimations of project's financial NPV and IRR result.
2.	In the report, we assume the company would cover all the costs for households to join the program so that they can be attracted to subscribe the scheme. However, we don’t make assumptions on the price discount for electricity price to be lower than the gas price, which may be a better and more sustainable way of encouragement for households to stay in the scheme in the future. Using specific discount assumption for price differences may also result in more reasonable revenue and net present value for the whole program.


**5.3 Further Analysis**

As mentioned in section 4.2.1, total curtailed energy is higher than demand, even with 100% of households in Orkney joining the scheme, the curtailed energy still remains at a relatively high level. This large amount of unexploited energy gives us room to consider additional kinds of demand-side response projects and thoroughly take advantage of this unused surplus. For example, one project could expand the current energy storage. This extra storage ability can be used to enter into energy arbitrage market. That is, to buy power from grid while energy curtailed/wholesale electricity price is low, and sell those power to the grid later when the wholesale electricity price is high [Wei W, Feng L & Sheng W (2015)]. From the social benefit perspective, connecting the decentralised energy storage system to the grid could not only utilise idle distributed generation capacity but also improve the electricity system's stability and reliability. This will also reduces government costs on maintaining system stability. [Association for Decentralised Energy (ADE)]

Moreover, our current analysis is based on the assumption that the heaters operates all year round, thus we have not taken into account seasonal trends in heating usage. For further analysis, we could filter the data for the winter months and perform analysis on this data, as this is likely to be more realistic and would avoid overstimation of electricity usage for heating.

# 6. Reference:

General Register Office for Scotland. (2010, August). Orkney Shetland Eilean Siar Migration Report. https://www.nrscotland.gov.uk/files/statistics/migration/Migration-Reports/orkney-shetland-eilean-siar-migration-report.pdf

Wei, Wei & Feng, Liu & Mei, Shengwei. (2015). Energy Pricing and Dispatch for Smart Grid Retailers Under Demand Response and Market Price Uncertainty. Smart Grid, IEEE Transactions on. 6. 1364-1374. 10.1109/TSG.2014.2376522. 

Paul Matthews and Iain Scherr (2016). Annual Compendium of Scottish Energy Statistics. Scottish Government

The Orkney News. (2018) Has Orkney Had Enough of Wind Farms?. [online] Available at: <https://theorkneynews.scot/2018/09/02/has-orkney-had-enough-of-wind-farms/>

Safdar, M. et al. (2019) Costs of Demand Response from Residential Customers’ Perspective. Energies (Basel). [Online] 12 (9), 1617–.

Association for Decentralised Energy (ADE): Less waste, more growth - Boosting energy productivity

GOV.UK. 2012. Capturing the full electricity efficiency potential of the UK. [online] Available at: <https://www.gov.uk/government/publications/capturing-the-full-electricity-efficiency-potential-of-the-uk--2> 

Wiser, R., & Yang, Z. (2018, March). Wind Energy. https://www.ipcc.ch/site/assets/uploads/2018/03/Chapter-7-Wind-Energy-1.pdf

U.S. Environmental Protection Agency. (2018, March). Greenhouse Gas Emissions from a Typical Passenger Vehicle (EPA-420-F-18-008). https://nepis.epa.gov/Exe/ZyPDF.cgi?Dockey=P100U8YT.pdf

Kaewpet, P. and Bullen, C. Feasibility Study of Orkney's Windfarm Development for self-sufficient for energy in electricity demand and road transport sectors. (April 2018) Advanced Energy: An International Journal
https://airccse.com/aeij/papers/5218aeij01.pdf
"""
