# Step 1: Import pandas
import pandas as pd
import os

def analyze_student_data(filepath="students.csv"):
    """
    Loads student data, separates features and labels, and prints a summary.
    """
    # Step 2: Load the dataset
    try:
        df = pd.read_csv(filepath)
    except FileNotFoundError:
        print(f"Error: The file '{filepath}' was not found. Please ensure it is in the same folder.")
        return

    # Step 3: View the first few rows
    print("First 5 rows of the dataset:")
    print(df.head())

    # Step 4: Separate features and label
    feature_columns = ["Age", "Salary", "Hours_Studied"]
    label_column = "Passed"
    features = df[feature_columns]
    label = df[label_column]

    print("\nFeatures (X):")
    print(features.head())

    print("\nLabel (y):")
    print(label.head())

if __name__ == "__main__":
    # Get the absolute path to the directory where the script is located
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # Join the script's directory path with the CSV filename
    csv_path = os.path.join(script_dir, "students.csv")
    
    analyze_student_data(csv_path)