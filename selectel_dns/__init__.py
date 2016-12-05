# coding: utf-8

"""
    Selectel DNS API

    Simple Selectel DNS API.

    OpenAPI spec version: 1.0.0
    Contact: info@mdsina.ru
    Generated by: https://github.com/swagger-api/swagger-codegen.git

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from __future__ import absolute_import

# import models into sdk package
from .models.api_response import ApiResponse
from .models.batch_update_model import BatchUpdateModel
from .models.domain import Domain
from .models.geo_record import GeoRecord
from .models.new_domain import NewDomain
from .models.new_or_updated_ptr_record import NewOrUpdatedPTRRecord
from .models.new_or_updated_record import NewOrUpdatedRecord
from .models.new_or_updated_tag import NewOrUpdatedTag
from .models.ptr_record import PTRRecord
from .models.record import Record
from .models.tag import Tag
from .models.updated_domain import UpdatedDomain

# import apis into sdk package
from .apis.domains_api import DomainsApi
from .apis.ptr_api import PtrApi
from .apis.records_api import RecordsApi
from .apis.tags_api import TagsApi

# import ApiClient
from .api_client import ApiClient

from .configuration import Configuration

configuration = Configuration()
