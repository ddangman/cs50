library("tidyverse")

# Remove selected columns using !c(col1, ...) or -c(col1, ...)
# use c(col1, ...)
dplyr::select(
  storms,
  !c(lat, long, pressure, tropicalstorm_force_diameter, hurricane_force_diameter)
)

