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
from petstore_api.model.pet import Pet


class PetApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        def __add_pet(
            self,
            pet,
            **kwargs
        ):
            """Add a new pet to the store  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.add_pet(pet, async_req=True)
            >>> result = thread.get()

            Args:
                pet (Pet): Pet object that needs to be added to the store

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
                None
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
            kwargs['pet'] = \
                pet
            return self.call_with_http_info(**kwargs)

        if self.add_pet is None:
            self.add_pet = _Endpoint(
                settings={
                    'response_type': None,
                    'auth': [
                        'http_signature_test',
                        'petstore_auth'
                    ],
                    'endpoint_path': '/pet',
                    'operation_id': 'add_pet',
                    'http_method': 'POST',
                    'servers': [
                        {
                            'url': "http://petstore.swagger.io/v2",
                            'description': "No description provided",
                        },
                        {
                            'url': "http://path-server-test.petstore.local/v2",
                            'description': "No description provided",
                        },
                    ]
                },
                params_map={
                    'all': [
                        'pet',
                    ],
                    'required': [
                        'pet',
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
                        'pet':
                            (Pet,),
                    },
                    'attribute_map': {
                    },
                    'location_map': {
                        'pet': 'body',
                    },
                    'collection_format_map': {
                    }
                },
                headers_map={
                    'accept': [],
                    'content_type': [
                        'application/json',
                        'application/xml'
                    ]
                },
                api_client=api_client,
                callable=__add_pet
            )

        def __delete_pet(
            self,
            pet_id,
            **kwargs
        ):
            """Deletes a pet  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.delete_pet(pet_id, async_req=True)
            >>> result = thread.get()

            Args:
                pet_id (int): Pet id to delete

            Keyword Args:
                api_key (str): [optional]
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
                None
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
            kwargs['pet_id'] = \
                pet_id
            return self.call_with_http_info(**kwargs)

        if self.delete_pet is None:
            self.delete_pet = _Endpoint(
                settings={
                    'response_type': None,
                    'auth': [
                        'petstore_auth'
                    ],
                    'endpoint_path': '/pet/{petId}',
                    'operation_id': 'delete_pet',
                    'http_method': 'DELETE',
                    'servers': None,
                },
                params_map={
                    'all': [
                        'pet_id',
                        'api_key',
                    ],
                    'required': [
                        'pet_id',
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
                        'pet_id':
                            (int,),
                        'api_key':
                            (str,),
                    },
                    'attribute_map': {
                        'pet_id': 'petId',
                        'api_key': 'api_key',
                    },
                    'location_map': {
                        'pet_id': 'path',
                        'api_key': 'header',
                    },
                    'collection_format_map': {
                    }
                },
                headers_map={
                    'accept': [],
                    'content_type': [],
                },
                api_client=api_client,
                callable=__delete_pet
            )

        def __find_pets_by_status(
            self,
            status,
            **kwargs
        ):
            """Finds Pets by status  # noqa: E501

            Multiple status values can be provided with comma separated strings  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.find_pets_by_status(status, async_req=True)
            >>> result = thread.get()

            Args:
                status ([str]): Status values that need to be considered for filter

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
                [Pet]
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
            kwargs['status'] = \
                status
            return self.call_with_http_info(**kwargs)

        if self.find_pets_by_status is None:
            self.find_pets_by_status = _Endpoint(
                settings={
                    'response_type': ([Pet],),
                    'auth': [
                        'http_signature_test',
                        'petstore_auth'
                    ],
                    'endpoint_path': '/pet/findByStatus',
                    'operation_id': 'find_pets_by_status',
                    'http_method': 'GET',
                    'servers': None,
                },
                params_map={
                    'all': [
                        'status',
                    ],
                    'required': [
                        'status',
                    ],
                    'nullable': [
                    ],
                    'enum': [
                        'status',
                    ],
                    'validation': [
                    ]
                },
                root_map={
                    'validations': {
                    },
                    'allowed_values': {
                        ('status',): {

                            "AVAILABLE": "available",
                            "PENDING": "pending",
                            "SOLD": "sold"
                        },
                    },
                    'openapi_types': {
                        'status':
                            ([str],),
                    },
                    'attribute_map': {
                        'status': 'status',
                    },
                    'location_map': {
                        'status': 'query',
                    },
                    'collection_format_map': {
                        'status': 'csv',
                    }
                },
                headers_map={
                    'accept': [
                        'application/xml',
                        'application/json'
                    ],
                    'content_type': [],
                },
                api_client=api_client,
                callable=__find_pets_by_status
            )

        def __find_pets_by_tags(
            self,
            tags,
            **kwargs
        ):
            """Finds Pets by tags  # noqa: E501

            Multiple tags can be provided with comma separated strings. Use tag1, tag2, tag3 for testing.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.find_pets_by_tags(tags, async_req=True)
            >>> result = thread.get()

            Args:
                tags ([str]): Tags to filter by

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
                [Pet]
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
            kwargs['tags'] = \
                tags
            return self.call_with_http_info(**kwargs)

        if self.find_pets_by_tags is None:
            self.find_pets_by_tags = _Endpoint(
                settings={
                    'response_type': ([Pet],),
                    'auth': [
                        'http_signature_test',
                        'petstore_auth'
                    ],
                    'endpoint_path': '/pet/findByTags',
                    'operation_id': 'find_pets_by_tags',
                    'http_method': 'GET',
                    'servers': None,
                },
                params_map={
                    'all': [
                        'tags',
                    ],
                    'required': [
                        'tags',
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
                        'tags':
                            ([str],),
                    },
                    'attribute_map': {
                        'tags': 'tags',
                    },
                    'location_map': {
                        'tags': 'query',
                    },
                    'collection_format_map': {
                        'tags': 'csv',
                    }
                },
                headers_map={
                    'accept': [
                        'application/xml',
                        'application/json'
                    ],
                    'content_type': [],
                },
                api_client=api_client,
                callable=__find_pets_by_tags
            )

        def __get_pet_by_id(
            self,
            pet_id,
            **kwargs
        ):
            """Find pet by ID  # noqa: E501

            Returns a single pet  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.get_pet_by_id(pet_id, async_req=True)
            >>> result = thread.get()

            Args:
                pet_id (int): ID of pet to return

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
                Pet
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
            kwargs['pet_id'] = \
                pet_id
            return self.call_with_http_info(**kwargs)

        if self.get_pet_by_id is None:
            self.get_pet_by_id = _Endpoint(
                settings={
                    'response_type': (Pet,),
                    'auth': [
                        'api_key'
                    ],
                    'endpoint_path': '/pet/{petId}',
                    'operation_id': 'get_pet_by_id',
                    'http_method': 'GET',
                    'servers': None,
                },
                params_map={
                    'all': [
                        'pet_id',
                    ],
                    'required': [
                        'pet_id',
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
                        'pet_id':
                            (int,),
                    },
                    'attribute_map': {
                        'pet_id': 'petId',
                    },
                    'location_map': {
                        'pet_id': 'path',
                    },
                    'collection_format_map': {
                    }
                },
                headers_map={
                    'accept': [
                        'application/xml',
                        'application/json'
                    ],
                    'content_type': [],
                },
                api_client=api_client,
                callable=__get_pet_by_id
            )

        def __update_pet(
            self,
            pet,
            **kwargs
        ):
            """Update an existing pet  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.update_pet(pet, async_req=True)
            >>> result = thread.get()

            Args:
                pet (Pet): Pet object that needs to be added to the store

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
                None
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
            kwargs['pet'] = \
                pet
            return self.call_with_http_info(**kwargs)

        if self.update_pet is None:
            self.update_pet = _Endpoint(
                settings={
                    'response_type': None,
                    'auth': [
                        'http_signature_test',
                        'petstore_auth'
                    ],
                    'endpoint_path': '/pet',
                    'operation_id': 'update_pet',
                    'http_method': 'PUT',
                    'servers': [
                        {
                            'url': "http://petstore.swagger.io/v2",
                            'description': "No description provided",
                        },
                        {
                            'url': "http://path-server-test.petstore.local/v2",
                            'description': "No description provided",
                        },
                    ]
                },
                params_map={
                    'all': [
                        'pet',
                    ],
                    'required': [
                        'pet',
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
                        'pet':
                            (Pet,),
                    },
                    'attribute_map': {
                    },
                    'location_map': {
                        'pet': 'body',
                    },
                    'collection_format_map': {
                    }
                },
                headers_map={
                    'accept': [],
                    'content_type': [
                        'application/json',
                        'application/xml'
                    ]
                },
                api_client=api_client,
                callable=__update_pet
            )

        def __update_pet_with_form(
            self,
            pet_id,
            **kwargs
        ):
            """Updates a pet in the store with form data  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.update_pet_with_form(pet_id, async_req=True)
            >>> result = thread.get()

            Args:
                pet_id (int): ID of pet that needs to be updated

            Keyword Args:
                name (str): Updated name of the pet. [optional]
                status (str): Updated status of the pet. [optional]
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
                None
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
            kwargs['pet_id'] = \
                pet_id
            return self.call_with_http_info(**kwargs)

        if self.update_pet_with_form is None:
            self.update_pet_with_form = _Endpoint(
                settings={
                    'response_type': None,
                    'auth': [
                        'petstore_auth'
                    ],
                    'endpoint_path': '/pet/{petId}',
                    'operation_id': 'update_pet_with_form',
                    'http_method': 'POST',
                    'servers': None,
                },
                params_map={
                    'all': [
                        'pet_id',
                        'name',
                        'status',
                    ],
                    'required': [
                        'pet_id',
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
                        'pet_id':
                            (int,),
                        'name':
                            (str,),
                        'status':
                            (str,),
                    },
                    'attribute_map': {
                        'pet_id': 'petId',
                        'name': 'name',
                        'status': 'status',
                    },
                    'location_map': {
                        'pet_id': 'path',
                        'name': 'form',
                        'status': 'form',
                    },
                    'collection_format_map': {
                    }
                },
                headers_map={
                    'accept': [],
                    'content_type': [
                        'application/x-www-form-urlencoded'
                    ]
                },
                api_client=api_client,
                callable=__update_pet_with_form
            )

    add_pet = None 
    delete_pet = None 
    find_pets_by_status = None 
    find_pets_by_tags = None 
    get_pet_by_id = None 
    update_pet = None 
    update_pet_with_form = None 
