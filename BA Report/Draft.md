### Whether Wider Public Use of Facial Covering could Save Livings of England During the First Wave

Name: Qian Zhang

CID number: 01939418

Report title: 

Word count: 3093

### Abstract (suggest 150 words)









|      |      |
| ---- | ---- |
|      |      |
|      |      |
|      |      |
|      |      |
|      |      |
|      |      |



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



