import pandas as pd
import matplotlib.pyplot as plt

# --- Step 1: Load the Final Analyzed Data ---
# We will use the CSV file we created in the last step.
file_name = 'final_product_analysis.csv'
print(f"Loading analyzed data from '{file_name}'...")

try:
    final_table = pd.read_csv(file_name)
    print("Data loaded successfully!")
except FileNotFoundError:
    print(f"Error: The file '{file_name}' was not found.")
    print("Please make sure this script is in the same folder as your CSV file.")
    exit()

# --- Step 2: Prepare the Data for Plotting ---
# We only want to plot the top 10 most discarded items to keep the chart clean.
top_10_products = final_table.head(10)

# We need to sort the values for a clean-looking plot (from lowest to highest).
top_10_products = top_10_products.sort_values(by='DiscardFrequency', ascending=True)

print("\nPreparing to plot the Top 10 most discarded products.")


# --- Step 3: Create and Save the Bar Chart ---
# Create a horizontal bar chart for better readability of product names.
plt.figure(figsize=(12, 8)) # Set the figure size to be larger.

plt.barh(top_10_products['Description'], top_10_products['DiscardFrequency'], color='skyblue')

# Add titles and labels for clarity.
plt.title('Top 10 Most Discarded Products (Last 90 Days)', fontsize=16)
plt.xlabel('Total Quantity Discarded', fontsize=12)
plt.ylabel('Product Description', fontsize=12)

# Make sure the layout is tight so labels don't get cut off.
plt.tight_layout()

# Save the plot to an image file.
output_plot_filename = 'discarded_products_trend.png'
plt.savefig(output_plot_filename)

print(f"\n--- Success! ---")
print(f"Visualization has been saved as '{output_plot_filename}'")
print("You have now completed all the steps of your project!")