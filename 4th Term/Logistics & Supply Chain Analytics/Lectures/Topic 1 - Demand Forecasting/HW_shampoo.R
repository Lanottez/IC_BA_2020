library(forecast)
library(ggplot2)

data <- read.csv(file = "shampoo.csv", header = TRUE)
shampoo <- ts(data[, 2], frequency = 12, start = c(2001, 1))
autoplot(shampoo)
shampoo %>% stl(s.window = "period") %>% autoplot

### Model estimation
# using HoltWinters
shampoo.HW <- HoltWinters(shampoo, gamma = FALSE)

# HW is sensitive to starting values
shampoo.HW2 <- HoltWinters(shampoo, gamma = FALSE, optim.start = c(alpha = 0, beta = 0), 
                           l.start = 200, b.start = -2.6)
plot(shampoo.HW)
lines(fitted(shampoo.HW2)[,2], col = "blue", lty = 2)

# in-sample one-step forecast
sqrt(shampoo.HW$SSE/(length(shampoo)-2))
sqrt(shampoo.HW2$SSE/(length(shampoo)-2))


# using ets
shampoo.ets <- ets(shampoo, model = "AAN")
shampoo.ets2 <- ets(shampoo, model = "ZZZ")

# in-sample fit
accuracy(shampoo.ets)


# out-of-sample forecast
shampoo.HW.f <- forecast(shampoo.HW, h = 6)
shampoo.ets.f <- forecast(shampoo.ets, h = 6)

plot(shampoo.HW.f)
lines(fitted(shampoo.HW.f), col = "blue")
lines(fitted(shampoo.ets), col = "red", lty = 2)
lines(shampoo.ets.f$mean, col = "red", lty = 2)


### model evaluation
# Fit model with first 2.5 years of data
m1 <- HoltWinters(window(shampoo, end = c(2003, 6)), gamma = FALSE)
m2 <- ets(window(shampoo, end = c(2003, 6)), model = "AAN")

# out-of-sample multi-step forecasts
accuracy(forecast(m1, h = 6), window(shampoo, start = c(2003, 7)))
accuracy(forecast(m2, h = 6), window(shampoo, start = c(2003, 7)))
