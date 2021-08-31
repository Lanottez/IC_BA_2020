### ParametersTitle page

Name: Qian Zhang

CID number: 01939418

Report title: 

Word count: 964

### Abstract (suggest 150 words)



### Introduction:

Coronavirus disease, as known as Covid-19, is an infectious disease caused by a newly discovered coronavirus(1). Being a highly infectious disease, Covid-19 has spread to almost whole world since the first confirmed victim, a Wuhan resident, fell sick on Dec. 8, 2019(2). On 30 January 2020, following the fact that COVID-19 has spread from the People’s Republic of China to 20 other countries, the World Health Organization (SARSWHO) declared the outbreak as a Public Health Emergency of International Concern(3). On 11 March 2020, WHO made made the assessment that COVID-19 can be characterized as a pandemic(4). The United Kingdom became a part of the worldwide pandemic two people from the same family have tested positive for coronavirus in the UK on 31 January 2020(5). The initial response from UK government on the COVID-19 situation was to launch public health information campaign to minimize the impact of COVID-19 on society. Governments campaign on the public use of mask, however, was vague. On the one hand, the study on severe acute respiratory syndrome (SARS), which was caused by another strain of SARSr-CoV, frequent mask use in public venues, frequent hand washing, and disinfecting the living quarters were significant protective factors(8).  On the other hand,  It takes a while until 15 June 2020 for the government to announce that face coverings will be mandatory on public transport after 15 June(7). 

英国首相提出flatten the curve的政策to slow down the spread of the SARS-CoV-2，以此避免对NHS造成医疗资源上的挤兑。这依赖于民众本身的努力，需要social distance及使用PPE来阻碍新冠疫情的传播，但是由于mask在英国原本仅用于医护人员，而新冠疫情导致的大幅需求上升是始料未及的。Early on in the pandemic, the NHS experienced severe shortages of personal protective equipment, known as PPE(6). 因此，英国的mask多数来自于进口，mainly from china. In March, 2020, France government forced a face mask manufacturer to cancel a major UK order(10)In 10 April 2020, British Govement dispatched a RAF plane to pressure Turkey to release gowns for NHS(9). 

未来的将来，是否会因为出现逆全球化，或者国家是否会定义新的战略物资，并不在这篇文章的讨论范围内。这paper致力于回答，在可见的、英国尚且依赖于国外进口口罩的时期，如何保证进口的口罩足够于国内居民的应用。或者，如果未来出现新的变种或者新的传染病，在假设口罩十分重要的情况下，如何储备库存，以免出现口罩不足的情况。

因此，我们需要一种手段来预测对mask的需求，并判断不同的mask采购量，以避免出现PPE出现严重短缺的情况。会对新冠造成多大的抑制效果。另外，我们需要考虑有R值更高的变种出现时，是否会出现PPE的严重短缺，或者是NHS资源的短缺。1.分析PPE对防止疫情蔓延的作用；2.分析2020年期间，如果英国没有出现PPE短缺现象，且民众对PPE接受程度很高，死亡人数是否会出现变化；3.分析在目前情况下，英国总体需要储备多少口罩，每个月需要购买多少PPE；4.分析如果未来出现传播率更高的病毒亚种，是否需要更多PPE。

首先，证明政府开始推广PPE之后，疫情的蔓延速度有所下降。为了可视化这个过程，我们需要先绘制疫情推广的速度。由于初期的数值是有限的，我们需要根据死亡人数倒推真实的疫情蔓延速度，同时通过这个速度，比较推广PPE及不推广PPE，对疫情的阻碍有多大作用。同时，我们要结合疫情的R值，及模拟不同程度的mask使用程度，判断推广PPE对疫情的阻碍，病人的住院率及死亡率会有什么作用。

这篇paper对于PPE效果的预测必须基于真实的疫情蔓延数字。这些数据可以从英国官网寻找，我们先将其画出，并包括一些重要的时间节点。但从以下图表可以看出，尽管第一波疫情及第二波疫情的死亡人数曲线非常类似，但确诊人数却差别很大。根据xxx，原始毒株及alpha毒株的致死率差距并无很大。因此，导致两者出现以上区别的原因是，在所有时期，官方的测量数据并不等于真实感染疫情的人数。这个现象有很多原因，包括无症状感染者，抗体检测的不足，官方检测的目标不同、患者因为各种原因（例如不想被隔离）主观上拒绝检测等等并且，在2020年初期疫情爆发的初期，由于官方检测力量的不足，确诊/报告的比例要远小于现在。因此，我们需要某种手段去推测真实的感染人数。同时，我们还要考虑covid-19存在的潜伏期，因此，我们需要用使用数学模型来预测在如果戴口罩的话，疫情的死亡人数是否会有变化。



