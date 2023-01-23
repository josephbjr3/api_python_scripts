from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.monitors_api import MonitorsApi
from datadog_api_client.v1.model.monitor import Monitor
from datadog_api_client.v1.model.monitor_type import MonitorType


body = Monitor(
    name="High avg CPU load (7)",
    query='avg(last_1h):avg:system.load.1{host:MacBook-Pro.local} by {host} > 7',
    type=MonitorType("query alert"),
    message="test 3",
    priority=4,
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = MonitorsApi(api_client)
    response = api_instance.create_monitor(body=body)
    print(response)
