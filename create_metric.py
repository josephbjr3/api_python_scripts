import json
import requests

# Set the API key and application key
api_key = '1363684daf076a499b10c52082d542ae'
app_key = '0ca46e3fe140999decb263add084df1b6346909c'

# Create the monitor
monitor_data = {
    'query': 'avg(last_1h):avg:system.load.1{host:MacBook-Pro.local} by {host} > 8',
    'name': 'High CPU load on {{host.name}}',
    'message': 'test',
    'type': 'query alert',
    'thresholds': {'critical': 1.0},
    'notify_no_data': False,
    'no_data_timeframe': 20,
}

headers = {
    # 'Content-type': 'application/json',
    'DD-API-KEY': api_key,
    'DD-APPLICATION-KEY': app_key
}

response = requests.post(
    'https://api.datadoghq.com/api/v1/monitor', json=monitor_data, headers=headers)

# Check the response
print("\n Response code: %d \n" % response.status_code)
print("\n" + format(response.text))
