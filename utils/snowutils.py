import snowflake.connector

class SnowflakeConnector:
    def __init__(self, account, user, password, warehouse, database, schema):
        self.account = account
        self.user = user
        self.password = password
        self.warehouse = warehouse
        self.database = database
        self.schema = schema
        self.connection = None
        self.cursor = None

    def connect(self):
        """
        Establish a connection to Snowflake.
        """
        self.connection = snowflake.connector.connect(
            user=self.user,
            password=self.password,
            account=self.account,
            warehouse=self.warehouse,
            database=self.database,
            schema=self.schema
        )
        self.cursor = self.connection.cursor()

    def execute_query(self, query):
        """
        Execute a SQL query.
        """
        if not self.connection or not self.cursor:
            raise Exception("Connection not established. Call connect() method first.")

        self.cursor.execute(query)
        return self.cursor.fetchall()

    def close_connection(self):
        """
        Close the connection.
        """
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()

# Example usage:

# Replace these with your Snowflake account details
account = 'dgnohgj-nhb45211'
user = 'SHIV'
password = 'Rohini@03'
warehouse = 'WH1'
database = 'VIRAT'
schema = 'SS1'

# Create an instance of SnowflakeConnector
snowflake_conn = SnowflakeConnector(account, user, password, warehouse, database, schema)

# Connect to Snowflake
snowflake_conn.connect()

# Execute a query
query_result = snowflake_conn.execute_query("select * from VIRAT.SS1.EMPLOYEES;")

# Print the result
print("Current Date in Snowflake:", query_result[0][0])
print(query_result)
# Close the connection
snowflake_conn.close_connection()