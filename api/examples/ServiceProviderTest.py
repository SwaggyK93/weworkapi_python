#!/usr/bin/env python
# -*- coding:utf-8 -*-
##
 # Copyright (C) 2018 All rights reserved.
 #   
 # @File ServiceProviderTest.py
 # @Brief 
 # @Author abelzhu, abelzhu@tencent.com
 # @Version 1.0
 # @Date 2018-02-26
 #
 #
 
import sys
sys.path.append("../src/")
sys.path.append("..")


from api.src.ServiceProviderApi import *
from api.examples.TestConf import *

api = ServiceProviderApi('CORPID', 'PROVIDER_SECRET')

try :
    response = api.httpCall(
            SERVICE_PROVIDER_API_TYPE['GET_LOGIN_INFO'],
            { 
                'auth_code' : 'XXXXXXX',
            })
    print (response)
except ApiException as e :
    print (e.errCode, e.errMsg)
