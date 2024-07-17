# Demonstrates removing NA values and resetting row names

chicks <- read.csv("chicks.csv")
sum(is.na(chicks$weight))

chicks <- subset(chicks, !is.na(weight))
rownames(chicks)

# update rownames after dropping missing data
rownames(chicks) <- NULL
rownames(chicks)
# we did NOT update chick number
