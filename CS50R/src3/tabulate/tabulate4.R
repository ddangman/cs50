# Demonstrates summing votes for each voting method with apply
# MARGIN=2 applies to columns

votes <- read.csv("votes.csv")
total_votes <- apply(votes, MARGIN = 2, FUN = sum)
total_votes
