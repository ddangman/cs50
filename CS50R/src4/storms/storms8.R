library("tidyverse")

# Keep only first observation about each hurricane
# if two storms have the same name, we further identify them by year
# .keep_all=TRUE prevents other columns from being dropped
# . prefix character used to reduce probability of collision with possible column named "keep_all"

storms |>
  select(!c(lat, long, pressure, ends_with("force_diameter"))) |>
  filter(status == "hurricane") |>
  arrange(desc(wind), name) |>
  distinct(name, year, .keep_all = TRUE)
