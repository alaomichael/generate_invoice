#!/bin/bash

# Set the CSV file path
CSV_FILE="receipt_data.csv"

# Check if the CSV file exists
if [ ! -f "$CSV_FILE" ]; then
    echo "Error: CSV file not found!"
    exit 1
fi

# # Run the Python script
# python3 generate_receipt.py "$CSV_FILE"

# # Check if the Python script ran successfully
# if [ $? -eq 0 ]; then
#     echo "Receipts generated successfully!"
# else
#     echo "Error generating receipts!"
# fi

# Run the Python script
python generate_receipt.py "$CSV_FILE" 2>&1 | tee error_log.txt

# Check if the Python script ran successfully
if [ $? -eq 0 ]; then
    echo "Receipts generated successfully!"
else
    echo "Error generating receipts! See error_log.txt for details."
fi

