import pandas as pd
from sqlalchemy import create_engine

# Update the connection string with your PostgreSQL credentials and database name.
DATABASE_URL = 'postgresql://postgres:postgres@localhost:5432/ab_testing_project'
engine = create_engine(DATABASE_URL)

def extract_data(query: str) -> pd.DataFrame:
    """
    Execute a SQL query and return the results as a DataFrame.
    
    :param query: SQL query to execute.
    :return: pandas DataFrame containing the query results.
    """
    return pd.read_sql(query, engine)

if __name__ == '__main__':
    query = "SELECT * FROM user_engagement LIMIT 10;"
    df = extract_data(query)
    print(df)
