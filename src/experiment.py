from data_extraction import extract_data
from analysis import run_ab_test

def main():
    # Extract all data from the table.
    query = "SELECT * FROM user_engagement;"
    data = extract_data(query)
    
    # Save data to CSV (in the data/ folder)
    data.to_csv('data/engagement_data.csv', index=False)
    
    # Run the A/B test analysis.
    model = run_ab_test(data)
    
    # Interpret the result based on the p-value for 'variant'
    if model.pvalues.get('variant', 1) < 0.05:
        print("Statistically significant impact detected!")
    else:
        print("No significant difference detected.")

if __name__ == '__main__':
    main()
