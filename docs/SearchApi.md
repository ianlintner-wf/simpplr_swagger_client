# swagger_client.SearchApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**content_search**](SearchApi.md#content_search) | **POST** /apex/DataServerRW?target&#x3D;ExternalSearchDataServer&amp;action&#x3D;externalSearch&amp;searchForType&#x3D;Content | Search a Content
[**external_auto_complete**](SearchApi.md#external_auto_complete) | **POST** /apex/DataServerRW?target&#x3D;ExternalSearchDataServer&amp;action&#x3D;externalAutoComplete | Auto Complete Search
[**file_search**](SearchApi.md#file_search) | **POST** /apex/DataServerRW?target&#x3D;ExternalSearchDataServer&amp;action&#x3D;externalSearch&amp;searchForType&#x3D;File | Search a File
[**search_feed_posts**](SearchApi.md#search_feed_posts) | **GET** /apex/DataServerRW?target&#x3D;FeedDataServer&amp;action&#x3D;search | Search feed posts
[**site_search**](SearchApi.md#site_search) | **POST** /apex/DataServerRW?target&#x3D;ExternalSearchDataServer&amp;action&#x3D;externalSearch&amp;searchForType&#x3D;Site | Search a Site
[**top_search**](SearchApi.md#top_search) | **POST** /apex/DataServerRW?target&#x3D;ExternalSearchDataServer&amp;action&#x3D;externalSearch&amp;searchForType&#x3D;Top | Search a Top
[**user_search**](SearchApi.md#user_search) | **POST** /apex/DataServerRW?target&#x3D;ExternalSearchDataServer&amp;action&#x3D;externalSearch&amp;searchForType&#x3D;User | Search a User

# **content_search**
> content_search(data)

Search a Content

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SearchApi()
data = swagger_client.Content() # Content | 

try:
    # Search a Content
    api_instance.content_search(data)
except ApiException as e:
    print("Exception when calling SearchApi->content_search: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**Content**](.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **external_auto_complete**
> external_auto_complete(data)

Auto Complete Search

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SearchApi()
data = swagger_client.AutoCompleteSearch() # AutoCompleteSearch | 

try:
    # Auto Complete Search
    api_instance.external_auto_complete(data)
except ApiException as e:
    print("Exception when calling SearchApi->external_auto_complete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**AutoCompleteSearch**](.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **file_search**
> file_search(data)

Search a File

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SearchApi()
data = '/path/to/file' # File | 

try:
    # Search a File
    api_instance.file_search(data)
except ApiException as e:
    print("Exception when calling SearchApi->file_search: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**File**](.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_feed_posts**
> search_feed_posts(size, subject_id, type, term, sort, next_page_token=next_page_token)

Search feed posts

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SearchApi()
size = 'size_example' # str | 
subject_id = 'subject_id_example' # str | me
type = 'type_example' # str | company
term = 'term_example' # str | which need to be searched
sort = 'sort_example' # str | by date
next_page_token = 'next_page_token_example' # str | _ (optional)

try:
    # Search feed posts
    api_instance.search_feed_posts(size, subject_id, type, term, sort, next_page_token=next_page_token)
except ApiException as e:
    print("Exception when calling SearchApi->search_feed_posts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **size** | **str**|  | 
 **subject_id** | **str**| me | 
 **type** | **str**| company | 
 **term** | **str**| which need to be searched | 
 **sort** | **str**| by date | 
 **next_page_token** | **str**| _ | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **site_search**
> site_search(data)

Search a Site

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SearchApi()
data = swagger_client.Site() # Site | 

try:
    # Search a Site
    api_instance.site_search(data)
except ApiException as e:
    print("Exception when calling SearchApi->site_search: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**Site**](.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **top_search**
> top_search(data)

Search a Top

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SearchApi()
data = swagger_client.Top() # Top | 

try:
    # Search a Top
    api_instance.top_search(data)
except ApiException as e:
    print("Exception when calling SearchApi->top_search: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**Top**](.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_search**
> user_search(data)

Search a User

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SearchApi()
data = swagger_client.User() # User | 

try:
    # Search a User
    api_instance.user_search(data)
except ApiException as e:
    print("Exception when calling SearchApi->user_search: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**User**](.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

