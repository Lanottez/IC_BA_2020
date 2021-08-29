### ParametersTitle page

Name: Qian Zhang

CID number: 01939418

Report title: 

Word count: 964

### Abstract (suggest 150 words)



### Main text:

*Introduction*

Coronavirus disease, as known as Covid-19, is an infectious disease caused by a newly discovered coronavirus(1). Being a highly infectious disease, Covid-19 has spread to almost whole world since the first confirmed victim, a Wuhan resident, fell sick on Dec. 8, 2019(2). On 30 January 2020, following the fact that COVID-19 has spread from the People’s Republic of China to 20 other countries, the World Health Organization (SARSWHO) declared the outbreak as a Public Health Emergency of International Concern(3). On 11 March 2020, WHO made made the assessment that COVID-19 can be characterized as a pandemic(4). The United Kingdom became a part of the worldwide pandemic two people from the same family have tested positive for coronavirus in the UK on 31 January 2020(5). The initial response from UK government on the COVID-19 situation was to launch public health information campaign to minimize the impact of COVID-19 on society. Governments campaign on the public use of mask, however, was vague. On the one hand, the study on severe acute respiratory syndrome (SARS), which was caused by another strain of SARSr-CoV, frequent mask use in public venues, frequent hand washing, and disinfecting the living quarters were significant protective factors(8).  On the other hand,  It takes a while until 15 June 2020 for the government to announce that face coverings will be mandatory on public transport after 15 June(7). 

英国首相提出flatten the curve的政策to slow down the spread of the SARS-CoV-2，以此避免对NHS造成医疗资源上的挤兑。这依赖于民众本身的努力，需要social distance及使用PPE来阻碍新冠疫情的传播，但是由于mask在英国原本仅用于医护人员，而新冠疫情导致的大幅需求上升是始料未及的。Early on in the pandemic, the NHS experienced severe shortages of personal protective equipment, known as PPE(6). 因此，英国的mask多数来自于进口，mainly from china. In March, 2020, France government forced a face mask manufacturer to cancel a major UK order(10)In 10 April 2020, British Govement dispatched a RAF plane to pressure Turkey to release gowns for NHS(9). 

未来的将来，是否会因为出现逆全球化，或者国家是否会定义新的战略物资，并不在这篇文章的讨论范围内。这paper致力于回答，在可见的、英国尚且依赖于国外进口口罩的时期，如何保证进口的口罩足够于国内居民的应用。或者，如果未来出现新的变种或者新的传染病，在假设口罩十分重要的情况下，如何储备库存，以免出现口罩不足的情况。

因此，我们需要一种手段来预测对mask的需求，并判断不同的mask采购量，以避免出现PPE出现严重短缺的情况。会对新冠造成多大的抑制效果。另外，我们需要考虑有R值更高的变种出现时，是否会出现PPE的严重短缺，或者是NHS资源的短缺。1.分析PPE对防止疫情蔓延的作用；2.分析2020年期间，如果英国没有出现PPE短缺现象，且民众对PPE接受程度很高，死亡人数是否会出现变化；3.分析在目前情况下，英国总体需要储备多少口罩，每个月需要购买多少PPE；4.分析如果未来出现传播率更高的病毒亚种，是否需要更多PPE。



*Will Personal Protective Equipment protect people from COVID-19?*

首先，证明政府开始推广PPE之后，疫情的蔓延速度有所下降。为了可视化这个过程，我们需要先绘制疫情推广的速度。由于初期的数值是有限的，我们需要根据死亡人数倒推真实的疫情蔓延速度，同时通过这个速度，比较推广PPE及不推广PPE，对疫情的阻碍有多大作用。同时，我们要结合疫情的R值，及模拟不同程度的mask使用程度，判断推广PPE对疫情的阻碍，病人的住院率及死亡率会有什么作用。

