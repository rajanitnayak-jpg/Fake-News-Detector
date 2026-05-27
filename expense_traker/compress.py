import pandas as pd

# 1. Process and shrink the Fake news file to 1,000 rows
print("Processing fake.csv...")
df_fake = pd.read_csv('fake.csv')
df_fake_small = df_fake.head(1000)
df_fake_small.to_csv('fake_small.csv', index=False)

# 2. Process and shrink the True news file to 1,000 rows
print("Processing true.csv...")
df_true = pd.read_csv('true.csv')
df_true_small = df_true.head(1000)
df_true_small.to_csv('true_small.csv', index=False)

print("Successfully created smaller files! (fake_small.csv and true_small.csv)")