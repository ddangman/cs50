# Demonstrates subsetting a vector with a logical vector

load("temps.RData")

# select outliers
temps[which(temps < 0 | temps > 60)]

temps[temps < 0 | temps > 60]

filter <- temps < 0 | temps > 60
temps[filter]



# drop outliers
temps[-which(temps < 0 | temps > 60)]

