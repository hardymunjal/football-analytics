# Import Libraries
library(dplyr)
library(tidyr)
library(tidyverse)


# Code
## Select required columns
raw_data = read_csv('data/match_data.csv')
colnames(data)

data_df = raw_data[,c("Date", "HomeTeam" ,"AwayTeam","FTHG","FTAG",
                  "FTR","HTHG","HTAG","HTR","HS","AS","HST","AST","HF","AF",
                  "HC","AC","HY","AY","HR","AR")]

betting_df = raw_data[,c("Date", "HomeTeam" ,"AwayTeam","FTHG","FTAG",
                  "FTR","HTHG","HTAG","HTR","HS","AS","HST","AST","HF","AF",
                  "HC","AC","HY","AY","HR","AR","B365H","B365D","B365A")]

## Data Cleaning

### Match Data
str(data_df)

# Check missing values for each column
sapply(data_df, function(x) sum(is.na(x)))

# Remove Missing values
cleaned_df = na.omit(data_df)

# Save new file
write.csv(cleaned_df, "cleaned_match_data.csv", row.names = FALSE)


### Betting Data

# Check missing values for each column
sapply(betting_df, function(x) sum(is.na(x)))

# Remove Missing values
betting_df = na.omit(betting_df)

# Save new file
write.csv(betting_df, "match_data_with_odds.csv", row.names = FALSE)