这篇paper对于PPE效果的预测必须基于真实的疫情蔓延数字。这些数据可以从英国官网寻找，我们先将其画出，并包括一些重要的时间节点。但从以下图表可以看出，尽管第一波疫情及第二波疫情的死亡人数曲线非常类似，但确诊人数却差别很大。根据xxx，原始毒株及alpha毒株的致死率差距并无很大。因此，导致两者出现以上区别的原因是，在所有时期，官方的测量数据并不等于真实感染疫情的人数。这个现象有很多原因，包括无症状感染者，抗体检测的不足，官方检测的目标不同、患者因为各种原因（例如不想被隔离）主观上拒绝检测等等并且，在2020年初期疫情爆发的初期，由于官方检测力量的不足，确诊/报告的比例要远小于现在。因此，我们需要某种手段去推测真实的感染人数。同时，我们还要考虑covid-19存在的潜伏期，因此，我们需要用使用数学模型来预测在如果戴口罩的话，疫情的死亡人数是否会有变化。

*All Models are wrong, but some models are useful*

自从疫情爆发以来，由于病毒本身的特征，确诊数字远远小于感染数字，因此数据分析师，生物学家，政客已经尝试通过许多模型来预测正式的感染数字。毫无疑问的是，没有模型可以准确预测真实的确诊数字，但是一个sophisticated的模型可以提供非常有意义的数字。

我们将使用Compartmental models in epidemiology来预测口罩政策是否会改变疫情的死亡数字。Compartmental models作为传染病界广泛应用的数学模型，可以根据传染病的各种性质进行调整，来针对性预测指导传染病的预防和控制工作。在文章To mask or not to mask Modeling the potential for face mask中，作者根据新冠的特征对compartmental models进行了调整。对于最简单的Compartmental models，人群会被分为S(Susceptible), I(Infectious), or R(Recovered)三个群体，I为患病的群体，R为患病后康复的群体，而剩下未曾患病但又得病可能的即为S群体。由于新冠的一大特征是存在无症状患者，who没有住院但依然存在传染性。因此，我们额外添加A群体以代表无症状患者，而I群体即为有症状患者。由于新冠存在潜伏期，患者在感染病毒后几天内无症状也无传染性，这段期间的患者被称为暴露期，我们以E来代表这个群体。最后，H为hospitalized的群体，D为死亡的群体。

总人数N = S + E + I + A + R, where H is excluded since hospitalized persons are supposed not exposed to the general population and do not contribute to infection rates in the general community. [11]

| Letters | Compartments                      |
| ------- | --------------------------------- |
| $S$     | Susceptible people                |
| $I$     | Infectious peolpe with symptom    |
| $R$     | Recovered people                  |
| $A$     | Infectious peolpe without symptom |
| $E$     | Exposed people                    |
| $H$     | Hospitalized people               |
| $D$     | Dead People                       |

Compartmental models in epidemiology需要parameters以用于量化不同compartments的group之间转化的速率。因此，我们设立parameters如下

| Letters            | Parameters                                                 |
| ------------------ | ---------------------------------------------------------- |
| $\beta$            | the baseline infectious contact rate                       |
| $\sigma$           | the transition rate from the exposed to infectious class   |
| $\frac{1}{\sigma}$ | the disease incubation period                              |
| $\eta$             | the infectiousness of asymptomatic carriers                |
| $\alpha$           | fraction of infections that become symptomatic             |
| $\varphi$          | the rate at which symptomatic individuals are hospitalized |
| $\gamma_{A}$       | the recover rate - asymptomatic infectious                 |
| $\gamma_{I}$       | the recover rate - symptomatic infectious                  |
| $\gamma_{H}$       | the recover rate - hospitizlied                            |
| $\delta$           | the disease-induced death rate                             |

各Compartments的改变速率如下

