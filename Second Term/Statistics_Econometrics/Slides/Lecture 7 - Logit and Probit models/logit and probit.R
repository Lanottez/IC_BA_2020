# Example 17.1
load("mroz.RData")

### binary response model estimation
inlf.lpm <- glm(inlf ~ nwifeinc + educ + exper + expersq + age 
                + kidslt6 + kidsge6, family = "gaussian", data)

inlf.lpm.lm <- lm(inlf ~ nwifeinc + educ + exper + expersq + age 
                  + kidslt6 + kidsge6, data)

inlf.probit <- glm(inlf ~ nwifeinc + educ + exper + expersq + age 
                   + kidslt6 + kidsge6, family = "binomial"(link = "probit"), data)

inlf.logit <- glm(inlf ~ nwifeinc + educ + exper + expersq + age
                  + kidslt6 + kidsge6, family = "binomial"(link = "logit"), data)


### deviance
# deviance = sum of squared deviance residuals
summary(residuals(inlf.logit, type = "deviance"))
sum(residuals(inlf.logit, type = "deviance")^2)
inlf.logit$deviance

# deviance = -2 * log likelihood
(-2) * logLik(inlf.logit)


### goodness of fit
# pseudo r-squared
1 - inlf.logit$deviance/inlf.logit$null.deviance

# information criteria
AIC(inlf.logit)
BIC(inlf.logit)

# confusion matrix
library(caret)
inlf.predicted <- ifelse(inlf.logit$fitted.values < 0.5, 0, 1)
inlf.predicted <- as.factor(inlf.predicted)
confusionMatrix(inlf.predicted, as.factor(data$inlf), positive = "1")


### LR test
# test for overall significance
library(lmtest)
lrtest(inlf.logit)
LR.overall <- 1 - pchisq(inlf.logit$null.deviance - inlf.logit$deviance, 
                        df = inlf.logit$df.null - inlf.logit$df.residual)

# hypothesis testing
library(car)
linearHypothesis(inlf.logit, c("exper = 0", "expersq = 0"))

# confidence intervals
confint(inlf.logit)


### variable selection
inlf.null <- glm(inlf ~ 1, family = "binomial"(link = "logit"), data)
inlf.full <- glm(inlf ~ nwifeinc + educ + exper + expersq + age
                + kidslt6 + kidsge6, family = "binomial"(link = "logit"), data)
step(inlf.null, scope = list(lower = inlf.null, upper = inlf.full), direction = "forward")
step(inlf.full, direction = "backward")


### prediction 
new.ob = data.frame(nwifeinc = 10.91, educ = 12, exper = 14, expersq = 14^2,
                     age = 32, kidslt6 = 1, kidsge6 = 0)
predict(inlf.logit, newdata = new.ob, type = "link")
predict(inlf.logit, newdata = new.ob, type = "response")

xb <- sum(cbind(1, new.ob) * inlf.logit$coefficients)
phat <- exp(xb)/(1 + exp(xb))


### interpretation of logit model
# partial effects in logit model
mean(inlf.logit$fitted.values * (1 - inlf.logit$fitted.values)) * inlf.logit$coefficients

# non-linear partial effects
new.ob <- with(data, data.frame(nwifeinc = mean(nwifeinc), educ = mean(educ), exper = mean(exper),
                    expersq = mean(expersq), age = mean(age), kidslt6 = c(0, 1, 2), kidsge6 = 1))

# partial effect of having the first kid less than 6
predict(inlf.logit, newdata = new.ob[2, ], type = "response") - 
        predict(inlf.logit, newdata = new.ob[1, ], type = "response")
# partial effect of having the second kid less than 6
predict(inlf.logit, newdata = new.ob[3, ], type = "response") - 
        predict(inlf.logit, newdata = new.ob[2, ], type = "response")