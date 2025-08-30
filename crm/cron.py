# crm/cron.py
from datetime import datetime

def log_crm_heartbeat():
    """
    Logs a heartbeat message every 5 minutes to /tmp/crm_heartbeat_log.txt
    """
    log_file = "/tmp/crm_heartbeat_log.txt"
    timestamp = datetime.now().strftime("%d/%m/%Y-%H:%M:%S")
    with open(log_file, "a") as f:
        f.write(f"{timestamp} CRM is alive\n")

