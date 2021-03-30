# swagger_client.DigitalDisplayApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**site_carousel**](DigitalDisplayApi.md#site_carousel) | **POST** /apex/DataServerRW?target&#x3D;CarouselDataServer&amp;action&#x3D;get&amp;Carousel&#x3D;Site | SiteCarousel
[**site_home_carousel**](DigitalDisplayApi.md#site_home_carousel) | **POST** /apex/DataServerRW?target&#x3D;CarouselDataServer&amp;action&#x3D;get&amp;Carousel&#x3D;Home | Home Carousel

# **site_carousel**
> site_carousel(data)

SiteCarousel

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DigitalDisplayApi()
data = swagger_client.SiteCarousel() # SiteCarousel | 

try:
    # SiteCarousel
    api_instance.site_carousel(data)
except ApiException as e:
    print("Exception when calling DigitalDisplayApi->site_carousel: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**SiteCarousel**](.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **site_home_carousel**
> site_home_carousel(data)

Home Carousel

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DigitalDisplayApi()
data = swagger_client.HomeCarousel() # HomeCarousel | 

try:
    # Home Carousel
    api_instance.site_home_carousel(data)
except ApiException as e:
    print("Exception when calling DigitalDisplayApi->site_home_carousel: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**HomeCarousel**](.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

