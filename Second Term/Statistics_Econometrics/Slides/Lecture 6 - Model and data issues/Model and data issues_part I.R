#### Functional form misspecifation
library(lmtest)
load("hprice1.RData")

# RESET test
house.m1 <- lm(price ~ lotsize + sqrft + bdrms, data)
resettest(house.m1, type = "fitted")

#### Variable Selections
install.packages("leaps")
library(leaps)
load("bwght.RData")
data.new <- na.omit(data)
bwght.model.search <- regsubsets(bwght ~ faminc + fatheduc + motheduc + parity 
                                 + male + white + cigs, data.new, nbest = 3)
plot(bwght.model.search, scale = "adjr2")
plot(bwght.model.search, scale = "bic")

# stepwise search
bwght.null <- lm(bwght ~ 1, data.new)
bwght.full <- lm(bwght ~ faminc + fatheduc + motheduc + parity + male + white 
                 + cigs, data.new)
step(bwght.null, scope = list(lower = bwght.null, upper = bwght.full), 
     direction = "forward")
step(bwght.full, data.new, direction = "backward")
step(bwght.null, scope = list(lower = bwght.null, upper = bwght.full), 
     direction = "both")

n <- nrow(data.new)
step(bwght.null, scope = list(lower = bwght.null, upper = bwght.full), 
     direction = "forward", k = log(n))


#### Prediction
library(ggplot2)
load("wage1.RData")
wage.m1 <- lm(wage ~ educ, data)
wage.m2 <- lm(wage ~ I(educ-12), data)
ggplot(data = data, aes(x = educ, y = wage)) + geom_point() + stat_smooth(method = "lm")

newdata <- data.frame(educ = 12)
predict(wage.m1, newdata, interval = "confidence", level = 0.95)
predict(wage.m1, newdata, interval = "predict", level = 0.95)

wage.pred <- predict(wage.m1, interval="prediction")
data.new <- cbind(data, wage.pred)
ggplot(data = data.new, aes(x = educ, y = wage)) + geom_point() + stat_smooth(method = "lm") +
  geom_line(aes(y=lwr), color = "red") + geom_line(aes(y=upr), color = "red")


wage.m3 <- lm(log(wage) ~ educ, data)
predicted.logwage <- predict(wage.m3, newdata, interval = "none")
predicted.wage <- mean(exp(wage.m3$residuals)) * exp(predicted.logwage)
