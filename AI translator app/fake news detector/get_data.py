import pandas as pd

print("--- Collecting WELFake Dataset ---")

# Correct and full direct download link for the multi-domain WELFake dataset
url = "https://githubusercontent.com"

try:
    print("Downloading data from internet, please wait for 30 seconds...")
    
    # Loading only the top 15,000 rows for fast and memory-safe collection
    df = pd.read_csv(url, nrows=15000, on_bad_lines='skip')
    
    # Saving the collected data into your folder as 'dataset.csv'
    df.to_csv('dataset.csv', index=False)
    
    print("\n✅ Data collection successful!")
    print(f"Total news records collected: {len(df)}")
    print("The 'dataset.csv' file has been successfully created in your folder.")

except Exception as e:
    print(f"🚨 Error occurred: {e}")
    print("Please ensure your internet connection is active and try again.")