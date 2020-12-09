library(tidyverse)

data(mpg)



# density(): calculates kernel density estimates
density(mpg$hwy)
# calculate teh density estimates
d <- with(mpg, density(hwy))
# save the results as a data frame
tmp <- data.frame(hwy=d$x, density=d$y)
tmp %>% ggplot(aes(hwy,density)) +
  geom_line() +
  geom_area(aes(x=hwy,y=density),
            data = filter(tmp, between(hwy, 20, 30)),
            alpha=0.2, fill="#00BFC4")




# before sorting
ggplot(data = mpg, mapping = aes(x = class)) +
  geom_bar()

# looking into where the order comes from
data(mpg)
mpg$class <- as.factor(mpg$class)
levels(mpg$class)

mpg$class <- fct_infreq(mpg$class)
levels(mpg$class)

# plot once sorted
ggplot(data = mpg, mapping = aes(x = class)) +
  geom_bar()

# reset
data(mpg)
# or sort on the fly
ggplot(data = mpg, mapping = aes(x=fct_infreq(class)))+
  geom_bar()



ggplot(data = mpg) +
  geom_point(mapping = aes(x = displ, y = hwy)) +
  geom_smooth(mapping = aes(x = displ, y = hwy))


# 2d density plot
ggplot(data = mpg, mapping = aes(x = displ, y = hwy)) +
  geom_point() +
  geom_density_2d(aes(color = class))

?stat_summary()

ggplot(data = diamonds) +
  geom_bar(mapping = aes(x = cut, fill = clarity), position = "identity")



?geom_path

ggplot(data = diamonds) +
  geom_bar(mapping = aes(x = cut))

ggplot(diamonds) +
  geom_bar(aes(x = cut))

?geom_bar

?stat_summary
?geom_pointrange


?geom_smooth

ggplot(data = mpg, aes(x = hwy)) +
  geom_density(alpha = .2, fill= "#00BFC4", color = 0) +
  theme_bw()

ggplot(data = mpg, aes(x = hwy)) +
  geom_density(alpha = .2, fill= "#00BFC4", aes(y = ..count..)) +
  theme_bw()



ggplot(data = mpg, aes(x = displ, fill=drv)) +
  geom_density(aes(y = ..count..), alpha = .2) +
  geom_line(stat='density') + theme_bw()


?geom_jitter
?geom_line

ggplot(data=mpg,mapping=aes(x=displ,y=hwy,color = drv))+
  geom_point()+
  geom_point()
