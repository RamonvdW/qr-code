# -*- coding: utf-8 -*-

#  Copyright (c) 2022 Ramon van der Winkel.
#  All rights reserved.
#  Licensed under BSD-3-Clause-Clear. See LICENSE file for details.

# Top level URL configuration

from django.urls import path
from django.conf.urls import include
from QRcode.views import site_root_view

urlpatterns = [
    path('', site_root_view),
    path('QRcode', include('QRcode.urls'))
]

# end of file
