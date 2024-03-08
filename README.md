   1. Read the input CSV file and load the data into a suitable data structure in Python, such as a pandas DataFrame.
   2. Sorted the data by employee identifier and effective date to ensure chronological order.
   3. Iterated through each row of the DataFrame and perform the following transformations:
        -Determined the effective date and end date for each historical record based on the next record's effective date or assigning a far-future date for the latest record.
        -Handled missing data by inheriting values from the most recent past record for the same employee.
        Transform columnar data into a row-based format.
    4.Generated a new DataFrame representing the historical records with the transformed data.
    5. Wrote the new DataFrame to a CSV file formatted for historical data analysis.
