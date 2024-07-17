# Demonstrates identifying NA values with `is.na`

chicks <- read.csv("chicks.csv")

is.na(chicks$weight)
chicks$chick[is.na(chicks$weight)]
which(is.na(chicks$weight))

!is.na(chicks$weight)
chicks$chick[!is.na(chicks$weight)]
which(!is.na(chicks$weight))
chicks <- chicks[!is.na(chicks$weight),]

soybean_chicks <- subset(chicks, feed == "soybean")
mean(soybean_chicks$weight)
