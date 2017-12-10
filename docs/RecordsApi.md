# selectel_dns_api.RecordsApi

All URIs are relative to *https://api.selectel.ru/domains/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_resource_record**](RecordsApi.md#add_resource_record) | **POST** /{domain_id}/records | Create resource records for domain
[**batch_update_resources_records**](RecordsApi.md#batch_update_resources_records) | **PATCH** /{domain_name}/records/batch_update | Mass update of domain&#39;s resources records
[**delete_resource_record**](RecordsApi.md#delete_resource_record) | **DELETE** /{domain_id}/records/{record_id} | Deletes a resource record
[**get_resource_records_by_domain_id**](RecordsApi.md#get_resource_records_by_domain_id) | **GET** /{domain_id}/records | Getting records info
[**get_resource_records_by_domain_name**](RecordsApi.md#get_resource_records_by_domain_name) | **GET** /{domain_name}/records | Find resource records info for domain by name
[**update_resource_record**](RecordsApi.md#update_resource_record) | **PUT** /{domain_id}/records/{record_id} | Updates a resource record


# **add_resource_record**
> Record add_resource_record(body, domain_id)

Create resource records for domain



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
api_instance = selectel_dns_api.RecordsApi()
body = selectel_dns_api.NewOrUpdatedRecord() # NewOrUpdatedRecord | Resource record info
domain_id = 789 # int | ID of domain

try: 
    # Create resource records for domain
    api_response = api_instance.add_resource_record(body, domain_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecordsApi->add_resource_record: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NewOrUpdatedRecord**](NewOrUpdatedRecord.md)| Resource record info | 
 **domain_id** | **int**| ID of domain | 

### Return type

[**Record**](Record.md)

### Authorization

[X-Token](../README.md#X-Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **batch_update_resources_records**
> batch_update_resources_records(domain_name, body)

Mass update of domain's resources records

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
api_instance = selectel_dns_api.RecordsApi()
domain_name = 'domain_name_example' # str | name of domain
body = selectel_dns_api.BatchUpdateModel() # BatchUpdateModel | Records info for update

try: 
    # Mass update of domain's resources records
    api_instance.batch_update_resources_records(domain_name, body)
except ApiException as e:
    print("Exception when calling RecordsApi->batch_update_resources_records: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_name** | **str**| name of domain | 
 **body** | [**BatchUpdateModel**](BatchUpdateModel.md)| Records info for update | 

### Return type

void (empty response body)

### Authorization

[X-Token](../README.md#X-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_resource_record**
> delete_resource_record(domain_id, record_id)

Deletes a resource record



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
api_instance = selectel_dns_api.RecordsApi()
domain_id = 789 # int | ID of domain
record_id = 789 # int | ID of resource record

try: 
    # Deletes a resource record
    api_instance.delete_resource_record(domain_id, record_id)
except ApiException as e:
    print("Exception when calling RecordsApi->delete_resource_record: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_id** | **int**| ID of domain | 
 **record_id** | **int**| ID of resource record | 

### Return type

void (empty response body)

### Authorization

[X-Token](../README.md#X-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_resource_records_by_domain_id**
> list[Record] get_resource_records_by_domain_id(domain_id)

Getting records info



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
api_instance = selectel_dns_api.RecordsApi()
domain_id = 789 # int | ID of domain

try: 
    # Getting records info
    api_response = api_instance.get_resource_records_by_domain_id(domain_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecordsApi->get_resource_records_by_domain_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_id** | **int**| ID of domain | 

### Return type

[**list[Record]**](Record.md)

### Authorization

[X-Token](../README.md#X-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_resource_records_by_domain_name**
> Record get_resource_records_by_domain_name(domain_name)

Find resource records info for domain by name

Returns a domain's resource records

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
api_instance = selectel_dns_api.RecordsApi()
domain_name = 'domain_name_example' # str | name of domain

try: 
    # Find resource records info for domain by name
    api_response = api_instance.get_resource_records_by_domain_name(domain_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecordsApi->get_resource_records_by_domain_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_name** | **str**| name of domain | 

### Return type

[**Record**](Record.md)

### Authorization

[X-Token](../README.md#X-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_resource_record**
> Record update_resource_record(domain_id, record_id, body)

Updates a resource record



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
api_instance = selectel_dns_api.RecordsApi()
domain_id = 789 # int | ID of domain
record_id = 789 # int | ID of resource record
body = selectel_dns_api.NewOrUpdatedRecord() # NewOrUpdatedRecord | Record info for update

try: 
    # Updates a resource record
    api_response = api_instance.update_resource_record(domain_id, record_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecordsApi->update_resource_record: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_id** | **int**| ID of domain | 
 **record_id** | **int**| ID of resource record | 
 **body** | [**NewOrUpdatedRecord**](NewOrUpdatedRecord.md)| Record info for update | 

### Return type

[**Record**](Record.md)

### Authorization

[X-Token](../README.md#X-Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

