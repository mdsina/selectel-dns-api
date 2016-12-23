# selectel_dns_api.DomainsApi

All URIs are relative to *https://api.selectel.ru/domains/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_domain**](DomainsApi.md#add_domain) | **POST** / | Create new domain
[**delete_domain**](DomainsApi.md#delete_domain) | **DELETE** /{domain_id} | Deletes a domain
[**get_domain_by_id**](DomainsApi.md#get_domain_by_id) | **GET** /{domain_id} | Find domain by ID
[**get_domain_by_name**](DomainsApi.md#get_domain_by_name) | **GET** /{domain_name} | Find domain by name
[**get_domain_zone_file**](DomainsApi.md#get_domain_zone_file) | **GET** /{domain_id}/export | Find domain by name
[**get_domains**](DomainsApi.md#get_domains) | **GET** / | Getting domains info
[**update_domain**](DomainsApi.md#update_domain) | **PATCH** /{domain_id} | Updates a domain


# **add_domain**
> Domain add_domain(body)

Create new domain



### Example 
```python
from __future__ import print_statement
import time
import selectel_dns_api
from selectel_dns_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = selectel_dns_api.DomainsApi()
body = selectel_dns_api.NewDomain() # NewDomain | Domain info for creation

try: 
    # Create new domain
    api_response = api_instance.add_domain(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DomainsApi->add_domain: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NewDomain**](NewDomain.md)| Domain info for creation | 

### Return type

[**Domain**](Domain.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_domain**
> delete_domain(domain_id)

Deletes a domain



### Example 
```python
from __future__ import print_statement
import time
import selectel_dns_api
from selectel_dns_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = selectel_dns_api.DomainsApi()
domain_id = 789 # int | ID of domain to delete

try: 
    # Deletes a domain
    api_instance.delete_domain(domain_id)
except ApiException as e:
    print("Exception when calling DomainsApi->delete_domain: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_id** | **int**| ID of domain to delete | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_domain_by_id**
> Domain get_domain_by_id(domain_id)

Find domain by ID

Returns a single domain

### Example 
```python
from __future__ import print_statement
import time
import selectel_dns_api
from selectel_dns_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = selectel_dns_api.DomainsApi()
domain_id = 789 # int | ID of domain to return

try: 
    # Find domain by ID
    api_response = api_instance.get_domain_by_id(domain_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DomainsApi->get_domain_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_id** | **int**| ID of domain to return | 

### Return type

[**Domain**](Domain.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_domain_by_name**
> Domain get_domain_by_name(domain_name)

Find domain by name

Returns a single domain

### Example 
```python
from __future__ import print_statement
import time
import selectel_dns_api
from selectel_dns_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = selectel_dns_api.DomainsApi()
domain_name = 'domain_name_example' # str | name of domain to return

try: 
    # Find domain by name
    api_response = api_instance.get_domain_by_name(domain_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DomainsApi->get_domain_by_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_name** | **str**| name of domain to return | 

### Return type

[**Domain**](Domain.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_domain_zone_file**
> str get_domain_zone_file(domain_id)

Find domain by name

Returns a domain's zone file

### Example 
```python
from __future__ import print_statement
import time
import selectel_dns_api
from selectel_dns_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = selectel_dns_api.DomainsApi()
domain_id = 789 # int | ID of domain to delete

try: 
    # Find domain by name
    api_response = api_instance.get_domain_zone_file(domain_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DomainsApi->get_domain_zone_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_id** | **int**| ID of domain to delete | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_domains**
> list[Domain] get_domains()

Getting domains info



### Example 
```python
from __future__ import print_statement
import time
import selectel_dns_api
from selectel_dns_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = selectel_dns_api.DomainsApi()

try: 
    # Getting domains info
    api_response = api_instance.get_domains()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DomainsApi->get_domains: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Domain]**](Domain.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_domain**
> Domain update_domain(domain_id, body)

Updates a domain



### Example 
```python
from __future__ import print_statement
import time
import selectel_dns_api
from selectel_dns_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = selectel_dns_api.DomainsApi()
domain_id = 789 # int | ID of domain to update
body = selectel_dns_api.UpdatedDomain() # UpdatedDomain | Domain info for update

try: 
    # Updates a domain
    api_response = api_instance.update_domain(domain_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DomainsApi->update_domain: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_id** | **int**| ID of domain to update | 
 **body** | [**UpdatedDomain**](UpdatedDomain.md)| Domain info for update | 

### Return type

[**Domain**](Domain.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

