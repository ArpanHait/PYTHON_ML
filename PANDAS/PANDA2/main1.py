import pandas as pd
import matplotlib.pyplot as plt
import os

def analyze_employee_salaries(filepath="employees.csv"):
    """
    Loads employee data, visualizes salary distribution, identifies outliers,
    and prints a summary of the cleaning process.
    """
    # Step 1: Load the dataset with error handling
    try:
        df = pd.read_csv(filepath)
    except FileNotFoundError:
        print(f"Error: The file '{filepath}' was not found.")
        return

    # Step 2: Look at the initial salary column statistics
    print("Salary statistics (before cleaning):")
    print(df["Salary"].describe())

    # Step 3: Visualize salary distribution, save, and show the plot
    plt.figure(figsize=(8, 6))
    plt.boxplot(df["Salary"])
    plt.title("Salary Distribution with Outliers")
    plt.ylabel("Salary")
    plt.savefig("salary_outliers.png")
    print("\nSaved boxplot to 'salary_outliers.png'. Now displaying plot...")
    plt.show()  # <-- This will display the plot in a new window
    plt.close() # Frees up memory after the plot window is closed

    # Step 4: Identify outliers using a simple rule
    outliers = df[(df["Salary"] < 10000) | (df["Salary"] > 200000)]
    print("\nOutliers found (Salary < 10000 or > 200000):")
    print(outliers)

    # Step 5: Remove the outliers
    df_clean = df[(df["Salary"] >= 10000) & (df["Salary"] <= 200000)]
    print("\nDataset shape before removing outliers:", df.shape)
    print("Dataset shape after removing outliers:", df_clean.shape)

if __name__ == "__main__":
    # Construct an absolute path to the CSV file to avoid FileNotFoundError.
    # This makes the script runnable from any directory.
    script_dir = os.path.dirname(os.path.abspath(__file__))
    csv_path = os.path.join(script_dir, "employees.csv")
    
    analyze_employee_salaries(csv_path)