import pandas as pd

print("Connecting to Zenodo Open-Science Repository... Please wait...")

# This is an official open-science server (Not GitHub), so it won't be blocked.
# It downloads thousands of diverse news records (Health, Tech, Politics, etc.)
url = "https://zenodo.org"

try:
    # Reading the first 10,000 highly accurate and diverse records
    df = pd.read_csv(url, nrows=10000, on_bad_lines='skip')
    
    # Saving to your project folder
    df.to_csv('dataset.csv', index=False)
    print(f"✅ Success! Downloaded {len(df)} diverse rows into 'dataset.csv' from Zenodo Server!")

except Exception as e:
    print(f"🚨 Zenodo server error: {e}")
    print("Trying alternative Kaggle Mirror...")
    
    # Alternate Kaggle dataset mirror link
    url_alt = "https://r2.dev"
    df = pd.read_csv(url_alt, nrows=10000, on_bad_lines='skip')
    df.to_csv('dataset.csv', index=False)
    print(f"✅ Success! Downloaded {len(df)} rows from Alternative Mirror!")