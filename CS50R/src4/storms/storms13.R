library("tidyverse")

# Find number of hurricanes per year

hurricanes <- read.csv("hurricanes.csv")

# default naming
hurricanes |>
  group_by(year) |>
  summarize(n())

# named column
hurricanes |>
  group_by(year) |>
  summarize(hurricanes = n())