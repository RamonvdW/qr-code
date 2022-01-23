# -*- coding: utf-8 -*-

#  Copyright (c) 2022 Ramon van der Winkel.
#  All rights reserved.
#  Licensed under BSD-3-Clause-Clear. See LICENSE file for details.

from django.urls import path
from QRcode import views

app_name = 'QRcode'

urlpatterns = [
    path('',
         views.ShowView.as_view(),
         name='show'),
]

# end of file
