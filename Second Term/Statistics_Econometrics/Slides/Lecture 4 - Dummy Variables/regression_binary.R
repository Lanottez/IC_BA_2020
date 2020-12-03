library(dplyr)
library(car)
library(ggplot2)

# Example 7.7
load("beauty.RData")
desc
data.male <- data %>% filter(female == 0)
male.m1 <- lm(log(wage) ~ belavg + abvavg + educ + exper, data = data.male)
data.female <- data %>% filter(female == 1)
female.m1 <- lm(log(wage) ~ belavg + abvavg + educ + exper, data = data.female)
stargazer(male.m1, female.m1, no.space = TRUE, align = TRUE)

# Interactions involving dummy variables
load("wage1.RData")
wage.m1 <- lm(log(wage) ~ female + educ + female:educ, data = data)
wage.m2 <- lm(log(wage) ~ female*educ, data = data)
summary(wage.m1)
linearHypothesis(wage.m1, c("female = 0", "female:educ = 0"))

data$female.educ <- data$female * data$educ
cor(data$female.educ, data$female)

data.female <- data %>% filter(female == 1)
summary(data.female$educ)
ggplot(data = data.female, aes(x = educ)) + geom_histogram()
sd(data.female$educ)

# Labor force participation by married women
load("mroz.RData")
fitted.inlf <- lm(inlf ~ educ + kidslt6, data = data)