import pandas as pd
import statsmodels.formula.api as smf
from data_extraction import extract_data  # Import our extraction function

def run_ab_test(data: pd.DataFrame):
    """
    Run A/B test analysis using an OLS regression model.
    Model: engagement_metric ~ variant
    """
    model = smf.ols('engagement_metric ~ variant', data=data).fit()
    print(model.summary())
    return model

if __name__ == '__main__':
    # Query the entire user_engagement table directly from the database.
    query = "SELECT * FROM user_engagement;"
    data = extract_data(query)
    print("Data extracted from the database:")
    print(data.head())
    run_ab_test(data)
