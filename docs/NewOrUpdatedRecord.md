# NewOrUpdatedRecord

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**type** | **str** | Record type (SOA, NS, A/AAAA, CNAME, SRV, MX, TXT, SPF) | 
**ttl** | **int** |  | [optional] 
**email** | **str** | Email of domain&#39;s admin (only for SOA records) | [optional] 
**content** | **str** | Record content (not for SRV) | [optional] 
**location** | **str** |  | [optional] 
**weight** | **int** | Relative weight for records with the same priority (only for SRV) | [optional] 
**port** | **int** | Service port (only for SRV) | [optional] 
**target** | **str** | Service hostname (only for SRV) | [optional] 
**priority** | **int** | Record priority (only for SRV and MX records) | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


