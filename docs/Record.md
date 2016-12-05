# Record

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**type** | **str** | Record type (SOA, NS, A/AAAA, CNAME, SRV, MX, TXT, SPF) | [optional] 
**ttl** | **int** |  | [optional] 
**email** | **str** | Email of domain&#39;s admin (only for SOA records) | [optional] 
**content** | **str** | Record content (not for SRV) | [optional] 
**weight** | **int** | Relative weight for records with the same priority (only for SRV) | [optional] 
**port** | **int** | Service port (only for SRV) | [optional] 
**target** | **str** | Service hostname (only for SRV) | [optional] 
**priority** | **int** | Record priority (only for SRV and MX records) | [optional] 
**create_date** | **int** | Create Date in UNIX Timestamp | [optional] 
**change_date** | **int** | Change Date in UNIX Timestamp | [optional] 
**expire** | **int** |  | [optional] 
**refresh** | **int** |  | [optional] 
**retry** | **int** |  | [optional] 
**minimum** | **int** |  | [optional] 
**ns** | **str** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


