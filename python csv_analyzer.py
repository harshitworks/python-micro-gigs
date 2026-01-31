import csv

def analyze_csv(file_path, column_name):
    total_rows = 0
    total_value = 0

    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)

        for row in reader:
            total_rows += 1
            total_value += float(row[column_name])

    average = total_value / total_rows if total_rows > 0 else 0

    print("📊 CSV Analysis Result")
    print("---------------------")
    print(f"Total Rows: {total_rows}")
    print(f"Average of '{column_name}': {average}")

# main program
file_path = input("Enter CSV file path: ")
column_name = input("Enter column name to calculate average: ")

analyze_csv(file_path, column_name)
