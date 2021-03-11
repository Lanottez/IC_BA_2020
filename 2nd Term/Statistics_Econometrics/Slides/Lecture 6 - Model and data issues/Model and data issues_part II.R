library(ggplot2)
library(dplyr)

#### Non-random sample
load("bwght.RData")
data <- data %>% mutate(rich = ifelse(faminc > median(faminc), 1, 0))
data$rich <- as.factor(data$rich)
ggplot(data, aes(x = cigs, y = bwght, color = rich)) + geom_point() + 
  geom_smooth(method='lm') + scale_color_brewer(palette="Set1")

data <- data %>% mutate(heavy = ifelse(bwght > median(bwght), 1, 0))
data$heavy <- as.factor(data$heavy)
ggplot(data, aes(x = cigs, y = bwght, color = heavy)) + geom_point() + 
  geom_smooth(method='lm') + scale_color_brewer(palette="Set1")


#### Outlier
load("rdchem.RData")
rdchem.m1 <- lm(rdintens ~ sales + profmarg, data)

ggplot(rdchem.m1, aes(.fitted, .stdresid)) + geom_point() + 
  stat_smooth(method = "loess") + xlab("Fitted Value") + ylab("Standardized Residuals")
ggplot(rdchem.m1, aes(.hat, .cooksd)) + geom_point() + 
  stat_smooth(method = "loess") + xlab("Leverage") + ylab("Cook's Distance")

# standardized residual
rstandard(rdchem.m1)

# leverage value
hatvalues(rdchem.m1)

# cooks distance
cooks.distance(rdchem.m1)

data.new <- data[-c(10), ]
rdchem.m2 <- lm(rdintens ~ sales + profmarg, data.new)