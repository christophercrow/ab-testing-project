from sqlalchemy import create_engine, text
import numpy as np
import pandas as pd

# Update the connection string with your PostgreSQL credentials and database name.
DATABASE_URL = 'postgresql://postgres:postgres@localhost:5432/ab_testing_project'
engine = create_engine(DATABASE_URL)

def create_table():
    # Drop table if exists and create a new one.
    create_query = """
    DROP TABLE IF EXISTS user_engagement;
    CREATE TABLE user_engagement (
        user_id SERIAL PRIMARY KEY,
        engagement_metric NUMERIC,
        variant INTEGER,  -- 0 for control, 1 for test
        signup_date DATE
    );
    """
    with engine.connect() as conn:
        conn.execute(text(create_query))
        conn.commit()
    print("Table 'user_engagement' created.")

def generate_data(n=2000):
    np.random.seed(42)  # For reproducibility
    n_control = n // 2
    n_test = n - n_control

    # Control group: mean = 100, std = 15
    control_engagement = np.random.normal(100, 15, n_control)
    # Test group: mean = 115, std = 15 (approx 15% increase)
    test_engagement = np.random.normal(115, 15, n_test)

    # Generate random signup dates within the last 180 days
    today = pd.to_datetime('2025-02-27')
    control_dates = today - pd.to_timedelta(np.random.randint(0, 180, n_control), unit='D')
    test_dates = today - pd.to_timedelta(np.random.randint(0, 180, n_test), unit='D')

    control_data = pd.DataFrame({
        'engagement_metric': control_engagement,
        'variant': 0,
        'signup_date': control_dates
    })
    test_data = pd.DataFrame({
        'engagement_metric': test_engagement,
        'variant': 1,
        'signup_date': test_dates
    })

    data = pd.concat([control_data, test_data]).reset_index(drop=True)
    return data

def populate_data():
    data = generate_data(n=2000)
    # Use to_sql with if_exists='append' to insert data into the table
    data.to_sql('user_engagement', engine, if_exists='append', index=False)
    print(f"Inserted {len(data)} pseudo-data records into user_engagement.")

if __name__ == '__main__':
    create_table()
    populate_data()