### Model

##### Baseline Compartmental Models

自从疫情爆发以来，由于病毒本身的特征，确诊数字远远小于感染数字，因此数据分析师，生物学家，政客已经尝试通过许多模型来预测正式的感染数字。毫无疑问的是，没有模型可以准确预测真实的确诊数字，但是一个sophisticated的模型可以提供非常有意义的数字。

我们将使用Compartmental models in epidemiology来预测口罩政策是否会改变疫情的死亡数字。Compartmental models作为传染病界广泛应用的数学模型，可以根据传染病的各种性质进行调整，来针对性预测指导传染病的预防和控制工作。对于最简单的Compartmental models，人群会被分为S(Susceptible), I(Infectious), or R(Recovered)三个群体，I为患病的群体，R为患病后康复的群体，而剩下未曾患病但又得病可能的即为S群体。这篇文章采用了文章Infectious Disease Modelling: Fit Your Model to Coronavirus Data中[15]设计的模型。作者Henri Froese根据新冠的特征对compartmental models进行了调整。由于新冠存在潜伏期，患者在感染病毒后几天内无症状也无传染性，这段期间的患者被称为暴露期，我们以E来代表这个群体。另外，绝大多数新冠患者实际上不需要入院治疗，但是由于新冠的传播力过强，因此大规模传播时会挤兑医疗资源。在March，2020，就有a leading ventilator manufacturer said that Britain faces a “massive shortage” of ventilators that will be needed to treat critically ill patients suffering from coronavirus.[16].因此，作者用C来标记 individuals that need intensive care。这可以帮助我们判断英国是否有额外购买呼吸机的必要。最后，D为死亡的群体。

| Letters | Compartments              |
| ------- | ------------------------- |
| $S$     | Susceptible people        |
| $E$     | Exposed people            |
| $I$     | Infectious people         |
| $C$     | People need Critical Care |
| $R$     | Recovered People          |
| $D$     | Dead People               |

Compartmental models in epidemiology需要parameters以用于量化不同compartments的group之间转化的速率。因此，我们设立parameters如下

| Parameters         | Explanation                                                  | Value                       | Reference |
| ------------------ | ------------------------------------------------------------ | --------------------------- | --------- |
| $\beta(t)$         | the baseline infectious contact rate                         |                             |           |
| $\sigma$           | the transition rate from the exposed to infectious class     | $\frac{1}{5}   $ $day^{-1}$ | [12]      |
| $\frac{1}{\sigma}$ | the disease incubation period                                | $5$ $day$                   | [12]      |
| $\eta$             | probability that an infected individual becomes critically ill | 0.25                        | [13]      |
| $\alpha$           | the probability of dying while critical                      | 0.16                        | [14]      |

各Compartments的改变速率如下

| Changing Rate of Compartments                                | Explanation                                                  |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| $\frac{dS}{dt} = -\beta(t)  I \frac{S}{N}$                   | the chance that a susceptible individual meets infect people is $I*\frac{S}{N}$, and the probability of catching the virus is $\beta(t)$. 因此S群体改变速率为$-\beta(t)*I*\frac{S}{N} $ . |
| $\frac{dE}{dt} = \beta(t) I \frac{S}{N}-\sigma E$            | $\beta(t) *I*\frac{S}{N}$ 为每个时间单位增加的exposed的人群。Moreover，有一部分exposed的人群会转变为有症状或无症状感染者，因此exposed人群的改变速率为$\beta(t) * I * \frac{S}{N}-\sigma E$. |
| $\frac{dI}{dt} = \sigma  E - \frac{1}{12}  \eta  I - \gamma  (1 - \eta)  I$ | $\sigma E$为每个时间单位从exposed的人群转变为感染者的人数，其中有$\alpha$比例的人为有症状感染者。另外，有症状感染者中，每个时间单位有$\delta I$的人死亡，有$\gamma_{I} I$的人康复，因此I人群的改变速率为$\alpha \sigma E - \delta I - \gamma_{I}I$. |
| $\frac{dC}{dt} = \frac{1}{12} \eta I - \frac{1}{7.5} \alpha * min(Beds(t), C)$<br />$- max(0, C-Beds(t)) - (1 - \alpha) \frac{1}{6.5}*min(Beds(t), C)$ | $(1-\alpha)\sigma E$为每个时间单位exposed人群转为无症状感染者的人数，$\gamma_{A}A$为每个时间单位无症状感染者康复的人数，因此A人群的改变速率为$(1-\alpha) \sigma E - \gamma_{A}A$. |
| $\frac{dR}{dt} = \gamma  (1 - \eta)  I + (1 - \alpha) * \frac{1}/{6.5} * min(Beds(t), C)$ | $R$为所有康复人群的总和，因此每个时间单位，有$\gamma_{I} I + \gamma_{A} A + \gamma_{H} H$的人康复 |
| $\frac{dD}{dt} = \frac{1}{7.5} \alpha  min(Beds(t), C) + max(0, C-Beds(t))$ | 每个时间单位，住院的人中有$\delta H$的人数死亡               |

