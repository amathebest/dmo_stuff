# file input e estrazione della dataframe
file_name = "C:/Users/Matteo/Dropbox/University/11/DMO/dmo_stuff/progetto/dataset.csv"
data <- read.csv(file_name, sep = ";", header = TRUE)
dt = data.frame(data)
head(dt)

cor(dt)
