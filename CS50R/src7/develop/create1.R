# Demonstrates initializing a package

# Load devtools, tidyverse for package creation
library(devtools)
library(tidyverse)

# Create a new folder for package
dir.create("ducksay")

# Set working directory to package directory
setwd("ducksay")

# Create a blank DESCRIPTION file
file.create("DESCRIPTION")

# Create a LICENSE file to fill in license details
file.create("LICENSE")
