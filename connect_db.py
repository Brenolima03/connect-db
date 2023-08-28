import cx_Oracle
import pandas as pd

# Configure the connection: 'user/password@host/database
connStr = ''

# List of queries
queries = [
    "select a from b where c and d", 
    "select e from f where g"
]

# Execute the queries and return the results as a DataFrame
def execute_query(connection, query):
    with connection.cursor() as cursor:
        cursor.execute(query)
        columns = [desc[0] for desc in cursor.description]
        result = cursor.fetchall()
        df = pd.DataFrame(result, columns=columns)
    return df

# Make the connection with the database
connection = cx_Oracle.connect(connStr)

# Execute queries and print or process results

for query in queries:
    result_df = execute_query(connection, query)
    print(result_df) # Or do something else with the DataFrame

# Close the database connection after executing queries
connection.close()