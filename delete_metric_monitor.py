"""
Delete a monitor returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.monitors_api import MonitorsApi
import os


configuration = Configuration()
configuration.api_key["apiKeyAuth"] = os.environ['DD_API_KEY']
configuration.api_key["appKeyAuth"] = os.environ['DD_APP_KEY']

with ApiClient(configuration) as api_client:
    api_instance = MonitorsApi(api_client)
    response = api_instance.delete_monitor(
        monitor_id=int(108667880),
    )

    print(response)