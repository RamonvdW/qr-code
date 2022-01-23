# -*- coding: utf-8 -*-

#  Copyright (c) 2022 Ramon van der Winkel.
#  All rights reserved.
#  Licensed under BSD-3-Clause-Clear. See LICENSE file for details.

from django.shortcuts import redirect, render
from django.views.generic import View
from .maak_qrcode import qrcode_get
from django.http import HttpRequest

TEMPLATE_QRCODE_SHOW = 'qrcode/show.dtl'


def site_root_view(request):
    """ simple Django view function to redirect the top-level url to the main application """

    return redirect('QRcode:show')


class ShowView(View):

    def get(self, request, *args, **kwargs):
        """ called by the template system to get the context data for the template """
        template = TEMPLATE_QRCODE_SHOW
        context = dict()

        context['issuer'] = issuer = request.GET.get('issuer', default='')
        context['username'] = username = request.GET.get('username', default='')
        context['secret'] = otp_code = request.GET.get('secret', default='').replace(' ', '')

        context['qrcode'] = qrcode_get(username, otp_code, issuer)

        return render(request, template, context)

# end of file
