library("tidyverse")

# Find most powerful hurricane for each year
# slice_head() returns only 1st row of each group_by()

hurricanes <- read.csv("hurricanes.csv")

hurricanes |>
  group_by(year) |>
  arrange(desc(wind)) |>
  slice_head()
