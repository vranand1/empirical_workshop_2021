########
## Unit Tests in R
########
## example taken from https://towardsdatascience.com/unit-testing-in-r-68ab9cc8d211

#install.packages("testthat")
library(testthat)
source("../examples/increment.R", chdir = TRUE)

test_that("single number", {
  expect_equal(increment(-1), 0)
  expect_equal(increment(0), 1)
})

test_that("vectors", {
  expect_equal(increment(c(0,1)), c(1,2))
})

test_that("empty vector", {
  expect_equal(increment(c()), c())
})

test_that("test NA", {
  expect_true(is.na(increment(NA)))
})

test_file("../examples/unit_testing.R")
