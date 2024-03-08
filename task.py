import pandas as pd

# Read the input CSV file
input_file = "input.csv"
employee_data = pd.read_csv(input_file)

# Initialize variables for storing transformed data
transformed_data = []

# Iterate through each row of the DataFrame
for index, row in employee_data.iterrows():
    # Extract relevant data
    employee_id = index + 1  # Assuming each row represents a unique employee
    date_of_joining = row['Date of Joining']
    date_of_exit = row['Date of Exit']
    
    # Compensation history
    compensation_data = [
        {'Effective Date': date_of_joining, 'End Date': row['Compensation 1 date'], 'Compensation': row['Compensation']},
        {'Effective Date': row['Compensation 1 date'], 'End Date': row['Compensation 2 date'], 'Compensation': row['Compensation 1']},
        {'Effective Date': row['Compensation 2 date'], 'End Date': date_of_exit if pd.notna(date_of_exit) else '2100-01-01', 'Compensation': row['Compensation 2']}
    ]
    
    # Review history
    review_data = [
        {'Effective Date': row['Review 1 date'], 'End Date': row['Review 2 date'], 'Review': row['Review 1']},
        {'Effective Date': row['Review 2 date'], 'End Date': date_of_exit if pd.notna(date_of_exit) else '2100-01-01', 'Review': row['Review 2']}
    ]
    
    # Engagement history
    engagement_data = [
        {'Effective Date': row['Engagement 1 date'], 'End Date': row['Engagement 2 date'], 'Engagement Score': row['Engagement 1']},
        {'Effective Date': row['Engagement 2 date'], 'End Date': date_of_exit if pd.notna(date_of_exit) else '2100-01-01', 'Engagement Score': row['Engagement 2']}
    ]
    
    # Combine all historical records
    historical_records = []
    historical_records.extend(compensation_data)
    historical_records.extend(review_data)
    historical_records.extend(engagement_data)
    
    # Append records to transformed data
    transformed_data.extend([{
        'EmployeeID': employee_id,
        'Effective Date': record['Effective Date'],
        'End Date': record['End Date'],
        'Compensation': record.get('Compensation', None),
        'Review': record.get('Review', None),
        'Engagement Score': record.get('Engagement Score', None)
    } for record in historical_records])

# Create a new DataFrame from the transformed data
historical_employee_records = pd.DataFrame(transformed_data)

# Write the new DataFrame to a CSV file
output_file = "historical_employee_records.csv"
historical_employee_records.to_csv(output_file, index=False)

# Print confirmation
print("Historical records successfully created and saved to:", output_file)
