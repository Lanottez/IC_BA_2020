install.packages("forecast")
install.packages("tseries")
library(forecast)
library(tseries)
library(ggplot2)

data <- read.csv(file = "shampoo.csv", header = TRUE)
shampoo <- ts(data[, 2], frequency = 12, start = c(2001, 1))
plot.ts(shampoo)
autoplot(shampoo)
ggtsdisplay(shampoo)

### stationarize time series
# take first order difference
shampoo.diff1 <- diff(shampoo, differences = 1)
autoplot(shampoo.diff1)

# stationary test
adf.test(shampoo.diff1)
pp.test(shampoo.diff1)
kpss.test(shampoo.diff1)
ndiffs(shampoo)

# seasonal stationarity
nsdiffs(shampoo)


### determine optimal p and q
# acf plot
acf(shampoo.diff1, lag.max = 20) # q <= 2 
ggAcf(shampoo.diff1)

# pacf plot
pacf(shampoo.diff1, lag.max = 20) # p <= 1
ggPacf(shampoo.diff1)

# choose optimal p and q based on information criteria
auto.arima(shampoo, trace = TRUE, ic = 'bic') 
# Best model: ARIMA(1,1,1)(0,0,1)[12] with drift (BIC=407.3)
# Second best: ARIMA(1,1,1) with drift (BIC=408.7)

# two candidate models
shampoo.m1 <- Arima(shampoo, order = c(1, 1, 1), 
                       seasonal = list(order = c(0, 0, 1), period = 12), include.drift = TRUE)
shampoo.m2 <- Arima(shampoo, order = c(1, 1, 1), include.drift = TRUE)

# in-sample one-step forecasts
accuracy(shampoo.m1)

# residual analysis
autoplot(shampoo.m1$residuals)
ggAcf(shampoo.m1$residuals)
checkresiduals(shampoo.m1)

# forecast
shampoo.f <- forecast(shampoo.m1, h = 6)
autoplot(shampoo.f)


### model evaluation
# Fit model with first 2.5-year of data
auto.arima(window(shampoo, end = c(2003, 6)), d = 1, trace = TRUE, ic = 'bic')

# two candidate models: ARIMA(0,1,2) with drift, ARIMA(1,1,1) with drift
m1 <- Arima(window(shampoo, end = c(2003, 6)), order = c(1, 1, 1), include.drift = TRUE)
m2 <- Arima(window(shampoo, end = c(2003, 6)), order = c(0, 1, 2), include.drift = TRUE)

# Apply fitted model to later data
m1.f <- Arima(window(shampoo, start = c(2003, 7)), model = m1)
m2.f <- Arima(window(shampoo, start = c(2003, 7)), model = m2)

# out-of-sample one-step ahead forecasts
accuracy(m1.f)
accuracy(m2.f)

# out-of-sample multi-step ahead forecasts
accuracy(forecast(m1, h = 6), window(shampoo, start = c(2003, 7)))
accuracy(forecast(m2, h = 6), window(shampoo, start = c(2003, 7)))
