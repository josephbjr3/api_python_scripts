"""
Create a metric monitor returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.monitors_api import MonitorsApi
from datadog_api_client.v1.model.monitor import Monitor
from datadog_api_client.v1.model.monitor_type import MonitorType
from datadog_api_client.v1.model.monitor_options import MonitorOptions
from datadog_api_client.v1.model.monitor_thresholds import MonitorThresholds


import os


body = Monitor(
    name="High avg CPU load",
    query='avg(last_1h):avg:system.load.1{host:MacBook-Pro.local} by {host} > 7',
    type=MonitorType("query alert"),
    message="This alert is triggered when the avg cpu load over the past hour is greater than 7.",
    priority=4,
    options=MonitorOptions(
        thresholds=MonitorThresholds(
            critical=7.0,
        ),
        notify_no_data=False,
        no_data_timeframe=20
    )
)

configuration = Configuration()
configuration.api_key["apiKeyAuth"] = os.environ['DD_API_KEY']
configuration.api_key["appKeyAuth"] = os.environ['DD_APP_KEY']

with ApiClient(configuration) as api_client:
    api_instance = MonitorsApi(api_client)
    response = api_instance.create_monitor(body=body)
    print(response)
