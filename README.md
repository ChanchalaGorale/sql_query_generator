# SQL query Generator - OpenAI App

    Created simple flask app where user query is converted to SQL command using GTP 3.5 turbo model which later one used to query the real time database to fetch the results that are passed to react app api call.

# Steps to Follow

## Clone repo
    - git init
    - git clone https://github.com/hypothesistribetechnology/sql_query_generator.git
    - sql_query_generator

## Set up virtual environment
    ```python -m venv venv```

    ```source venv/bin/activate```

## Install Requirements

    pip install -r requirements.txt

## Set up database 

   ``` python databse.py```

## App OpenAI API Key

    1. Create ``.env`` file
    2. Add OPENAI_API_KEY

    **Note**: OPENAI_API_KEY can be created from your openai developers dashboard

## Run App

    ```python app.py```





    

