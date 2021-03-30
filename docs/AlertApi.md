# swagger_client.AlertApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**alert_create**](AlertApi.md#alert_create) | **POST** /apex/DataServerRW?target&#x3D;AlertDataServer&amp;action&#x3D;create | Create an Alert For Everyone
[**alert_create_for_site_members**](AlertApi.md#alert_create_for_site_members) | **POST** /apex/DataServerRW?target&#x3D;AlertDataServer&amp;action&#x3D;create&amp; | Create new alert for site members/ followers by site id
[**delete_alert_by_id**](AlertApi.md#delete_alert_by_id) | **POST** /apex/DataServerRW?target&#x3D;AlertDataServer&amp;action&#x3D;delete | Delete alert by ID
[**edit_alert_by_id**](AlertApi.md#edit_alert_by_id) | **POST** /apex/DataServerRW?target&#x3D;AlertDataServer&amp;action&#x3D;update | Edit Alert By ID
[**expire_alert_by_id**](AlertApi.md#expire_alert_by_id) | **POST** /apex/DataServerRW?target&#x3D;AlertDataServer&amp;action&#x3D;expireNow | Expire alert by ID
[**list_alerts**](AlertApi.md#list_alerts) | **POST** /apex/DataServerRW?target&#x3D;AlertDataServer&amp;action&#x3D;searchAlert | List Alerts

# **alert_create**
> alert_create(data)

Create an Alert For Everyone

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AlertApi()
data = swagger_client.Alert() # Alert | 

try:
    # Create an Alert For Everyone
    api_instance.alert_create(data)
except ApiException as e:
    print("Exception when calling AlertApi->alert_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**Alert**](.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **alert_create_for_site_members**
> alert_create_for_site_members(data)

Create new alert for site members/ followers by site id

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AlertApi()
data = swagger_client.AlertForSiteMembers() # AlertForSiteMembers | 

try:
    # Create new alert for site members/ followers by site id
    api_instance.alert_create_for_site_members(data)
except ApiException as e:
    print("Exception when calling AlertApi->alert_create_for_site_members: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**AlertForSiteMembers**](.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_alert_by_id**
> delete_alert_by_id(data)

Delete alert by ID

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AlertApi()
data = swagger_client.DeleteAlert() # DeleteAlert | 

try:
    # Delete alert by ID
    api_instance.delete_alert_by_id(data)
except ApiException as e:
    print("Exception when calling AlertApi->delete_alert_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**DeleteAlert**](.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_alert_by_id**
> edit_alert_by_id(data)

Edit Alert By ID

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AlertApi()
data = swagger_client.UpdateAlert() # UpdateAlert | 

try:
    # Edit Alert By ID
    api_instance.edit_alert_by_id(data)
except ApiException as e:
    print("Exception when calling AlertApi->edit_alert_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**UpdateAlert**](.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **expire_alert_by_id**
> expire_alert_by_id(data)

Expire alert by ID

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AlertApi()
data = swagger_client.DeleteAlert() # DeleteAlert | 

try:
    # Expire alert by ID
    api_instance.expire_alert_by_id(data)
except ApiException as e:
    print("Exception when calling AlertApi->expire_alert_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**DeleteAlert**](.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_alerts**
> list_alerts(data)

List Alerts

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AlertApi()
data = swagger_client.ListAlert() # ListAlert | 

try:
    # List Alerts
    api_instance.list_alerts(data)
except ApiException as e:
    print("Exception when calling AlertApi->list_alerts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**ListAlert**](.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

