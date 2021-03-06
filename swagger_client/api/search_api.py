# coding: utf-8

"""
    Simpplr APIs

    This collection of Simpplr APIs lets developers create and manage content outside the Simpplr UI. We have APIs for notifications, alerts, app searches, and content creation. Looking for parameters or code samples? Click on an endpoint to see a sample snippet along with descriptions of its parameters and responses.  If you have questions about an API, reach out to us support@simpplr.com  # noqa: E501

    OpenAPI spec version: 0.1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class SearchApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def content_search(self, data, **kwargs):  # noqa: E501
        """Search a Content  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.content_search(data, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Content data: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.content_search_with_http_info(data, **kwargs)  # noqa: E501
        else:
            (data) = self.content_search_with_http_info(data, **kwargs)  # noqa: E501
            return data

    def content_search_with_http_info(self, data, **kwargs):  # noqa: E501
        """Search a Content  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.content_search_with_http_info(data, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Content data: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['data']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method content_search" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'data' is set
        if ('data' not in params or
                params['data'] is None):
            raise ValueError("Missing the required parameter `data` when calling `content_search`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'data' in params:
            form_params.append(('data', params['data']))  # noqa: E501

        body_params = None
        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/x-www-form-urlencoded'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/apex/DataServerRW?target=ExternalSearchDataServer&action=externalSearch&searchForType=Content', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def external_auto_complete(self, data, **kwargs):  # noqa: E501
        """Auto Complete Search  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.external_auto_complete(data, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param AutoCompleteSearch data: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.external_auto_complete_with_http_info(data, **kwargs)  # noqa: E501
        else:
            (data) = self.external_auto_complete_with_http_info(data, **kwargs)  # noqa: E501
            return data

    def external_auto_complete_with_http_info(self, data, **kwargs):  # noqa: E501
        """Auto Complete Search  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.external_auto_complete_with_http_info(data, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param AutoCompleteSearch data: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['data']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method external_auto_complete" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'data' is set
        if ('data' not in params or
                params['data'] is None):
            raise ValueError("Missing the required parameter `data` when calling `external_auto_complete`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'data' in params:
            form_params.append(('data', params['data']))  # noqa: E501

        body_params = None
        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/x-www-form-urlencoded'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/apex/DataServerRW?target=ExternalSearchDataServer&action=externalAutoComplete', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def file_search(self, data, **kwargs):  # noqa: E501
        """Search a File  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.file_search(data, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param File data: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.file_search_with_http_info(data, **kwargs)  # noqa: E501
        else:
            (data) = self.file_search_with_http_info(data, **kwargs)  # noqa: E501
            return data

    def file_search_with_http_info(self, data, **kwargs):  # noqa: E501
        """Search a File  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.file_search_with_http_info(data, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param File data: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['data']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method file_search" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'data' is set
        if ('data' not in params or
                params['data'] is None):
            raise ValueError("Missing the required parameter `data` when calling `file_search`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'data' in params:
            form_params.append(('data', params['data']))  # noqa: E501

        body_params = None
        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/x-www-form-urlencoded'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/apex/DataServerRW?target=ExternalSearchDataServer&action=externalSearch&searchForType=File', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def search_feed_posts(self, size, subject_id, type, term, sort, **kwargs):  # noqa: E501
        """Search feed posts  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.search_feed_posts(size, subject_id, type, term, sort, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str size: (required)
        :param str subject_id: me (required)
        :param str type: company (required)
        :param str term: which need to be searched (required)
        :param str sort: by date (required)
        :param str next_page_token: _
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.search_feed_posts_with_http_info(size, subject_id, type, term, sort, **kwargs)  # noqa: E501
        else:
            (data) = self.search_feed_posts_with_http_info(size, subject_id, type, term, sort, **kwargs)  # noqa: E501
            return data

    def search_feed_posts_with_http_info(self, size, subject_id, type, term, sort, **kwargs):  # noqa: E501
        """Search feed posts  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.search_feed_posts_with_http_info(size, subject_id, type, term, sort, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str size: (required)
        :param str subject_id: me (required)
        :param str type: company (required)
        :param str term: which need to be searched (required)
        :param str sort: by date (required)
        :param str next_page_token: _
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['size', 'subject_id', 'type', 'term', 'sort', 'next_page_token']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method search_feed_posts" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'size' is set
        if ('size' not in params or
                params['size'] is None):
            raise ValueError("Missing the required parameter `size` when calling `search_feed_posts`")  # noqa: E501
        # verify the required parameter 'subject_id' is set
        if ('subject_id' not in params or
                params['subject_id'] is None):
            raise ValueError("Missing the required parameter `subject_id` when calling `search_feed_posts`")  # noqa: E501
        # verify the required parameter 'type' is set
        if ('type' not in params or
                params['type'] is None):
            raise ValueError("Missing the required parameter `type` when calling `search_feed_posts`")  # noqa: E501
        # verify the required parameter 'term' is set
        if ('term' not in params or
                params['term'] is None):
            raise ValueError("Missing the required parameter `term` when calling `search_feed_posts`")  # noqa: E501
        # verify the required parameter 'sort' is set
        if ('sort' not in params or
                params['sort'] is None):
            raise ValueError("Missing the required parameter `sort` when calling `search_feed_posts`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'next_page_token' in params:
            query_params.append(('nextPageToken', params['next_page_token']))  # noqa: E501
        if 'size' in params:
            query_params.append(('size', params['size']))  # noqa: E501
        if 'subject_id' in params:
            query_params.append(('subjectId', params['subject_id']))  # noqa: E501
        if 'type' in params:
            query_params.append(('type', params['type']))  # noqa: E501
        if 'term' in params:
            query_params.append(('term', params['term']))  # noqa: E501
        if 'sort' in params:
            query_params.append(('sort', params['sort']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/apex/DataServerRW?target=FeedDataServer&action=search', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def site_search(self, data, **kwargs):  # noqa: E501
        """Search a Site  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.site_search(data, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Site data: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.site_search_with_http_info(data, **kwargs)  # noqa: E501
        else:
            (data) = self.site_search_with_http_info(data, **kwargs)  # noqa: E501
            return data

    def site_search_with_http_info(self, data, **kwargs):  # noqa: E501
        """Search a Site  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.site_search_with_http_info(data, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Site data: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['data']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method site_search" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'data' is set
        if ('data' not in params or
                params['data'] is None):
            raise ValueError("Missing the required parameter `data` when calling `site_search`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'data' in params:
            form_params.append(('data', params['data']))  # noqa: E501

        body_params = None
        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/x-www-form-urlencoded'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/apex/DataServerRW?target=ExternalSearchDataServer&action=externalSearch&searchForType=Site', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def top_search(self, data, **kwargs):  # noqa: E501
        """Search a Top  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.top_search(data, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Top data: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.top_search_with_http_info(data, **kwargs)  # noqa: E501
        else:
            (data) = self.top_search_with_http_info(data, **kwargs)  # noqa: E501
            return data

    def top_search_with_http_info(self, data, **kwargs):  # noqa: E501
        """Search a Top  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.top_search_with_http_info(data, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Top data: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['data']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method top_search" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'data' is set
        if ('data' not in params or
                params['data'] is None):
            raise ValueError("Missing the required parameter `data` when calling `top_search`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'data' in params:
            form_params.append(('data', params['data']))  # noqa: E501

        body_params = None
        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/x-www-form-urlencoded'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/apex/DataServerRW?target=ExternalSearchDataServer&action=externalSearch&searchForType=Top', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def user_search(self, data, **kwargs):  # noqa: E501
        """Search a User  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.user_search(data, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param User data: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.user_search_with_http_info(data, **kwargs)  # noqa: E501
        else:
            (data) = self.user_search_with_http_info(data, **kwargs)  # noqa: E501
            return data

    def user_search_with_http_info(self, data, **kwargs):  # noqa: E501
        """Search a User  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.user_search_with_http_info(data, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param User data: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['data']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method user_search" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'data' is set
        if ('data' not in params or
                params['data'] is None):
            raise ValueError("Missing the required parameter `data` when calling `user_search`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'data' in params:
            form_params.append(('data', params['data']))  # noqa: E501

        body_params = None
        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/x-www-form-urlencoded'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/apex/DataServerRW?target=ExternalSearchDataServer&action=externalSearch&searchForType=User', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
