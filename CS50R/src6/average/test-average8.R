source("average7.R")

test_that("`average` calculates mean", {
  expect_equal(average(c(3, 3, 4)), 3.3)
  expect_equal(average(c(3, 3, 4)), 3.3, tolerance = 0.03)
})