# Demonstrates using custom package

library(ducksay)

name <- readline("What's your name? ")
greeting <- ducksay(paste("hello,", name))
cat(greeting)
