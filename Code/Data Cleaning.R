library(tidyverse)
library(data.table)
library(fastDummies)
library(ggplot2)
library(ggthemes)
library(corrplot)
library(caTools)
library(Amelia)
library(lubridate)
library(gridExtra)
library(janitor)

setwd("~/Documents/Fall Module 2/WDA/WDA Final Project")

#reading data into csv
ds1 <- read.csv('Monthly Datasets/202101-divvy-tripdata.csv')
ds2 <- read.csv('Monthly Datasets/202102-divvy-tripdata.csv')
ds3 <- read.csv('Monthly Datasets/202103-divvy-tripdata.csv')
ds4 <- read.csv('Monthly Datasets/202104-divvy-tripdata.csv')
ds5 <- read.csv('Monthly Datasets/202105-divvy-tripdata.csv')
ds6 <- read.csv('Monthly Datasets/202106-divvy-tripdata.csv')
ds7 <- read.csv('Monthly Datasets/202107-divvy-tripdata.csv')
ds8 <- read.csv('Monthly Datasets/202108-divvy-tripdata.csv')
ds9 <- read.csv('Monthly Datasets/202109-divvy-tripdata.csv')
ds10 <- read.csv('Monthly Datasets/202110-divvy-tripdata.csv')
ds11 <- read.csv('Monthly Datasets/202111-divvy-tripdata.csv')
ds12 <- read.csv('Monthly Datasets/202112-divvy-tripdata.csv')
ds13 <- read.csv('Monthly Datasets/202201-divvy-tripdata.csv')
ds14 <- read.csv('Monthly Datasets/202202-divvy-tripdata.csv')
ds15<- read.csv('Monthly Datasets/202203-divvy-tripdata.csv')
ds16 <- read.csv('Monthly Datasets/202204-divvy-tripdata.csv')
ds17 <- read.csv('Monthly Datasets/202205-divvy-tripdata.csv')

#combining all datasets into one dataset
df <- rbind(ds1, ds2, ds3, ds4, ds5, ds6, ds7, ds8, ds9, ds10, ds11, ds12, ds13
            ,ds14,ds15,ds16,ds17)

names(df)
summary(df)

#count missing values
colSums(is.na(df))


is.null(df$start_station_id)




