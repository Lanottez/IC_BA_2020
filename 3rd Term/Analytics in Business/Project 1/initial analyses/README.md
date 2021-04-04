# IC_BA_2020_BIA_A3


## To Do           

* Plot total revenue over time and its increase rate Qian
* KPI: Revenue per Member Qian
* Seasonality patterns Mary


* breakdown of our membership per type percentage over time Arianna-> transfer the most important to python
* age groups
* Find a benchmark for budget gyms in London ???

* start building the report / hypothesis / insights

* Question 5 about prediction?

* Survival rates-> Had a look into survival curve and tried splitting up the survival rates by gender and plotted the survival curve for both genders, it seems that the curve for female is slightly steeper where the survival rate for female is higher, until about 2010-02-01 where the survival rate for males exceed females. I will try to have a look into other member classes and see if there are any new insights.

### What other factors? (age, social class, sex) 
* Contribution to revenue Qian
* Growth rate over years Jiaxuan
* Behaviour change over years: type of memebership, duration of membership, visiting in peak/off peak (that may be challenging) Jiaqi- Done Analysis into the distribution of duration of membership for different customer segments, plotted out the distribution curves and it seems like the mean duration is very similar for different clubs as well as the age groups. One interesting thing found is that for subscription type, the mean duration for flexible and standard is the same, however the for standard membership it also has a second peak (i.e it is a bimodal distribtion). 
* Churn rate over years Mary DONE except for each lub
* See the visitation pattern in general as a possible predictor for cacellation, as well as description (frequency and peak/off peak)


### Qian:
#### Any trend in visitation during last months before gym : 
* peak times  
* freq per month
#### What I have found so far: 
* Chart 1: if I draw the number of membership versus time, we could find that the number of membership has been increasing constantly over time, although it dropped in 2016 while the price increased
<img title="Chart 1" src="Screenshots/Qian_Zhang/Chart_1.png" alt="drawing" width="200"/>

* Chart 2: if I draw the number of membership seperately according to the type of membership, we could find the the drop of customers was primarily caused by drop of standard customer. The reason could be that most members have standard memberships, as what is found by Jiaqi
<img title="Chart 2" src="Screenshots/Qian_Zhang/Chart_2.png" alt="drawing" width="200"/>

* Chart 3(Above) and Chart 4(Below): the membership of most customers only last less than 3 months, but the group who contribute the most to the revenue are those whose memberships last between 1 year and 3 months 
<img title="Chart 3" src="Screenshots/Qian_Zhang/Chart_3.png" alt="drawing" width="200"/>
<img title="Chart 4" src="Screenshots/Qian_Zhang/Chart_4.png" alt="drawing" width="200"/>

* Chart 5 The charged membership fees increases   
<img title="Chart 5" src="Screenshots/Qian_Zhang/Chart_5.png" alt="drawing" width="200"/>

* Chart 6
<img title="Chart 6" src="Screenshots/Qian_Zhang/Chart_6.png" alt="drawing" width="200"/>

###  Mary: 
#### Churn rate over time DONE 
Based on Jiaqi's analysis I plotted the churn rate over time and the insights are those that Jiaqi mentions on  __Graph 3__
#### Membership over time DONE
The membership growth over time seems to move around an average between 2012 and 2015, while there is a steep increase in late 2015 (maybe because of the reduction of total members??) and then it decreases again quickly. It seems that there is no longterm impact in the membership growth
#### I explore now:
* Membership change per club from increase -> calculate mean churn for Sep-2015 till Feb-2017, for most clubs similar mean except for 2 who had very lower rates 
  I should although check the difference compared to their means in general and check based on statistics if it is important
* clubs - members number over time -> Made the preliminary work but because of the number of the clubs (32) may we need to find a smarter way to inspect all of them
#### Churn rates per group DONE ( age not done)
* per gender,  per affluence,* per subscrition type
* for the plots please check my branch folder screenshots


### Arianna:
#### Hey guys i'm still learning my way to use pandas but here is some finding i found use other software. It shall be a good benchmark for double check and ideas. 
#### Currently i'm doing most analysis in excel & powerbi and moved/will move to jupyter if find any useful insights.

