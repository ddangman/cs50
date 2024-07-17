library("tidyverse")

# Introduce slice_max

hurricanes <- read.csv("hurricanes.csv")

hurricanes |>
  group_by(year) |>
  slice_max(order_by = wind)

hurricanes |>
  group_by(year) |>
  slice_max(order_by = wind) |>
  filter(year >= 1980 & year <= 1990)
