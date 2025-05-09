import os
import pandas as pd
import pymongo
from pymongo import MongoClient

def import_csv_to_mongodb():
    client = MongoClient("mongodb://localhost:27017/")

    db = client["famous_painters_db"]

    bike_store_path = "C:/Users/athar/Documents/USC/551/Project/dsci551project/FamousPaintingDB"

    csv_files = [f for f in os.listdir(bike_store_path) if f.endswith('.csv')]

    for csv_file in csv_files:
        # Get the collection name (file name without extension)
        collection_name = os.path.splitext(csv_file)[0]
        
        # Read the CSV file
        file_path = os.path.join(bike_store_path, csv_file)
        df = pd.read_csv(file_path)
        
        # Convert DataFrame to list of dictionaries
        records = df.to_dict('records')
        
        # Create or get the collection
        collection = db[collection_name]
        
        # Insert the records into the collection
        if records:
            collection.insert_many(records)
            print(f"Imported {len(records)} records into {collection_name} collection")
        else:
            print(f"No records to import for {collection_name}")

    print("All CSV files have been imported to the bikestore database.") 

if __name__ == "__main__":
    import_csv_to_mongodb()