# !/usr/bin/env python3
# -*- coding: utf-8 -*-
from django.test import TestCase
from django.urls import resolve

from bugreport.views import create_report
from accounts.views import login_view, register


class ResolversTest(TestCase):

    def test_login_url_resolves_to_login_view(self):
        view = resolve('/login/')
        self.assertEquals(view.func, login_view)

    def test_home_url_resolves_to_home_view(self):
        view = resolve('/home/')
        self.assertEquals(view.func, create_report)

    def test_register_url_resolves_to_register_view(self):
        view = resolve('/register/')
        self.assertEquals(view.func, register)
