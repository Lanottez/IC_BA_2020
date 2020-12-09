library(tidyverse)

# Look up documentation on mpg
?mpg

ggplot(data = mpg) +
  geom_point(mapping = aes(x = displ, y = hwy, color ="blue"))

# color outside of aes() function
ggplot(data = mpg) +
  geom_point(mapping = aes(x = displ, y = hwy), color ="blue")

# Look up the function details
?facet_grid

# midwest is another data frame that comes with ggplot2
# you can use View() to see the table in RStudio
midwest %>% View()

ggplot(data = mpg)+
  geom_point(mapping = aes(x = displ, y = hwy))

# facet technique
ggplot(data = mpg)+
  geom_point(mapping = aes(x = displ, y = hwy)) +
  facet_grid(vars(drv), vars(cyl), labeller = label_both)


