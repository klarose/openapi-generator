"""
    OpenAPI Petstore

    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from petstore_api.api_client import ApiClient, Endpoint as _Endpoint
from petstore_api.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from petstore_api.model.client import Client


class AnotherFakeApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        def __call_123_test_special_tags(
            self,
            body,
            **kwargs
        ):
            """To test special tags  # noqa: E501

            To test special tags and operation ID starting with number  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.call_123_test_special_tags(body, async_req=True)
            >>> result = thread.get()

            Args:
                body (Client): client model

            Keyword Args:
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                Client
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['body'] = \
                body
            return self.call_with_http_info(**kwargs)

        if self.call_123_test_special_tags is None:
            self.call_123_test_special_tags = _Endpoint(
                settings={
                    'response_type': (Client,),
                    'auth': [],
                    'endpoint_path': '/another-fake/dummy',
                    'operation_id': 'call_123_test_special_tags',
                    'http_method': 'PATCH',
                    'servers': None,
                },
                params_map={
                    'all': [
                        'body',
                    ],
                    'required': [
                        'body',
                    ],
                    'nullable': [
                    ],
                    'enum': [
                    ],
                    'validation': [
                    ]
                },
                root_map={
                    'validations': {
                    },
                    'allowed_values': {
                    },
                    'openapi_types': {
                        'body':
                            (Client,),
                    },
                    'attribute_map': {
                    },
                    'location_map': {
                        'body': 'body',
                    },
                    'collection_format_map': {
                    }
                },
                headers_map={
                    'accept': [
                        'application/json'
                    ],
                    'content_type': [
                        'application/json'
                    ]
                },
                api_client=api_client,
                callable=__call_123_test_special_tags
            )

    call_123_test_special_tags = None 
