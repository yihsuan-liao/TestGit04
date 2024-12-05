# Load necessary libraries
if(!require("ggplot2")) install.packages("ggplot2")
if(!require("reshape2")) install.packages("reshape2")
if(!require("RColorBrewer")) install.packages("RColorBrewer")

library(ggplot2)
library(reshape2)
library(RColorBrewer)

#Date Standardised
scaled_data <- scale(cleaned_df[, c("clk_click_rate", "cart_add_rate", "pur_purchase_rate")])
correlation_matrix <- cor(scaled_data)

# Correlation Heatmap
# Select columns for correlation analysis
correlation_data <- cleaned_df[, c("clk_click_rate", "cart_add_rate", "pur_purchase_rate")]

# Calculate the correlation matrix
correlation_matrix <- cor(correlation_data, use = "complete.obs")

# Melt the correlation matrix for ggplot
melted_corr <- melt(correlation_matrix)

# Plot the heatmap
ggplot(data = melted_corr, aes(x = Var1, y = Var2, fill = value)) +
  geom_tile(color = "white") +
  scale_fill_gradient2(low = "blue", high = "red", mid = "white", 
                       midpoint = 0, limit = c(-1, 1), space = "Lab", 
                       name = "Correlation") +
  theme_minimal() +
  theme(axis.text.x = element_text(angle = 45, vjust = 1, hjust = 1)) +
  labs(title = "Correlation Heatmap: Click, Cart Add, and Purchase Rate", x = "", y = "") +
  geom_text(aes(label = round(value, 2)), color = "white", size = 4)

