# swagger_client.ContentApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**event_create**](ContentApi.md#event_create) | **POST** /apex/DataServerRW?target&#x3D;SiteAddEventDataServer&amp;action&#x3D;publish | Create an Event
[**event_delete**](ContentApi.md#event_delete) | **POST** /apex/DataServerRW?target&#x3D;AllContentDataServer&amp;action&#x3D;delete&amp;type&#x3D;Event | Delete an Event
[**event_get**](ContentApi.md#event_get) | **GET** /apex/DataServerRW?target&#x3D;SiteAddEventDataServer&amp;action&#x3D;get | Get an Event
[**event_update**](ContentApi.md#event_update) | **POST** /apex/DataServerRW?target&#x3D;SiteAddEventDataServer&amp;action&#x3D;update | Update an Event
[**list_latest_content_for_a_site_by_site_id**](ContentApi.md#list_latest_content_for_a_site_by_site_id) | **POST** /apex/DataServerRW?target&#x3D;AllContentDataServer&amp;action&#x3D;search&amp;filter&#x3D;latest | List Latest Content for a site by Site ID
[**list_latest_contentfromsites_ifollow**](ContentApi.md#list_latest_contentfromsites_ifollow) | **POST** /apex/DataServerRW?target&#x3D;AllContentDataServer&amp;action&#x3D;search | List Latest Content from sites I follow
[**list_popular_content_for_a_site_by_site_id**](ContentApi.md#list_popular_content_for_a_site_by_site_id) | **POST** /apex/DataServerRW?target&#x3D;AllContentDataServer&amp;action&#x3D;search&amp;filter&#x3D;popular | List Popular Content for a site by Site ID
[**page_create**](ContentApi.md#page_create) | **POST** /apex/DataServerRW?target&#x3D;SiteAddPageDataServer&amp;action&#x3D;publish | Create a Page
[**page_delete**](ContentApi.md#page_delete) | **POST** /apex/DataServerRW?target&#x3D;AllContentDataServer&amp;action&#x3D;delete | Delete a Page
[**page_get**](ContentApi.md#page_get) | **GET** /apex/DataServerRW?target&#x3D;SiteAddPageDataServer&amp;action&#x3D;get | Get a Page
[**page_update**](ContentApi.md#page_update) | **POST** /apex/DataServerRW?target&#x3D;SiteAddPageDataServer&amp;action&#x3D;update | Edit a Page
[**search_content_from_sites_i_follow**](ContentApi.md#search_content_from_sites_i_follow) | **POST** /apex/DataServerRW?target&#x3D;AllContentDataServer&amp;action&#x3D;search&amp; | List popular Content from sites I follow

# **event_create**
> event_create(data, site_id)

Create an Event

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ContentApi()
data = swagger_client.Event() # Event | 
site_id = 'site_id_example' # str | Site Id in which the event needs to be created

try:
    # Create an Event
    api_instance.event_create(data, site_id)
except ApiException as e:
    print("Exception when calling ContentApi->event_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**Event**](.md)|  | 
 **site_id** | **str**| Site Id in which the event needs to be created | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **event_delete**
> event_delete(data, site_id)

Delete an Event

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ContentApi()
data = swagger_client.Delete() # Delete | 
site_id = 'site_id_example' # str | Site Id in which the event needs to be deleted

try:
    # Delete an Event
    api_instance.event_delete(data, site_id)
except ApiException as e:
    print("Exception when calling ContentApi->event_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**Delete**](.md)|  | 
 **site_id** | **str**| Site Id in which the event needs to be deleted | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **event_get**
> event_get(content_id)

Get an Event

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ContentApi()
content_id = 'content_id_example' # str | Id of event

try:
    # Get an Event
    api_instance.event_get(content_id)
except ApiException as e:
    print("Exception when calling ContentApi->event_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_id** | **str**| Id of event | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **event_update**
> event_update(data, content_id, site_id)

Update an Event

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ContentApi()
data = swagger_client.EventUpdate() # EventUpdate | 
content_id = 'content_id_example' # str | Id of event that needs to be updated
site_id = 'site_id_example' # str | Site Id in which the event needs to be updated

try:
    # Update an Event
    api_instance.event_update(data, content_id, site_id)
except ApiException as e:
    print("Exception when calling ContentApi->event_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**EventUpdate**](.md)|  | 
 **content_id** | **str**| Id of event that needs to be updated | 
 **site_id** | **str**| Site Id in which the event needs to be updated | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_latest_content_for_a_site_by_site_id**
> list_latest_content_for_a_site_by_site_id(data, site_id)

List Latest Content for a site by Site ID

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ContentApi()
data = swagger_client.LatestContent() # LatestContent | 
site_id = 'site_id_example' # str | Site Id in which the Latest Content needs to be Listed

try:
    # List Latest Content for a site by Site ID
    api_instance.list_latest_content_for_a_site_by_site_id(data, site_id)
except ApiException as e:
    print("Exception when calling ContentApi->list_latest_content_for_a_site_by_site_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**LatestContent**](.md)|  | 
 **site_id** | **str**| Site Id in which the Latest Content needs to be Listed | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_latest_contentfromsites_ifollow**
> list_latest_contentfromsites_ifollow(data)

List Latest Content from sites I follow

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ContentApi()
data = swagger_client.LatestContentFollowed() # LatestContentFollowed | 

try:
    # List Latest Content from sites I follow
    api_instance.list_latest_contentfromsites_ifollow(data)
except ApiException as e:
    print("Exception when calling ContentApi->list_latest_contentfromsites_ifollow: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**LatestContentFollowed**](.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_popular_content_for_a_site_by_site_id**
> list_popular_content_for_a_site_by_site_id(data, site_id)

List Popular Content for a site by Site ID

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ContentApi()
data = swagger_client.PopularContent() # PopularContent | 
site_id = 'site_id_example' # str | Site Id in which the Popular Content needs to be Listed

try:
    # List Popular Content for a site by Site ID
    api_instance.list_popular_content_for_a_site_by_site_id(data, site_id)
except ApiException as e:
    print("Exception when calling ContentApi->list_popular_content_for_a_site_by_site_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**PopularContent**](.md)|  | 
 **site_id** | **str**| Site Id in which the Popular Content needs to be Listed | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **page_create**
> page_create(data, site_id)

Create a Page

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ContentApi()
data = swagger_client.Page() # Page | 
site_id = 'site_id_example' # str | Site Id in which the page needs to be created

try:
    # Create a Page
    api_instance.page_create(data, site_id)
except ApiException as e:
    print("Exception when calling ContentApi->page_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**Page**](.md)|  | 
 **site_id** | **str**| Site Id in which the page needs to be created | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **page_delete**
> page_delete(data, site_id)

Delete a Page

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ContentApi()
data = swagger_client.Delete() # Delete | 
site_id = 'site_id_example' # str | Site Id in which the page needs to be deleted

try:
    # Delete a Page
    api_instance.page_delete(data, site_id)
except ApiException as e:
    print("Exception when calling ContentApi->page_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**Delete**](.md)|  | 
 **site_id** | **str**| Site Id in which the page needs to be deleted | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **page_get**
> page_get(content_id)

Get a Page

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ContentApi()
content_id = 'content_id_example' # str | Id of the page

try:
    # Get a Page
    api_instance.page_get(content_id)
except ApiException as e:
    print("Exception when calling ContentApi->page_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_id** | **str**| Id of the page | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **page_update**
> page_update(data, content_id, site_id)

Edit a Page

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ContentApi()
data = swagger_client.Page() # Page | 
content_id = 'content_id_example' # str | Id of page that needs to be updated
site_id = 'site_id_example' # str | Site Id in which the page needs to be updated

try:
    # Edit a Page
    api_instance.page_update(data, content_id, site_id)
except ApiException as e:
    print("Exception when calling ContentApi->page_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**Page**](.md)|  | 
 **content_id** | **str**| Id of page that needs to be updated | 
 **site_id** | **str**| Site Id in which the page needs to be updated | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_content_from_sites_i_follow**
> search_content_from_sites_i_follow(data)

List popular Content from sites I follow

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ContentApi()
data = swagger_client.PopularContentFollowed() # PopularContentFollowed | 

try:
    # List popular Content from sites I follow
    api_instance.search_content_from_sites_i_follow(data)
except ApiException as e:
    print("Exception when calling ContentApi->search_content_from_sites_i_follow: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**PopularContentFollowed**](.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

