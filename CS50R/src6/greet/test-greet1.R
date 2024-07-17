# Test greet

source("greet1.R")

test_that("`greet` says hello to a user", {
  expect_equal(greet("Carter"), "hello, Carter")
})
