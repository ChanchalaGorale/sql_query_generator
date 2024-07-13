import pandas as pd
import sqlite3


# Connect to SQLite database
conn = sqlite3.connect('bytegenie_test.db')
cursor = conn.cursor()

cursor.execute('DROP TABLE IF EXISTS company')
cursor.execute('DROP TABLE IF EXISTS event')
cursor.execute('DROP TABLE IF EXISTS people')

cursor.execute(
    '''
CREATE TABLE event (
    event_id SERIAL PRIMARY KEY,
    event_logo_url TEXT,
    event_name TEXT NOT NULL,
    event_start_date DATE,
    event_end_date DATE,
    event_venue TEXT,
    event_country TEXT,
    event_description TEXT,
    event_active_days INT,
    event_industry TEXT,
    event_url TEXT UNIQUE NOT NULL
)
'''
)

cursor.execute(
    '''
CREATE TABLE company (
    company_id SERIAL PRIMARY KEY,
    company_logo_url TEXT,
    company_logo_text TEXT,
    company_name TEXT NOT NULL,
    relation_to_event TEXT,
    event_url TEXT,
    company_revenue TEXT,
    n_employees INT,
    company_phone TEXT,
    company_founding_year INT,
    company_address TEXT,
    company_industry TEXT,
    company_overview TEXT,
    homepage_url TEXT,
    linkedin_company_url TEXT,
    homepage_base_url TEXT UNIQUE NOT NULL,
    company_logo_url_on_event_page TEXT,
    company_logo_match_flag BOOLEAN,
    min_employees INT,
    max_employees INT,
    FOREIGN KEY (event_url) REFERENCES events(event_url)
)
'''
)


cursor.execute(
    '''
CREATE TABLE people (
    person_id SERIAL PRIMARY KEY,
    first_name TEXT,
    middle_name TEXT,
    last_name TEXT,
    job_title TEXT,
    person_city TEXT,
    person_state TEXT,
    person_country TEXT,
    email_pattern TEXT,
    homepage_base_url TEXT NOT NULL,
    duration_in_current_job INT,
    duration_in_current_company INT,
    email TEXT,
    FOREIGN KEY (homepage_base_url) REFERENCES companies(homepage_base_url)
)
'''
)

conn.commit()
cursor.close()

# Function to load CSV data into SQLite table
def load_csv_to_sqlite(csv_file, table_name, ):
    df = pd.read_csv("processed_data/"+csv_file)
    df.to_sql(table_name, conn, if_exists='replace', index=False)

# Load data into the events table
load_csv_to_sqlite('event_info.csv', 'event')

# Load data into the companies table
load_csv_to_sqlite('company_info.csv', 'company')

# Load data into the people table
load_csv_to_sqlite('people_info.csv', 'people')

conn.commit()
conn.close()