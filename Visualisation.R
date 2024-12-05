# Install and load required libraries
if (!require("ggplot2")) install.packages("ggplot2")
if (!require("dplyr")) install.packages("dplyr")
if (!require("tidyr")) install.packages("tidyr")

library(ggplot2)
library(dplyr)

# Calculate the average rates for each cluster
metrics <- c("clk_click_rate", "cart_add_rate", "pur_purchase_rate")
cluster_avg <- cleaned_df %>%
  group_by(Cluster) %>%
  summarise(across(all_of(metrics), mean, na.rm = TRUE))

# Convert Metric to a factor to ensure consistent ordering
cluster_avg_long$Metric <- factor(cluster_avg_long$Metric, 
                                  levels = c("clk_click_rate", "cart_add_rate", "pur_purchase_rate"))

# Automatically map cluster numbers to the desired labels
cluster_labels <- c("Moderate correlation", "Low correlation", "High correlation")

# Create the bar chart
ggplot(cluster_avg_long, aes(x = factor(Cluster), y = Average_Rate, fill = Metric)) +
  geom_bar(stat = "identity", position = position_dodge(width = 0.8), width = 0.7) +
  scale_fill_manual(values = c("#4682B4", "#FF6347", "#32CD32")) +  
  labs(title = "Average Click, Cart, and Purchase Rates by Cluster",
       x = "Cluster",
       y = "Average Rate",
       fill = "Metrics") +
  scale_x_discrete(labels = cluster_labels) +  # Assign the labels based on cluster numbers
  theme_minimal()



# Keyword Table
# Load necessary libraries
if (!require("dplyr")) install.packages("dplyr")
if (!require("tidyverse")) install.packages("tidyverse")

library(dplyr)
library(tidyverse)

# Split the `search_query` into individual words and create a word frequency dataset
word_counts <- cleaned_df %>%
  mutate(search_query = str_split(search_query, "\\s+")) %>% # Split search queries into words
  unnest(search_query) %>% # Expand the list of words into individual rows
  group_by(Cluster, search_query) %>%
  summarise(Frequency = n(), .groups = "drop") # Count frequency of each word by cluster

# Get the top 10 keywords for Cluster 3
top_keywords_cluster3 <- word_counts %>%
  filter(Cluster == 3) %>%
  arrange(desc(Frequency)) %>%
  slice_head(n = 10) %>%
  pull(search_query)

# Filter data for the top 10 keywords across all clusters
top_keywords_data <- word_counts %>%
  filter(search_query %in% top_keywords_cluster1) %>%
  pivot_wider(names_from = Cluster, values_from = Frequency, values_fill = list(Frequency = 0))

# Rename columns for better readability
colnames(top_keywords_data)[-1] <- paste0("Cluster ", colnames(top_keywords_data)[-1])

# Sort the table by Cluster 1 frequency for better display
top_keywords_data <- top_keywords_data %>%
  arrange(desc(`Cluster 3`))

# Display the table
print("Top 10 Keywords for Cluster 3 Across All Clusters:")
print(top_keywords_data)