#### Findings - benchmark and won't include in jupyter
#### Average duration of membership is around 4.5 month for standard, and 2 month for flexible.
#### There is no significant membership duration differnece between 
* Affluence (range 2.3-1.97 for flexible; 5-3.8 for standard)
* different clubs (range 2.5-2 for flexible;  5.3- 4.1 for standard)
* ages (seperated by age group- range 2.6-1.9 for flexible ; 5.7-4 for standard)
* Gender (2.3-2.2 for flexible; 4.8 - 4.5 for standard)
                                                               
#### Interesting insights - Will/has move to pandas by tomorrow:
* for people left membership- there is no change in AFFLUENCE over year
* for people still in memebership - there is trend by affluence, gender membership status amond different years. However there is no change if we filter the data by memebership status >12 month.
*  younger people are more willing to join club in recent year. we can target promotion here 
* In general we see a reduction in number of memebers that left gym in 2016 compare wil 2015, and increase in numbers of members that join gym in 2016 compare with 2015. This might due to new gym opening - further investigation required
                                                       
                                                                                                 
### Jiaqi:
* Uploaded jupyter file of my code:
* The first two graphs is an initial overview of OC&Gym's customer segment(maybe can put in intro of presentation?)
* __Graph 1__: Affluence segment and membership type; B is the affluence group with highest members; Most members have Standard memberships(True across all affluence classes)
* __Graph 2__: Gender and age: Calculated age of each member and split into age-groups, most customers are from the age-group 30-39; there is relatively higher number of male members across all age groups

#### Graph 3 and 4 may be relevant to __Q2:What happened when the price was increased?__
* __Graph 3__: cancellations percentages(Monthly) : There is a sharp increase in percentage of cancellations just before the price increase in 01/01/2016, this may be due to OC&Gym's policy that  for standard customers, they are given the option of leaving before the price rise. However this increase in cancellation is not long-term. The percentage cancellations overtime seem to have seasonality trends
* __Graph 4__: New membership percentages(monthly) : There is a small decrease in percentage of new membership just after the price increase, however the decrease is not significant, thus the price increase seem to have small effect on percentage of monthly new memberships.
* I joined the data from both visitation datasets with the subscriptions dataset together into one dataframe

__File: Further Analysis AIB__
* similar to what Arianna has done in powerbi, I had Look at visitation times for customers who leaves within 3 months for different segements: The trends are all similar for the segements where members mainly come during the 3 peak time periods where the morning peak and evening peak is higher across all members. The peak is highest during the morning peak and the client mentioned the workout spaces can get very crowded during peak times; as the midday peak hour has the smallest of visits, potentially the gym can offer for this peak period to encourage more members to come during this time to ease the overcrowdedness in the morning peak. 


### Jiaxuan:
* Considered the membership growth rate over the year from the perspective of affluence, the oldest five clubs, Gender, Subscription Type
* Plot graphs for each factor for both the trend of total number of members and growth rate.
* Most factors have very similar trends for different groups inside.
* For the affluence graph, we can see that the growth rate of group C2 is very sensitive to the trend. It experienced the most rapid drop in 2015 and then rebounded in a fastest speed with the largest growth rate on the peak. This can be an interesting part to discuss.

#### Still working on the age group. Seems to be problematic at this time.


### Jiaqi & Jiaxuan：
#### Hi! We have uploaded a pdf file in the list.

This pdf file includes：
* Basic industrial backgrounds for the fitness industry and the problems that many gyms have been facing now. 
* Common and maningful KPIs for this industry that can be used in our analysis. We can choose some of them based on our data results.
* Potential OKRs that may be used to measure our analysis. This is mentioned in our project requirements. We think this part can be combined with the benchmarks from other competitors, using the competitors' data to set up our own OKRs. Here we include two feasible companies and the first one seems to be a better choice since it has more information with the data in their reports. 

If you guys have any thought for deeper researches or wants to include extra perspectives, we can focus on specific parts after considering our analysis results.
