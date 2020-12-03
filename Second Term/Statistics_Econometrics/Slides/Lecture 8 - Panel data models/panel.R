# Example 9.7. City crime rates
load("crime2.RData")
crime.87 <- lm(crmrte ~ unem, data, subset = year == 87)

# estimation with plm
install.packages("plm")
library(plm)

# create a panel data frame
data$city <- rep(1:46, each = 2)
data.p <- pdata.frame(data, index = c("city", "year"))

# first difference estimation
crime.fd <- plm(crmrte ~ d87 + unem, data, index = c("city", "year"), 
                effect = "individual", model = "fd")

# fixed effects estimation
crime.fe <- plm(crmrte ~ d87 + unem, data, index = c("city", "year"), 
                effect = "individual", model = "within")
