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
configuration.api_key["apiKeyAuth"] = "1363684daf076a499b10c52082d542ae"
configuration.api_key["appKeyAuth"] = "0ca46e3fe140999decb263add084df1b6346909c"

with ApiClient(configuration) as api_client:
    api_instance = MonitorsApi(api_client)
    response = api_instance.create_monitor(body=body)
    print(response)