这是一个符合新冠特质的传染病模型，首先，我们可以通过拟合英国第一波疫情期间的死亡数据，得出英格兰第一波疫情时期R值的变化。我们选择英国第一波疫情是因为当时英国政府仅通过社交隔离及推荐使用口罩的方式来压制疫情，而第二波第三波疫情时，英国出现了alpha及delta变种，且英国在持续不断地接种疫苗，另外，第一波疫情时的患者可能免疫力笑死，出现重复感染的现象。这些变数会让这个传染病模型预测不准，因此，我们仅用第一波的死亡数据来估量R值的变化。另外，拟合死亡数据的原因是因为确诊数字收到太多因素的影响，仅代表了一部分的感染数字，但是英国政府的死亡数据则更加贴近真实的因新冠死亡的人数。



##### Adjusting Model with Consideration of Mask Use in Public

通过拟合英国第一波疫情期间的死亡数据，我们得出了模型的model。通过调整基础的Compartmental models，我们可以预测如果英格兰民众自疫情开始就广泛且使用面具，因为新冠死亡的人数会有什么变化。对于调整后的compartment models，我们会采用To mask or not to mask modeling the potential for face mask中的办法。While the author的compartment models与本文中的模型并不相同，我参考了作者的思路，assume that the masks used by public have uniform inward efficiency (i.e., primary protection against catching disease) of $\epsilon_{i}$, and outward efficiency (i.e., source control/protection against transmitting disease) of $\epsilon_o$ .Also, the author disaggregated all population variables into those that typically do and do not wear masks, respectively subscripted with $U$ and $M$. 调整后，the adjusted Compartmental model is as below: 



##### Projecting Death Of The First Wave Under Different Coverage

我们假设第一波疫情期间，英国人没有任何群众使用口罩。因此，我们设计了三种不同的scenario。这三种情况中，分别有30%，50%，及70%的人在公共场合正确地使用了口罩。将这三个情况代入到the Adjusted Compartmental Model。我们即可以预测出，这三种情况下，英国第一波疫情中的死亡人数是否会出现不同的变化。



Fitting Parameter of Adjusting Model with respect to Current Wave









### Result



### Conclusion



### Limition



### References

1. https://www.who.int/health-topics/coronavirus#tab=tab_1
2. https://www.wsj.com/articles/in-hunt-for-covid-19-origin-patient-zero-points-to-second-wuhan-market-11614335404
3. COVID 19 PHEIC.pdf
4. https://www.who.int/director-general/speeches/detail/who-director-general-s-opening-remarks-at-the-media-briefing-on-covid-19---11-march-2020
5. https://www.bbc.com/news/health-51325192
6. https://www.bbc.com/news/uk-54897737
7. https://www.independent.co.uk/news/uk/home-news/coronavirus-face-mask-uk-fine-police-public-transport-grant-shapps-tube-bus-train-a9567056.html
8. [SARS Transmission, Risk Factors, and Prevention in Hong Kong - Volume 10, Number 4—April 2004 - Emerging Infectious Diseases journal - CDC](https://wwwnc.cdc.gov/eid/article/10/4/03-0628_article)
9. https://www.theguardian.com/society/2020/apr/20/raf-planes-await-order-to-set-off-to-collect-ppe-from-turkey
10. https://www.euronews.com/2020/03/06/coronavirus-french-protective-mask-manufacturer-scraps-nhs-order-to-keep-masks-in-france
11. To mask or not to mask: Modeling the potential for face mask use by the general public to curtail the COVID-19 pandemic
12. https://www.webmd.com/lung/coronavirus-incubation-period#1
13. Infectivity of asymptomatic versus symptomatic COVID-19
14. Quantifying asymptomatic infection and transmission of COVID-19 in New York City using observed cases, serology, and testing capacity
15. https://towardsdatascience.com/infectious-disease-modelling-fit-your-model-to-coronavirus-data-2568e672dbc7
16. https://www.reuters.com/article/us-health-coronavirus-ventilators-idUSKBN2153JV



### Appendix or appendices (if applicable)





