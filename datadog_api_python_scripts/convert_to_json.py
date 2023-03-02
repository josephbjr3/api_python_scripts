import json


monitor_data = {
    'query': 'avg(last_1h):avg:system.load.1{host:MacBook-Pro.local} by {host} > 7',
    'name': 'High avg CPU load',
    'message': 'This alert is triggered when the avg cpu load over the past hour is greater than 7.',
    'type': 'query alert',
    'priority': 4,
    'thresholds': {'critical': 1.0},
    'notify_no_data': False,
    'no_data_timeframe': 20,
}

print(json.dumps(monitor_data))
