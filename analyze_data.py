import pandas as pd

# --- Step 1 & 2: Load and Prepare Data (Same as before) ---
file_name = 'Online Retail.xlsx'
print(f"Loading data from '{file_name}'...")
try:
    df = pd.read_excel(file_name, dtype={'CustomerID': str})
    print("Data loaded successfully!")
except FileNotFoundError:
    print(f"Error: The file '{file_name}' was not found.")
    exit()

df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
latest_date = df['InvoiceDate'].max()
ninety_days_ago = latest_date - pd.Timedelta(days=90)
df_filtered = df[df['InvoiceDate'] >= ninety_days_ago].copy()


# --- Step 3: Isolate Discarded Items (Same as before) ---
discarded_df = df_filtered[df_filtered['Quantity'] < 0].copy()
discarded_df['DiscardedQuantity'] = discarded_df['Quantity'].abs()


# --- Step 4: Calculate Discard Frequency (Same as before) ---
discard_frequency = discarded_df.groupby(['StockCode', 'Description'])['DiscardedQuantity'].sum().reset_index()
discard_frequency = discard_frequency.sort_values(by='DiscardedQuantity', ascending=False)


# --- NEW: Step 5: Create the Final Table with Identifiers and Brand ---
print("\nBuilding the final table with brand and identifiers...")

# Let's call our final table 'final_table'.
final_table = discard_frequency.copy()

# 1. Independent Primary Identifier: 'StockCode'
# This is our unique product identifier. Let's rename it for clarity.
final_table = final_table.rename(columns={'StockCode': 'ProductID'})

# 2. Dependent Identifier: 'DiscardFrequency'
# This is the value we calculated. Let's rename 'DiscardedQuantity' for clarity.
final_table = final_table.rename(columns={'DiscardedQuantity': 'DiscardFrequency'})

# 3. Add the 'Brand' column.
# We will extract the first word from the 'Description' as the brand.
# We make sure the Description is a string first to avoid errors.
final_table['Brand'] = final_table['Description'].astype(str).apply(lambda x: x.split()[0])

# Reorder the columns to look clean.
final_table = final_table[['ProductID', 'Description', 'Brand', 'DiscardFrequency']]


# --- Display the Final Results ---
print("\n--- Final Table with Brand and Identifiers (Top 10) ---")
print(final_table.head(10))

# Save this new final table to a new CSV file.
output_filename = 'final_product_analysis.csv'
final_table.to_csv(output_filename, index=False)
print(f"\nSuccessfully saved the final table to '{output_filename}'")
print("This file is now ready for the visualization platform.")