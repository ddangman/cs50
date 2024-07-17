# Demonstrates summing votes for each candidate with apply
# MARGIN=1 applies to rows

votes <- read.csv("votes.csv")
total_votes <- apply(votes, MARGIN = 1, FUN = sum)
total_votes
