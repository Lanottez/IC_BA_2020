install.packages("sandwich")
install.packages("lmtest")
library(sandwich)
library(lmtest)

#### BP test and White test
load("wage1.RData")
wage.m1 <- lm(wage ~ educ + exper + tenure, data)

# residual plot
library(ggplot2)
ggplot(wage.m1, aes(.fitted, .resid)) + geom_point() + geom_hline(yintercept = 0)

# BP test
bptest(wage.m1)

# White test
fitted.wage <- wage.m1$fitted.values
bptest(wage.m1, ~ fitted.wage + I(fitted.wage^2))


#### robust t test and F test
# robust vcov
vcov.robust <- vcovHC(wage.m1, "HC1")

# t test
coeftest(wage.m1, vcov = vcov.robust)

# F test
library(car)
linearHypothesis(wage.m1, "educ - exper = 0", white.adjust = "hc1")
