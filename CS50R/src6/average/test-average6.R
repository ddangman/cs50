# Test stop if argument is non-numeric

source("average7.R")

test_that("`average` calculates mean", {
  expect_equal(average(c(1, 2, 3)), 2)
  expect_equal(average(c(-1, -2, -3)), -2)
  expect_equal(average(c(-1, 0, 1)), 0)
  expect_equal(average(c(-2, -1, 1, 2)), 0)
})

test_that("`average` returns NA with NAs in input", {
  expect_equal(suppressWarnings(average(c(1, NA, 3))), NA)
  expect_equal(suppressWarnings(average(c(NA, NA, NA))), NA)
})

test_that("`average` warns about NAs in input", {
  expect_warning(average(c(1, NA, 3)))
  expect_warning(average(c(NA, NA, NA)))
})

test_that("`average` stops if `x` is non-numeric", {
  expect_error(average(c("quack!")))
  expect_error(average(c("1", "2", "3")))
})
