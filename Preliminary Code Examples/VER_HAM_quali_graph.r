library(data.table)
library(tidyverse)
HAM2021SpeedData <- scan("Data/ham_car_data_2021_clean.txt", character(), quote = "")
HAM2021TimeData <- scan("Data/ham_time_data_2021_clean.txt", character(), quote = "")
HAM2021LapData <- data.table(HAM2021TimeData, HAM2021SpeedData)
HAM2021LapData$HAM2021TimeData <- as.numeric(HAM2021LapData$HAM2021TimeData)
HAM2021LapData$HAM2021TimeData <- HAM2021LapData$HAM2021TimeData / 1000
HAM2021LapData$HAM2021SpeedData <- as.numeric(HAM2021LapData$HAM2021SpeedData)
HAM2022SpeedData <- scan("Data/ham_car_data_2022_clean.txt", character(), quote = "")
HAM2022TimeData <- scan("Data/ham_time_data_2022_clean.txt", character(), quote = "")
HAM2022LapData <- data.table(HAM2022TimeData, HAM2022SpeedData)
HAM2022LapData$HAM2022TimeData <- as.numeric(HAM2022LapData$HAM2022TimeData)
HAM2022LapData$HAM2022TimeData <- HAM2022LapData$HAM2022TimeData / 1000
HAM2022LapData$HAM2022SpeedData <- as.numeric(HAM2022LapData$HAM2022SpeedData)
VER2021SpeedData <- scan("Data/ver_car_data_2021_clean.txt", character(), quote = "")
VER2021TimeData <- scan("Data/ver_time_data_2021_clean.txt", character(), quote = "")
VER2021LapData <- data.table(VER2021TimeData, VER2021SpeedData)
VER2021LapData$VER2021TimeData <- as.numeric(VER2021LapData$VER2021TimeData)
VER2021LapData$VER2021TimeData <- VER2021LapData$VER2021TimeData / 1000
VER2021LapData$VER2021SpeedData <- as.numeric(VER2021LapData$VER2021SpeedData)
VER2022SpeedData <- scan("Data/ver_car_data_2022_clean.txt", character(), quote = "")
VER2022TimeData <- scan("Data/ver_time_data_2022_clean.txt", character(), quote = "")
VER2022LapData <- data.table(VER2022TimeData, VER2022SpeedData)
VER2022LapData$VER2022TimeData <- as.numeric(VER2022LapData$VER2022TimeData)
VER2022LapData$VER2022TimeData <- VER2022LapData$VER2022TimeData / 1000
VER2022LapData$VER2022SpeedData <- as.numeric(VER2022LapData$VER2022SpeedData)

ggplot() +
  geom_line(data = HAM2021LapData, aes(x = HAM2021TimeData, y = HAM2021SpeedData, color = "Hamilton")) +
  geom_line(data = VER2021LapData, aes(x = VER2021TimeData, y = VER2021SpeedData, color = "Verstappen")) +
  labs(title = "2021 Lap Time and Speed Comparison",
       x = "Lap Time (s)", y = "Speed (km/h)",
       color = "Driver") +
  scale_color_manual(values = c("red", "blue"),
                     labels = c("Hamilton", "Verstappen"),
                     name = "Driver") +
  theme_classic()

ggplot() +
  geom_line(data = HAM2022LapData, aes(x = HAM2022TimeData, y = HAM2022SpeedData, color = "Hamilton")) +
  geom_line(data = VER2022LapData, aes(x = VER2022TimeData, y = VER2022SpeedData, color = "Verstappen")) +
  labs(title = "2022 Lap Time and Speed Comparison",
       x = "Lap Time (s)", y = "Speed (km/h)",
       color = "Driver") +
  scale_color_manual(values = c("red", "blue"),
                     labels = c("Hamilton", "Verstappen"),
                     name = "Driver") +
  theme_classic()