| Changing Rate of Compartments                               | Explanation                                                  |
| ----------------------------------------------------------- | ------------------------------------------------------------ |
| $\frac{dS}{dt} = -\beta(t) (I + \eta A)\frac{S}{N}$         | $(I + \eta A) $ stands for the group that 有传染性，会以$\beta$的速率导致S的人群暴露。因此S中人群的改变速率为$\beta(t) (I + \eta A)\frac{S}{N} $ . |
| $\frac{dE}{dt} = \beta(t) (I + \eta A)\frac{S}{N}-\sigma E$ | $\beta(t) (I + \eta A)\frac{S}{N}$ 为每个时间单位增加的exposed的人群。Moreover，有一部分exposed的人群会转变为有症状或无症状感染者，因此exposed人群的改变速率为$\beta(t) (I + \eta A)\frac{S}{N}-\sigma E$. |
| $\frac{dI}{dt} = \alpha \sigma E - \varphi I - \gamma_{I}I$ | $\sigma E$为每个时间单位从exposed的人群转变为感染者的人数，其中有$\alpha$比例的人为有症状感染者。另外，有症状感染者中，每个时间单位有$\varphi I$的人住院，有$\gamma_{I} I$的人康复，因此I人群的改变速率为$\alpha \sigma E - \varphi I - \gamma_{I}I$. |
| $\frac{dA}{dt} = (1-\alpha) \sigma E - \gamma_{A}A$         | $(1-\alpha)\sigma E$为每个时间单位exposed人群转为无症状感染者的人数，$\gamma_{A}A$为每个时间单位无症状感染者康复的人数，因此A人群的改变速率为$(1-\alpha) \sigma E - \gamma_{A}A$. |
| $\frac{dH}{dt} = \varphi I - \delta H - \gamma_{H}H$        | $\varphi I$为每个时间单位有症状感染者需要住院的人数。另外，有症状感染者中，每个时间单位有$\delta H$的人死亡，而$\gamma_{H}H$的人会直复，因此H人群的改变速率为$\varphi I - \delta H - \gamma_{H}H$. |
| $\frac{dR}{dt}$                                             | $R$为所有康复人群的总和，因此每个时间单位，有$\gamma_{I} I + \gamma_{A} A + \gamma_{H} H$康复 |
| $\frac{dD}{dt}$                                             | 每个时间单位，住院的人中有$\delta H$的人数死亡               |



xxxx（真实感染预测 I.pdf）



根据以上的模型，我们可以得出一个比确诊数字更加接近于真实的感染人数的数字。我们可以通过这个数字，

 

|      |      |      |      |
| ---- | ---- | ---- | ---- |
|      |      |      |      |
|      |      |      |      |
|      |      |      |      |
|      |      |      |      |
|      |      |      |      |
|      |      |      |      |
|      |      |      |      |
|      |      |      |      |
|      |      |      |      |

 



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

### Appendix or appendices (if applicable)





# The SIR epidemic model

A simple mathematical description of the spread of a disease in a population is the so-called SIR model, which divides the (fixed) population of $N$ individuals into three "compartments" which may vary as a function of time, $t$:

- $S(t)$ are those susceptible but not yet infected with the disease;
- $I(t)$ is the number of infectious individuals;
- $R(t)$ are those individuals who have recovered from the disease and now have immunity to it.

The SIR model describes the change in the population of each of these compartments in terms of two parameters, $\beta$ and $\gamma$. $\beta$ describes the effective *contact rate* of the disease: an infected individual comes into contact with $\beta N$ other individuals per unit time (of which the fraction that are susceptible to contracting the disease is $S/N$). $\gamma$ is the mean recovery rate: that is, $1/\gamma$ is the mean period of time during which an infected individual can pass it on.

The differential equations describing this model were first derived by Kermack and McKendrick [*Proc. R. Soc. A*, **115**, 772 (1927)]:

\begin {align} \frac{\mathrm{d}S}{\mathrm{d}t} &= -\frac{\beta S I}{N},\\ \frac{\mathrm{d}I}{\mathrm{d}t} &= \frac{\beta S I}{N} - \gamma I,\\ \frac{\mathrm{d}R}{\mathrm{d}t} &= \gamma I. \end{align}



The following Python code integrates these equations for a disease characterised by parameters $\beta = 0.2$, $1/\gamma = 10\;\mathrm{days}$ in a population of $N=1000$ (perhaps 'flu in a school). The model is started with a single infected individual on day 0: $I(0)=1$. The plotted curves of $S(t)$, $I(t)$ and $R(t)$ are styled to look a bit nicer than Matplotlib's defaults.