library(data.table)
library(tidyverse)
speedData <- scan("Data/lec_car_data_clean.txt", character(), quote = "")
timeData <- scan("Data/lec_time_data_clean.txt", character(), quote = "")

lapData <- data.table(timeData, speedData)

lapData$timeData <- as.numeric(lapData$timeData)
lapData$timeData <- lapData$timeData / 1000
lapData$speedData <- as.numeric(lapData$speedData)

ggplot(lapData, aes(x = timeData, y = speedData)) +
  geom_line(color = "red", size = 1.5) +
  labs(x = "Time (s)", y = "Speed (KPH)", title = "Leclerc Qualifying Lap Speed") +
  ylim(0, 370) +
  theme_minimal()


