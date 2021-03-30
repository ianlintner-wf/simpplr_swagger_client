# swagger_client.NotificationApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**noti_create**](NotificationApi.md#noti_create) | **POST** /apex/DataServerRW?target&#x3D;NotificationDataServer&amp;action&#x3D;create | Create a notification
[**noti_list**](NotificationApi.md#noti_list) | **POST** /apex/DataServerRW?target&#x3D;NotificationDataServer&amp;action&#x3D;search | Notification List
[**noti_update**](NotificationApi.md#noti_update) | **POST** /apex/DataServerRW?target&#x3D;NotificationDataServer&amp;action&#x3D;markAsActioned | Mark actionable notification as actioned

# **noti_create**
> noti_create(data)

Create a notification

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NotificationApi()
data = swagger_client.Notification() # Notification | 

try:
    # Create a notification
    api_instance.noti_create(data)
except ApiException as e:
    print("Exception when calling NotificationApi->noti_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**Notification**](.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **noti_list**
> noti_list(data)

Notification List

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NotificationApi()
data = swagger_client.NotificationList() # NotificationList | 

try:
    # Notification List
    api_instance.noti_list(data)
except ApiException as e:
    print("Exception when calling NotificationApi->noti_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**NotificationList**](.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **noti_update**
> noti_update(data, notification_id)

Mark actionable notification as actioned

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NotificationApi()
data = swagger_client.NotificationActioned() # NotificationActioned | 
notification_id = 'notification_id_example' # str | Id of notification that needs to be updated

try:
    # Mark actionable notification as actioned
    api_instance.noti_update(data, notification_id)
except ApiException as e:
    print("Exception when calling NotificationApi->noti_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**NotificationActioned**](.md)|  | 
 **notification_id** | **str**| Id of notification that needs to be updated | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

