# -*- coding: utf-8 -*-

"""Tests for `saxo_openapi` package."""

import requests_mock
from .unittestsetup import test_generic, ReqMockTest
import saxo_openapi.endpoints.rootservices as rs
from parameterized import parameterized


class TestSaxo_RootServices_Features(ReqMockTest):
    """Tests for `rootservices-features` endpoints."""

    def setUp(self):
        super(TestSaxo_RootServices_Features, self).setUp()

    @parameterized.expand([
        (rs.features, "Availability", {}),
        (rs.features, "CreateAvailabilitySubscription", {}),
        (rs.features, "RemoveAvailabilitySubscription", {}),
      ])
    @requests_mock.Mocker(kw='mock')
    def test_all(self, _mod, clsNm, route, **kwargs):
        test_generic(self, _mod, clsNm, route, **kwargs)
