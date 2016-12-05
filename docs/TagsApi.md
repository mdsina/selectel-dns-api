# selectel_dns.TagsApi

All URIs are relative to *https://api.selectel.ru/domains/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_new_tag**](TagsApi.md#add_new_tag) | **POST** /tags | Create new tag
[**delete_tag**](TagsApi.md#delete_tag) | **DELETE** /tags/{tag_id} | Deletes a tag
[**get_tag_by_id**](TagsApi.md#get_tag_by_id) | **GET** /tags/{tag_id} | Find information about tag by ID
[**get_tags**](TagsApi.md#get_tags) | **GET** /tags | Getting tags
[**update_tag**](TagsApi.md#update_tag) | **PUT** /tags/{tag_id} | Updates a tag


# **add_new_tag**
> Tag add_new_tag(body)

Create new tag



### Example 
```python
from __future__ import print_statement
import time
import selectel_dns
from selectel_dns.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = selectel_dns.TagsApi()
body = selectel_dns.NewOrUpdatedTag() # NewOrUpdatedTag | Tag info for creation

try: 
    # Create new tag
    api_response = api_instance.add_new_tag(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TagsApi->add_new_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NewOrUpdatedTag**](NewOrUpdatedTag.md)| Tag info for creation | 

### Return type

[**Tag**](Tag.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_tag**
> delete_tag(tag_id)

Deletes a tag



### Example 
```python
from __future__ import print_statement
import time
import selectel_dns
from selectel_dns.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = selectel_dns.TagsApi()
tag_id = 789 # int | ID of tag

try: 
    # Deletes a tag
    api_instance.delete_tag(tag_id)
except ApiException as e:
    print("Exception when calling TagsApi->delete_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tag_id** | **int**| ID of tag | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tag_by_id**
> Tag get_tag_by_id(tag_id)

Find information about tag by ID

Returns a single tag

### Example 
```python
from __future__ import print_statement
import time
import selectel_dns
from selectel_dns.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = selectel_dns.TagsApi()
tag_id = 789 # int | ID of tag

try: 
    # Find information about tag by ID
    api_response = api_instance.get_tag_by_id(tag_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TagsApi->get_tag_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tag_id** | **int**| ID of tag | 

### Return type

[**Tag**](Tag.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tags**
> list[Tag] get_tags()

Getting tags



### Example 
```python
from __future__ import print_statement
import time
import selectel_dns
from selectel_dns.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = selectel_dns.TagsApi()

try: 
    # Getting tags
    api_response = api_instance.get_tags()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TagsApi->get_tags: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Tag]**](Tag.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_tag**
> Tag update_tag(tag_id, body)

Updates a tag



### Example 
```python
from __future__ import print_statement
import time
import selectel_dns
from selectel_dns.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = selectel_dns.TagsApi()
tag_id = 789 # int | ID of tag
body = selectel_dns.NewOrUpdatedTag() # NewOrUpdatedTag | Tag info for update

try: 
    # Updates a tag
    api_response = api_instance.update_tag(tag_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TagsApi->update_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tag_id** | **int**| ID of tag | 
 **body** | [**NewOrUpdatedTag**](NewOrUpdatedTag.md)| Tag info for update | 

### Return type

[**Tag**](Tag.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

