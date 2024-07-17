library("tidyverse")

# select() has helper functions:
# contains()
# ends_with()
# starts_with()

select(
  storms,
  !c(lat, long, pressure, ends_with("diameter"))
)
