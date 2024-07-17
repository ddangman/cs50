library("tidyverse")

# Find only rows about hurricanes

filter(
  select(
    storms,
    !c(lat, long, pressure, ends_with("diameter"))
  ),
  status == "hurricane"
)

# if using multiple packages with functions having same name
dplyr::filter(
  dplyr::select(
    storms,
    !c(lat, long, pressure, ends_with("diameter"))
  ),
  status == "hurricane"
)