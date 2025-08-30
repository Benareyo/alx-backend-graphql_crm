from datetime import datetime
from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport

LOG_FILE = "/tmp/crm_heartbeat_log.txt"

def log_crm_heartbeat():
    # Append heartbeat message
    with open(LOG_FILE, "a") as f:
        f.write(f"{datetime.now().strftime('%d/%m/%Y-%H:%M:%S')} CRM is alive\n")

    # Optional: Query GraphQL hello field
    transport = RequestsHTTPTransport(
        url="http://localhost:8000/graphql",
        verify=False,
        retries=3,
    )
    client = Client(transport=transport, fetch_schema_from_transport=True)
    query = gql(
        """
        query {
            hello
        }
        """
    )
    try:
        client.execute(query)
    except Exception:
        pass  # ignore errors

