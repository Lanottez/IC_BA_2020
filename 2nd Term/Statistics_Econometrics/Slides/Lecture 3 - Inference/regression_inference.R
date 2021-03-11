# find critical values in R
qnorm(0.995)
qt(0.995, df = 522)

# Example 4.1
load("wage1.RData")
wage.m1 <- lm(log(wage) ~ educ + exper + tenure, data = data)
summary(wage.m1)

# hypothesis testing in R
install.packages("car")
library(car)
linearHypothesis(wage.m1, "educ = 2")

# confidence interval
confint(wage.m1, 'educ', level = 0.95)
confint(wage.m1, level = 0.95)

# A single linear combination of parameters
linearHypothesis(wage.m1, "educ - exper = 0")

# Example 4.9
load("bwght.RData")
bwght.ur <- lm(bwght ~ cigs + parity + faminc + motheduc + fatheduc, data = data)
summary(bwght.ur)
summary(data)

# remove observations with missing values
data.new <- na.omit(data)
bwght.ur <- lm(bwght ~ cigs + parity + faminc + motheduc + fatheduc, data = data.new)
summary(bwght.ur)
sum(bwght.ur$residuals^2)

bwght.r <- lm(bwght ~ cigs + parity + faminc, data = data.new)
summary(bwght.r)
sum(bwght.r$residuals^2)
qf(0.95, 2, 1185)

linearHypothesis(bwght.ur, c("motheduc = 0", "fatheduc = 0"))