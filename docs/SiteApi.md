# swagger_client.SiteApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apex_data_server_r_wtarget_site_data_serveractiongetsite_detail_data_get**](SiteApi.md#apex_data_server_r_wtarget_site_data_serveractiongetsite_detail_data_get) | **GET** /apex/DataServerRW?target&#x3D;SiteDataServer&amp;action&#x3D;getsiteDetailData | Get a Site
[**site_activate_deactivate**](SiteApi.md#site_activate_deactivate) | **POST** /apex/DataServerRW?target&#x3D;SiteDataServer&amp;action&#x3D;setActivated | Activate and Deactivate a Site
[**site_add_follower**](SiteApi.md#site_add_follower) | **POST** /apex/DataServerRW?target&#x3D;ManageSiteDataServer&amp;action&#x3D;addPeople&amp; membershipType&#x3D;follower&amp;addFollower | Add Follower to Site
[**site_add_member**](SiteApi.md#site_add_member) | **POST** /apex/DataServerRW?target&#x3D;ManageSiteDataServer&amp;action&#x3D;addPeople&amp; membershipType&#x3D;member&amp;addMember | Add Member to Site
[**site_category**](SiteApi.md#site_category) | **POST** /apex/DataServerRW?target&#x3D;SiteDataServer&amp;action&#x3D;search&amp;filter&#x3D;SiteCategory | Search Site Category
[**site_category_by_id**](SiteApi.md#site_category_by_id) | **POST** /apex/DataServerRW?target&#x3D;SiteDataServer&amp;action&#x3D;search&amp;category&#x3D;CategoryById | Search Site CategoryById
[**site_create**](SiteApi.md#site_create) | **POST** /apex/DataServerRW?target&#x3D;SiteDataServer&amp;action&#x3D;search | Search Site
[**site_create_0**](SiteApi.md#site_create_0) | **POST** /apex/DataServerRW?target&#x3D;SiteDataServer&amp;action&#x3D;createSite | Create a Site
[**site_edit**](SiteApi.md#site_edit) | **POST** /apex/DataServerRW?target&#x3D;ManageSiteDataServer&amp;action&#x3D;saveSiteDetail&amp;edit&#x3D;SiteDetails | Edit Site Details
[**site_featured**](SiteApi.md#site_featured) | **POST** /apex/DataServerRW?target&#x3D;SiteDataServer&amp;action&#x3D;search&amp;filter&#x3D;SiteFeatured | Search Site Featured
[**site_following**](SiteApi.md#site_following) | **POST** /apex/DataServerRW?target&#x3D;SiteDataServer&amp;action&#x3D;search&amp;filter&#x3D;following | Search Following Site
[**site_latest**](SiteApi.md#site_latest) | **POST** /apex/DataServerRW?target&#x3D;SiteDataServer&amp;action&#x3D;search&amp;filter&#x3D;SiteLatest | Search Site Latest
[**site_member**](SiteApi.md#site_member) | **POST** /apex/DataServerRW?target&#x3D;SiteDataServer&amp;action&#x3D;search&amp;filter&#x3D;SiteMember | Search Site Member
[**site_mysite**](SiteApi.md#site_mysite) | **POST** /apex/DataServerRW?target&#x3D;SiteDataServer&amp;action&#x3D;search&amp;Mysite | Search Mysite
[**site_popular**](SiteApi.md#site_popular) | **POST** /apex/DataServerRW?target&#x3D;SiteDataServer&amp;action&#x3D;search&amp;filter&#x3D;SitePopular | Search Site Popular
[**site_remove_follower**](SiteApi.md#site_remove_follower) | **POST** /apex/DataServerRW?target&#x3D;ManageSiteDataServer&amp;action&#x3D;removePeople&amp; membershipType&#x3D;follower&amp;removeFollower | Remove Follower to Site
[**site_remove_member**](SiteApi.md#site_remove_member) | **POST** /apex/DataServerRW?target&#x3D;ManageSiteDataServer&amp;action&#x3D;removePeople&amp; membershipType&#x3D;member&amp;removeMember | Remove Member to Site

# **apex_data_server_r_wtarget_site_data_serveractiongetsite_detail_data_get**
> apex_data_server_r_wtarget_site_data_serveractiongetsite_detail_data_get(site_id)

Get a Site

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SiteApi()
site_id = 'site_id_example' # str | Site Id

try:
    # Get a Site
    api_instance.apex_data_server_r_wtarget_site_data_serveractiongetsite_detail_data_get(site_id)
except ApiException as e:
    print("Exception when calling SiteApi->apex_data_server_r_wtarget_site_data_serveractiongetsite_detail_data_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **str**| Site Id | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **site_activate_deactivate**
> site_activate_deactivate(data)

Activate and Deactivate a Site

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SiteApi()
data = swagger_client.Activate() # Activate | 

try:
    # Activate and Deactivate a Site
    api_instance.site_activate_deactivate(data)
except ApiException as e:
    print("Exception when calling SiteApi->site_activate_deactivate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**Activate**](.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **site_add_follower**
> site_add_follower(data, site_id)

Add Follower to Site

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SiteApi()
data = swagger_client.AddSiteFollower() # AddSiteFollower | 
site_id = 'site_id_example' # str | Site Id in which the follower needs to be added

try:
    # Add Follower to Site
    api_instance.site_add_follower(data, site_id)
except ApiException as e:
    print("Exception when calling SiteApi->site_add_follower: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**AddSiteFollower**](.md)|  | 
 **site_id** | **str**| Site Id in which the follower needs to be added | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **site_add_member**
> site_add_member(data, site_id)

Add Member to Site

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SiteApi()
data = swagger_client.AddSiteMember() # AddSiteMember | 
site_id = 'site_id_example' # str | Site Id in which the member needs to be added

try:
    # Add Member to Site
    api_instance.site_add_member(data, site_id)
except ApiException as e:
    print("Exception when calling SiteApi->site_add_member: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**AddSiteMember**](.md)|  | 
 **site_id** | **str**| Site Id in which the member needs to be added | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **site_category**
> site_category(data)

Search Site Category

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SiteApi()
data = swagger_client.SiteCategory() # SiteCategory | 

try:
    # Search Site Category
    api_instance.site_category(data)
except ApiException as e:
    print("Exception when calling SiteApi->site_category: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**SiteCategory**](.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **site_category_by_id**
> site_category_by_id(data)

Search Site CategoryById

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SiteApi()
data = swagger_client.SiteCategoryById() # SiteCategoryById | 

try:
    # Search Site CategoryById
    api_instance.site_category_by_id(data)
except ApiException as e:
    print("Exception when calling SiteApi->site_category_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**SiteCategoryById**](.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **site_create**
> site_create(data)

Search Site

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SiteApi()
data = swagger_client.SiteSearch() # SiteSearch | 

try:
    # Search Site
    api_instance.site_create(data)
except ApiException as e:
    print("Exception when calling SiteApi->site_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**SiteSearch**](.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **site_create_0**
> site_create_0(data)

Create a Site

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SiteApi()
data = swagger_client.SiteCreate() # SiteCreate | 

try:
    # Create a Site
    api_instance.site_create_0(data)
except ApiException as e:
    print("Exception when calling SiteApi->site_create_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**SiteCreate**](.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **site_edit**
> site_edit(data, site_id)

Edit Site Details

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SiteApi()
data = swagger_client.SiteEdit() # SiteEdit | 
site_id = 'site_id_example' # str | Site Id in which the member needs to edit site details

try:
    # Edit Site Details
    api_instance.site_edit(data, site_id)
except ApiException as e:
    print("Exception when calling SiteApi->site_edit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**SiteEdit**](.md)|  | 
 **site_id** | **str**| Site Id in which the member needs to edit site details | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **site_featured**
> site_featured(data)

Search Site Featured

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SiteApi()
data = swagger_client.SiteFeatured() # SiteFeatured | 

try:
    # Search Site Featured
    api_instance.site_featured(data)
except ApiException as e:
    print("Exception when calling SiteApi->site_featured: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**SiteFeatured**](.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **site_following**
> site_following(data)

Search Following Site

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SiteApi()
data = swagger_client.SiteFollow() # SiteFollow | 

try:
    # Search Following Site
    api_instance.site_following(data)
except ApiException as e:
    print("Exception when calling SiteApi->site_following: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**SiteFollow**](.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **site_latest**
> site_latest(data)

Search Site Latest

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SiteApi()
data = swagger_client.SiteLatest() # SiteLatest | 

try:
    # Search Site Latest
    api_instance.site_latest(data)
except ApiException as e:
    print("Exception when calling SiteApi->site_latest: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**SiteLatest**](.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **site_member**
> site_member(data)

Search Site Member

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SiteApi()
data = swagger_client.SiteMember() # SiteMember | 

try:
    # Search Site Member
    api_instance.site_member(data)
except ApiException as e:
    print("Exception when calling SiteApi->site_member: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**SiteMember**](.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **site_mysite**
> site_mysite(data)

Search Mysite

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SiteApi()
data = swagger_client.SiteMysite() # SiteMysite | 

try:
    # Search Mysite
    api_instance.site_mysite(data)
except ApiException as e:
    print("Exception when calling SiteApi->site_mysite: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**SiteMysite**](.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **site_popular**
> site_popular(data)

Search Site Popular

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SiteApi()
data = swagger_client.SitePopular() # SitePopular | 

try:
    # Search Site Popular
    api_instance.site_popular(data)
except ApiException as e:
    print("Exception when calling SiteApi->site_popular: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**SitePopular**](.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **site_remove_follower**
> site_remove_follower(data, site_id)

Remove Follower to Site

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SiteApi()
data = swagger_client.RemoveSiteFollower() # RemoveSiteFollower | 
site_id = 'site_id_example' # str | Site Id in which the follower needs to be remove

try:
    # Remove Follower to Site
    api_instance.site_remove_follower(data, site_id)
except ApiException as e:
    print("Exception when calling SiteApi->site_remove_follower: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**RemoveSiteFollower**](.md)|  | 
 **site_id** | **str**| Site Id in which the follower needs to be remove | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **site_remove_member**
> site_remove_member(data, site_id)

Remove Member to Site

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SiteApi()
data = swagger_client.RemoveSiteMember() # RemoveSiteMember | 
site_id = 'site_id_example' # str | Site Id in which the member needs to be remove

try:
    # Remove Member to Site
    api_instance.site_remove_member(data, site_id)
except ApiException as e:
    print("Exception when calling SiteApi->site_remove_member: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**RemoveSiteMember**](.md)|  | 
 **site_id** | **str**| Site Id in which the member needs to be remove | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

