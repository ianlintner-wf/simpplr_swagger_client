# swagger_client.PeopleApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_profile_by_people_id**](PeopleApi.md#get_profile_by_people_id) | **POST** /apex/DataServerRW?target&#x3D;peopledataserver&amp;action&#x3D;getUser | Get profile by People Id
[**get_profile_by_user_id**](PeopleApi.md#get_profile_by_user_id) | **POST** /apex/DataServerRW?target&#x3D;peopledataserver&amp;action&#x3D;getUser&amp; | Get profile by User Id
[**list_people**](PeopleApi.md#list_people) | **POST** /apex/DataServerRW?target&#x3D;peopledataserver&amp;action&#x3D;search&amp; | List People
[**list_people_by_expertise**](PeopleApi.md#list_people_by_expertise) | **POST** /apex/DataServerRW?target&#x3D;peopledataserver&amp;action&#x3D;search&amp;Expertise | List people by Expertise
[**list_people_in_my_department**](PeopleApi.md#list_people_in_my_department) | **POST** /apex/DataServerRW?target&#x3D;peopledataserver&amp;action&#x3D;search&amp;Department | List people in my department
[**list_people_in_my_location**](PeopleApi.md#list_people_in_my_location) | **POST** /apex/DataServerRW?target&#x3D;peopledataserver&amp;action&#x3D;search&amp;Location | List people in my location
[**people_update**](PeopleApi.md#people_update) | **POST** /apex/DataServerRW?target&#x3D;MySettingDataServer&amp;action&#x3D;saveProfileSettings | Edit profile by people Id
[**search**](PeopleApi.md#search) | **POST** /apex/DataServerRW?target&#x3D;peopledataserver&amp;action&#x3D;search | Search

# **get_profile_by_people_id**
> get_profile_by_people_id(data)

Get profile by People Id

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PeopleApi()
data = swagger_client.PeopleId() # PeopleId | 

try:
    # Get profile by People Id
    api_instance.get_profile_by_people_id(data)
except ApiException as e:
    print("Exception when calling PeopleApi->get_profile_by_people_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**PeopleId**](.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_profile_by_user_id**
> get_profile_by_user_id(data)

Get profile by User Id

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PeopleApi()
data = swagger_client.UserId() # UserId | 

try:
    # Get profile by User Id
    api_instance.get_profile_by_user_id(data)
except ApiException as e:
    print("Exception when calling PeopleApi->get_profile_by_user_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**UserId**](.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_people**
> list_people(data)

List People

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PeopleApi()
data = swagger_client.ListPeople() # ListPeople | 

try:
    # List People
    api_instance.list_people(data)
except ApiException as e:
    print("Exception when calling PeopleApi->list_people: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**ListPeople**](.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_people_by_expertise**
> list_people_by_expertise(data)

List people by Expertise

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PeopleApi()
data = swagger_client.ListPeopleByExpertise() # ListPeopleByExpertise | 

try:
    # List people by Expertise
    api_instance.list_people_by_expertise(data)
except ApiException as e:
    print("Exception when calling PeopleApi->list_people_by_expertise: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**ListPeopleByExpertise**](.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_people_in_my_department**
> list_people_in_my_department(data)

List people in my department

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PeopleApi()
data = swagger_client.ListPeopleByDepartment() # ListPeopleByDepartment | 

try:
    # List people in my department
    api_instance.list_people_in_my_department(data)
except ApiException as e:
    print("Exception when calling PeopleApi->list_people_in_my_department: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**ListPeopleByDepartment**](.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_people_in_my_location**
> list_people_in_my_location(data)

List people in my location

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PeopleApi()
data = swagger_client.ListPeopleByLocation() # ListPeopleByLocation | 

try:
    # List people in my location
    api_instance.list_people_in_my_location(data)
except ApiException as e:
    print("Exception when calling PeopleApi->list_people_in_my_location: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**ListPeopleByLocation**](.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **people_update**
> people_update(data)

Edit profile by people Id

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PeopleApi()
data = swagger_client.PeopleUpdate() # PeopleUpdate | 

try:
    # Edit profile by people Id
    api_instance.people_update(data)
except ApiException as e:
    print("Exception when calling PeopleApi->people_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**PeopleUpdate**](.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search**
> search(data)

Search

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PeopleApi()
data = swagger_client.People() # People | 

try:
    # Search
    api_instance.search(data)
except ApiException as e:
    print("Exception when calling PeopleApi->search: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**People**](.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

