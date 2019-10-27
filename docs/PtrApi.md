# selectel_dns_api.PtrApi

All URIs are relative to *https://api.selectel.ru/domains/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_ptr_record**](PtrApi.md#add_ptr_record) | **POST** /ptr | Create new PTR record
[**delete_ptr_record**](PtrApi.md#delete_ptr_record) | **DELETE** /ptr/{ptr_id} | Deletes a PTR record
[**get_ptr_record_by_id**](PtrApi.md#get_ptr_record_by_id) | **GET** /ptr/{ptr_id} | Find information about PTR record by ID
[**get_ptr_records**](PtrApi.md#get_ptr_records) | **GET** /ptr | Getting PTR records
[**update_ptr_record**](PtrApi.md#update_ptr_record) | **PUT** /ptr/{ptr_id} | Updates a PTR record


# **add_ptr_record**
> PTRRecord add_ptr_record(body)

Create new PTR record



### Example 
```python
from __future__ import print_function
import time
import selectel_dns_api
from selectel_dns_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: X-Token
selectel_dns_api.configuration.api_key['X-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# selectel_dns_api.configuration.api_key_prefix['X-Token'] = 'Bearer'

# create an instance of the API class
api_instance = selectel_dns_api.PtrApi()
body = selectel_dns_api.NewOrUpdatedPTRRecord() # NewOrUpdatedPTRRecord | PTR record info for creation

try: 
    # Create new PTR record
    api_response = api_instance.add_ptr_record(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PtrApi->add_ptr_record: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NewOrUpdatedPTRRecord**](NewOrUpdatedPTRRecord.md)| PTR record info for creation | 

### Return type

[**PTRRecord**](PTRRecord.md)

### Authorization

[X-Token](../README.md#X-Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_ptr_record**
> delete_ptr_record(ptr_id)

Deletes a PTR record



### Example 
```python
from __future__ import print_function
import time
import selectel_dns_api
from selectel_dns_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: X-Token
selectel_dns_api.configuration.api_key['X-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# selectel_dns_api.configuration.api_key_prefix['X-Token'] = 'Bearer'

# create an instance of the API class
api_instance = selectel_dns_api.PtrApi()
ptr_id = 789 # int | ID of PTR record

try: 
    # Deletes a PTR record
    api_instance.delete_ptr_record(ptr_id)
except ApiException as e:
    print("Exception when calling PtrApi->delete_ptr_record: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ptr_id** | **int**| ID of PTR record | 

### Return type

void (empty response body)

### Authorization

[X-Token](../README.md#X-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ptr_record_by_id**
> PTRRecord get_ptr_record_by_id(ptr_id)

Find information about PTR record by ID

Returns a single PTR record

### Example 
```python
from __future__ import print_function
import time
import selectel_dns_api
from selectel_dns_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: X-Token
selectel_dns_api.configuration.api_key['X-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# selectel_dns_api.configuration.api_key_prefix['X-Token'] = 'Bearer'

# create an instance of the API class
api_instance = selectel_dns_api.PtrApi()
ptr_id = 789 # int | ID of PTR record

try: 
    # Find information about PTR record by ID
    api_response = api_instance.get_ptr_record_by_id(ptr_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PtrApi->get_ptr_record_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ptr_id** | **int**| ID of PTR record | 

### Return type

[**PTRRecord**](PTRRecord.md)

### Authorization

[X-Token](../README.md#X-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ptr_records**
> list[PTRRecord] get_ptr_records()

Getting PTR records



### Example 
```python
from __future__ import print_function
import time
import selectel_dns_api
from selectel_dns_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: X-Token
selectel_dns_api.configuration.api_key['X-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# selectel_dns_api.configuration.api_key_prefix['X-Token'] = 'Bearer'

# create an instance of the API class
api_instance = selectel_dns_api.PtrApi()

try: 
    # Getting PTR records
    api_response = api_instance.get_ptr_records()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PtrApi->get_ptr_records: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[PTRRecord]**](PTRRecord.md)

### Authorization

[X-Token](../README.md#X-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_ptr_record**
> PTRRecord update_ptr_record(ptr_id, body)

Updates a PTR record



### Example 
```python
from __future__ import print_function
import time
import selectel_dns_api
from selectel_dns_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: X-Token
selectel_dns_api.configuration.api_key['X-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# selectel_dns_api.configuration.api_key_prefix['X-Token'] = 'Bearer'

# create an instance of the API class
api_instance = selectel_dns_api.PtrApi()
ptr_id = 789 # int | ID of PTR record
body = selectel_dns_api.NewOrUpdatedPTRRecord() # NewOrUpdatedPTRRecord | PTR record info for update

try: 
    # Updates a PTR record
    api_response = api_instance.update_ptr_record(ptr_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PtrApi->update_ptr_record: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ptr_id** | **int**| ID of PTR record | 
 **body** | [**NewOrUpdatedPTRRecord**](NewOrUpdatedPTRRecord.md)| PTR record info for update | 

### Return type

[**PTRRecord**](PTRRecord.md)

### Authorization

[X-Token](../README.md#X-Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

