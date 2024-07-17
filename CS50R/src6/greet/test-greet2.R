library(testthat)
# Describe greet

source("greet1.R")

describe("greet()", {
  it("can say hello to a user", {
    name <- "Carter"
    expect_equal(greet(name), "hello, Carter")
  })
})
