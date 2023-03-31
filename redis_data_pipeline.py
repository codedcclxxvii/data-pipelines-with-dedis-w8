import pandas as pd
import psycopg2
import redis

# Redis client object
redis_host = 'redis-12345.redislabs.com'
redis_port = 12345
redis_password = 'password'
redis_client = redis.Redis(host=redis_host, port=redis_port, password=redis_password)

# Extract function
def extract(file_path, redis_key):
    data = pd.read_csv(file_path)
    redis_client.set(redis_key, data.to_json())
    return data

# Transform function
def transform(data):
    # Clean data
    data = data.dropna()
    data = data.drop_duplicates()

    # Structure data
    data = data.rename(columns={'duration': 'call_duration', 'cost': 'call_cost', 'destination': 'call_destination'})
    data['call_duration'] = pd.to_timedelta(data['call_duration'])
    data['call_cost'] = pd.to_numeric(data['call_cost'])
    data['call_date'] = pd.to_datetime(data['call_date'])

    # Format data
    data['call_destination'] = data['call_destination'].str.upper()

    return data

# Load function
def load(data, db_config):
    conn = psycopg2.connect(**db_config)
    cur = conn.cursor()

    # Create table
    cur.execute("CREATE TABLE IF NOT EXISTS call_logs (call_date TIMESTAMP, call_duration INTERVAL, call_cost NUMERIC, call_destination VARCHAR)")

    # Insert data
    for index, row in data.iterrows():
        cur.execute("INSERT INTO call_logs (call_date, call_duration, call_cost, call_destination) VALUES (%s, %s, %s, %s)", (row['call_date'], row['call_duration'], row['call_cost'], row['call_destination']))

    # Commit changes and close connection
    conn.commit()
    cur.close()
    conn.close()

# Data pipeline function
def data_pipeline(file_path, redis_key, db_config):
    # Extract data
    data = extract(file_path, redis_key)

    # Check if data exists in Redis cache
    cached_data = redis_client.get(redis_key)
    if cached_data is not None:
        data = pd.read_json(cached_data)

    # Transform data
    data = transform(data)

    # Load data into Postgres database
    load(data, db_config)

# Test the pipeline with a sample dataset
if __name__ == '__main__':
    file_path = 'customer_call_logs.csv'
    redis_key = 'customer_call_logs'
    db_config = {
        'host': 'localhost',
        'database': 'mydatabase',
        'user': 'myusername',
        'password': 'mypassword'
    }
    data_pipeline(file_path, redis_key, db_config)
