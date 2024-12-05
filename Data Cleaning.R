# Install necessary libraries
if(!require("skimr")) install.packages("skimr")
if(!require("dplyr")) install.packages("dplyr")
if(!require("stringr")) install.packages("stringr")

# Load the libraries
library(dplyr)
library(skimr)
library(stringr)

# Load the dataset
df <- read.csv("/Users/xuan/Downloads/week_data.csv")

# Display the first few rows of the dataset
head(df)

# Basic exploratory analysis of the dataset
dim(df) # Shape of the dataset
str(df) # Information about the dataset
summary(df) # Descriptive statistics
colSums(is.na(df)) # Count missing values in each column

# Rename a column
colnames(df)[colnames(df) == "search_quey_volume"] <- "search_query_volume"

# Check unique values in the 'pur_ASIN_share' column
unique(df$pur_ASIN_share)

# Adjust week logic
df$week <- str_replace_all(df$week, c("Week 1" = "Week 52+1", 
                                      "Week 2" = "Week 52+2", 
                                      "Week 3" = "Week 52+3"))

# Convert 'pur_ASIN_share' to numeric, replacing '-' and coercing errors
df$pur_ASIN_share <- as.numeric(str_replace_all(df$pur_ASIN_share, "-", ""))

# Check unique values in the 'pur_ASIN_share' column after conversion
unique(df$pur_ASIN_share)

# Count missing values in each column
colSums(is.na(df))

# Fill missing values in 'pur_ASIN_share' with the column mean
df$pur_ASIN_share[is.na(df$pur_ASIN_share)] <- mean(df$pur_ASIN_share, na.rm = TRUE)

# Drop extreme values and unrealistic rates
cleaned_df <- df %>%
  filter(search_query_volume <= 2000000 & clk_click_rate <= 100)

# Summarise the dataset
skim(cleaned_df)

dim(cleaned_df)

# Save the cleaned dataset to a CSV file
write.csv(cleaned_df, "cleaned_amazon_data.csv", row.names = FALSE)
