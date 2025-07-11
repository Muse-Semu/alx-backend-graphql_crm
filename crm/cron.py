from datetime import datetime
import os

from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport

def log_crm_heartbeat():
    # Time format: DD/MM/YYYY-HH:MM:SS
    timestamp = datetime.now().strftime('%d/%m/%Y-%H:%M:%S')
    log_message = f"{timestamp} CRM is alive\n"

    # Append heartbeat log
    with open('/tmp/crm_heartbeat_log.txt', 'a') as log_file:
        log_file.write(log_message)

    # Optional GraphQL hello query to check endpoint
    try:
        transport = RequestsHTTPTransport(
            url='http://localhost:8000/graphql',
            verify=False,
            retries=2,
        )
        client = Client(transport=transport, fetch_schema_from_transport=True)

        hello_query = gql("""query { hello }""")
        result = client.execute(hello_query)
        print(f"Heartbeat GraphQL Response: {result.get('hello')}")
    except Exception as e:
        print(f"GraphQL health check failed: {e}")
