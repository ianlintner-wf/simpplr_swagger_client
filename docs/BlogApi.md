# swagger_client.BlogApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**blog_create**](BlogApi.md#blog_create) | **POST** /apex/DataServerRW?target&#x3D;ProfileAddBlogPostDataServer&amp;action&#x3D;publish | Create a Blog
[**blog_delete**](BlogApi.md#blog_delete) | **POST** /apex/DataServerRW?target&#x3D;AllContentDataServer&amp;action&#x3D;delete&amp;type&#x3D;Blog | Delete a Blog
[**blog_get**](BlogApi.md#blog_get) | **GET** /apex/DataServerRW?target&#x3D;ProfileAddBlogPostDataServer&amp;action&#x3D;get | Get a Blog
[**blog_update**](BlogApi.md#blog_update) | **POST** /apex/DataServerRW?target&#x3D;ProfileAddBlogPostDataServer&amp;action&#x3D;update | Update a Blog

# **blog_create**
> blog_create(data, site_id=site_id)

Create a Blog

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BlogApi()
data = swagger_client.Blog() # Blog | 
site_id = 'site_id_example' # str | Site Id in which the blog need to be created (optional)

try:
    # Create a Blog
    api_instance.blog_create(data, site_id=site_id)
except ApiException as e:
    print("Exception when calling BlogApi->blog_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**Blog**](.md)|  | 
 **site_id** | **str**| Site Id in which the blog need to be created | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **blog_delete**
> blog_delete(data, site_id=site_id)

Delete a Blog

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BlogApi()
data = swagger_client.Delete() # Delete | 
site_id = 'site_id_example' # str | Site Id in which the blog need to be deleted (optional)

try:
    # Delete a Blog
    api_instance.blog_delete(data, site_id=site_id)
except ApiException as e:
    print("Exception when calling BlogApi->blog_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**Delete**](.md)|  | 
 **site_id** | **str**| Site Id in which the blog need to be deleted | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **blog_get**
> blog_get(content_id=content_id)

Get a Blog

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BlogApi()
content_id = 'content_id_example' # str | Id of blog (optional)

try:
    # Get a Blog
    api_instance.blog_get(content_id=content_id)
except ApiException as e:
    print("Exception when calling BlogApi->blog_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_id** | **str**| Id of blog | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **blog_update**
> blog_update(data, content_id=content_id)

Update a Blog

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BlogApi()
data = swagger_client.Blog() # Blog | 
content_id = 'content_id_example' # str | Id of page that needs to be updated (optional)

try:
    # Update a Blog
    api_instance.blog_update(data, content_id=content_id)
except ApiException as e:
    print("Exception when calling BlogApi->blog_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**Blog**](.md)|  | 
 **content_id** | **str**| Id of page that needs to be updated | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

