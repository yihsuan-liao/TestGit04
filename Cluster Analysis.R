#Elbow Method
# Install and load required libraries
if (!require("factoextra")) install.packages("factoextra")
if (!require("stats")) install.packages("stats")

library(factoextra) # For visualisation and clustering functions
library(stats)      # For kmeans()

# Assuming 'scaled_data' is the scaled dataset used for clustering
# Replace 'scaled_data' with your actual scaled dataset

# Calculate WCSS for different numbers of clusters
wcss <- c()
for (k in 1:10) {
  kmeans_model <- kmeans(scaled_data, centers = k, nstart = 25) # Perform K-means clustering
  wcss[k] <- kmeans_model$tot.withinss # Total within-cluster sum of squares
}

# Plot the Elbow Method
plot(1:10, wcss, type = "b", pch = 19, frame = TRUE, 
     xlab = "Number of Clusters", ylab = "WCSS (Within-Cluster Sum of Squares)", 
     main = "Elbow Method for Optimal Clusters")

#K-Means Cluster
# Install and load required libraries
if (!require("dplyr")) install.packages("dplyr")
if (!require("ggplot2")) install.packages("ggplot2")
if (!require("scales")) install.packages("scales")

library(dplyr)
library(ggplot2)

# Extract the 'search_query_score' column
search_query_score <- cleaned_df$search_query_score

# Standardise the search_query_score
search_query_score_scaled <- scale(search_query_score)

# Apply K-Means Clustering
set.seed(42) # For reproducibility
kmeans_model <- kmeans(search_query_score_scaled, centers = 3, nstart = 25)

# Add cluster information to the dataset
cleaned_df$Cluster <- kmeans_model$cluster

# Analyse the clusters by examining the mean search_query_score for each cluster
cluster_summary <- cleaned_df %>%
  group_by(Cluster) %>%
  summarise(mean_search_query_score = mean(search_query_score))

# Sort the clusters by the average search_query_score
sorted_clusters <- cluster_summary %>%
  arrange(mean_search_query_score)

# Assign labels based on adjusted interpretation (lower scores = higher correlation)
cluster_labels <- c("High Correlation", "Moderate Correlation", "Low Correlation")
sorted_clusters$Correlation_Category <- cluster_labels

# Map the labels to the clusters
label_mapping <- setNames(cluster_labels, sorted_clusters$Cluster)
cleaned_df$Correlation_Category <- factor(cleaned_df$Cluster, levels = names(label_mapping), 
                                          labels = label_mapping)

# Visualise the Clustering
ggplot(cleaned_df, aes(x = 1:nrow(cleaned_df), y = search_query_score, colour = factor(Cluster))) +
  geom_point(size = 2) +
  scale_colour_manual(values = c("green", "blue", "red")) +
  labs(title = "K-Means Clustering of Search Query Score into 3 Clusters",
       x = "Index", 
       y = "Search Query Score", 
       colour = "Cluster") +
  theme_minimal()

