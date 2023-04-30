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

# Reading Data into csv
ds1 <- read.csv('Monthly Datasets/202105-divvy-tripdata.csv')
ds2 <- read.csv('Monthly Datasets/202106-divvy-tripdata.csv')
ds3 <- read.csv('Monthly Datasets/202107-divvy-tripdata.csv')
ds4 <- read.csv('Monthly Datasets/202108-divvy-tripdata.csv')
ds5 <- read.csv('Monthly Datasets/202109-divvy-tripdata.csv')
ds6 <- read.csv('Monthly Datasets/202110-divvy-tripdata.csv')
ds7 <- read.csv('Monthly Datasets/202111-divvy-tripdata.csv')
ds8 <- read.csv('Monthly Datasets/202112-divvy-tripdata.csv')
ds9 <- read.csv('Monthly Datasets/202201-divvy-tripdata.csv')
ds10 <- read.csv('Monthly Datasets/202202-divvy-tripdata.csv')
ds11<- read.csv('Monthly Datasets/202203-divvy-tripdata.csv')
ds12 <- read.csv('Monthly Datasets/202204-divvy-tripdata.csv')
ds13 <- read.csv('Monthly Datasets/202205-divvy-tripdata.csv')

#combining all datasets into one dataset
ds <- rbind(ds1, ds2, ds3, ds4, ds5, ds6, ds7, ds8, ds9, ds10, ds11, ds12, ds13)

names(ds)

summary(ds)

#processing for duplicates, there are no duplicates
Dup_rides <- ds[duplicated(ds$ride_id)|duplicated(ds$ride_id, fromLast=TRUE),]
Dup_rides

#negative times, swap values for negative times
negative_time <- filter(ds, ended_at < started_at)
summary(negative_time)
head(negative_time,10)
i <- which(ds$ended_at < ds$started_at)
v1 <- ds$started_at[i]
v2 <- ds$ended_at[i]
ds$ended_at[i] <- v1
ds$started_at[i] <- v2

#location outliers
data1 <- ds
start_lat_count <- data1 %>% count(start_lat)
start_lng_count <- data1 %>% count(start_lng)
end_lat_count <- data1 %>% count(end_lat)
end_lng_count <- data1 %>% count(end_lng)

b1 <- ggplot(start_lat_count, aes(y=start_lat)) + geom_boxplot()+ labs(title="Start Latitude", y = "Latitude")
b2 <- ggplot(start_lng_count, aes(y=start_lng)) + geom_boxplot()+ labs(title="Start Longitude", y = "Longitude")+coord_flip()
b3 <- ggplot(end_lat_count, aes(y=end_lat)) + geom_boxplot()+ labs(title="End Latitude", y = "Latitude")
b4 <- ggplot(end_lng_count, aes(y=end_lng)) + geom_boxplot()+ labs(title="End Longitude", y = "Longitude")+coord_flip()

summary(data1)
grid.arrange(b1, b2, b3, b4, ncol=2, nrow = 2)

#data conversion
data2 <- data1
data2$started_at = as.POSIXlt(data2$started_at)
data2$ended_at = as.POSIXlt(data2$ended_at)

#filter location outliers
position_outlier <- filter(data2, start_lat > 43 | start_lng > -80 | end_lng < -88.5 )
position_outlier


data3 <- filter(data2, start_lng < -80)
data3 <- filter(data3, end_lng > -88.5)
summary(data3)
#add distance and time
data4 <- data3 %>%
  
  mutate(square_distance = if_else(start_lat*end_lat*start_lng*end_lng*((end_lat-start_lat)+(end_lng-start_lng)) == 0, 0 , 
                                   round(6371000*2*pi*(abs(end_lat-start_lat)+abs(end_lng-start_lng))/360,2),0),
         
         straight_distance = if_else(start_lat*end_lat*start_lng*end_lng*((end_lat-start_lat)+(end_lng-start_lng)) == 0, 0 , 
                                     round(((6371000*2*pi*abs(end_lat-start_lat)/360)^2 + (6371000*2*pi*abs(end_lng-start_lng)/360)^2)^(1/2),2),0),
         
         total_time = as.numeric(ended_at-started_at, units="mins"),
  )

colnames(data4) <- c("bike_type","start_time","end_time","station_name","start_lat","start_lng","end_lat","end_lng","user_type","square_distance","straight_distance","total_time")

summary(data4)
head(data4,10)

# find number of outliers
stats_sd <- fivenum(data4$square_distance)
iqr_sd <- (nth(stats_sd,4)-nth(stats_sd,2))
lower_fence_sd <- nth(stats_sd,2)-iqr_sd*1.5
upper_fence_sd <- nth(stats_sd,4)+iqr_sd*1.5

stats_tt <- fivenum(data4$total_time)
iqr_tt <- (nth(stats_tt,4)-nth(stats_tt,2))
lower_fence_tt <- nth(stats_tt,2)-iqr_tt*1.5
upper_fence_tt <- nth(stats_tt,4)+iqr_tt*1.5

outliers_dt <- filter(data4, square_distance < lower_fence_sd | square_distance > upper_fence_sd | total_time < lower_fence_tt | total_time > upper_fence_tt)

summary(outliers_dt)


#remove inconsistencies
data5 <- data4[-which(duplicated(data4)), ]
data5 <- filter(data4, (square_distance/1000)/(total_time/60) < 20*1.609 | total_time < 1)

summary(data5)

#lat long range box plot
start_lat_count <- data5 %>% count(start_lat)
start_lng_count <- data5 %>% count(start_lng)
end_lat_count <- data5 %>% count(end_lat)
end_lng_count <- data5 %>% count(end_lng)

c1 <- ggplot(start_lat_count, aes(y=start_lat)) + geom_boxplot()+ labs(title="Start Latitude", x="", y = "Latitude")
c2 <- ggplot(start_lng_count, aes(y=start_lng)) + geom_boxplot()+ labs(title="Start Longitude", x="", y = "Longitude")+coord_flip()
c3 <- ggplot(end_lat_count, aes(y=end_lat)) + geom_boxplot()+ labs(title="End Latitude", x="", y = "Latitude")
c4 <- ggplot(end_lng_count, aes(y=end_lng)) + geom_boxplot()+ labs(title="End Longitude", x="", y = "Longitude")+coord_flip()
c5 <- ggplot(data5, aes(x=user_type, y=square_distance/1000)) + geom_boxplot() +
  stat_summary(fun = "mean", geom = "point", shape = 8, size = 2, color = "red")+
  labs(title="Square Distance", x="User", y="Miles")
c6 <- ggplot(data5, aes(x=user_type, y=total_time)) + geom_boxplot() +
  stat_summary(fun = "mean", geom = "point", shape = 8, size = 2, color = "red")+
  labs(title="Total Time", x="User", y="minutes")

grid.arrange(c1, c2, c3, c4, ncol=2, nrow = 2)
grid.arrange(c5,c6, ncol=2, nrow = 1)

