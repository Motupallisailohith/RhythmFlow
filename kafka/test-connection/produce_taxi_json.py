import csv
import os
from json import dumps
from kafka import KafkaProducer
from time import sleep
from datetime import datetime

#set the env variable to an IP if not localhost
KAFKA_ADDRESS=os.getenv('KAFKA_ADDRESS', 'localhost') # cite: 1

producer = KafkaProducer(bootstrap_servers=[f'{KAFKA_ADDRESS}:9092'], # cite: 1
                         key_serializer=lambda x: dumps(x).encode('utf-8'), # cite: 1
                         value_serializer=lambda x: dumps(x, default=str).encode('utf-8')) # cite: 1

file = open('data/rides.csv') # cite: 1

csvreader = csv.reader(file) # cite: 1
header = next(csvreader) # cite: 1
for row in csvreader: # cite: 1
    key = {"vendorId": int(row[0])} # cite: 1
    
    value = {"vendorId": int(row[0]), # cite: 1
            "passenger_count": int(row[3]), # cite: 1
            "trip_distance": float(row[4]), # cite: 1
            "pickup_location": int(row[7]), # cite: 1
            "dropoff_location": int(row[8]), # cite: 1
            "payment_type": int(row[9]), # cite: 1
            "total_amount": float(row[16]), # cite: 1
            "pickup_datetime": datetime.now() # cite: 1
            }

    producer.send('yellow_taxi_ride.json', value=value, key=key) # cite: 1
    print("producing") # cite: 1
    sleep(1) # cite: 1