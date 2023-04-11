library(data.table)
library(tidyverse)
HAMRacePace <- read.csv("Data/2022/ham_monza.csv")
VERRacePace <- read.csv("Data/2022/ver_monza.csv")
HAMRacePace <-
    HAMRacePace %>%
    mutate(driver = "Hamilton")
VERRacePace <-
    VERRacePace %>%
    mutate(driver = "Verstappen")

racePace <- rbind(HAMRacePace, VERRacePace)
avgLapTime <- racePace %>%
  group_by(driver, compound) %>%
  summarize(avgTimeSeconds = mean(lapTime)/1000)

ggplot(avgLapTime, aes(x = compound, y = avgTimeSeconds, fill = driver)) +
  geom_bar(stat = "identity", position = "dodge") +
  labs(x = "Tire Compound", y = "Average Lap Time (Seconds)", fill = "Driver") +
  ggtitle("Average Lap Time by Tire Compound and Driver") +
  coord_cartesian(ylim=c(80,100))

