# Tally votes for favorite shows
# note whitespace and capitalization duplicates

shows <- read.csv("shows.csv")

shows |>
  group_by(show) |>
  summarize(votes = n()) |>
  ungroup() |>
  arrange(desc(votes))
