import json
import requests

# Set the API key and application key
api_key = '<api key>' #took out my api key for security
app_key = '<app key>' #took out my app key for security

# Create the monitor
monitor_data = {
    'query': 'avg(last_1h):avg:system.load.1{host:MacBook-Pro.local} by {host} > 8',
    'name': 'High CPU load on {{host.name}}',
    'message': 'test',
    'type': 'query alert',
    'priority': 4,
    'thresholds': {'critical': 1.0},
    'notify_no_data': False,
    'no_data_timeframe': 20,
}

headers = {
    'DD-API-KEY': api_key,
    'DD-APPLICATION-KEY': app_key
}

response = requests.post(
    'https://api.datadoghq.com/api/v1/monitor', json=monitor_data, headers=headers)

# Check the response
print("\n Response code: %d \n" % response.status_code)
print("\n" + format(response.text))
