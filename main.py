import pandas as pd
from blockchain import add_to_blockchain
from database import create_db, insert_data
from encryption import generate_key, encrypt_data

# Load dataset
df = pd.read_csv("dataset/healthcare_dataset.csv")

# Generate key
key = generate_key("securepassword123")

# Encrypt each row
df["Encrypted_Data"] = df.astype(str).apply(
    lambda x: encrypt_data(",".join(x), key), axis=1
)

print("Encryption Completed 🔐")
print(df[["Encrypted_Data"]].head())

# Create database
create_db()

# Store encrypted data
insert_data(df["Encrypted_Data"].tolist())

print("Data Stored in Database 💾")

# Add to blockchain
chain = add_to_blockchain(df["Encrypted_Data"].tolist())

print("Blockchain Created 🔗")
print(chain[:2])  # show first 2 blocks