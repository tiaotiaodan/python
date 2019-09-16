#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# Author:shichao
# File: .py

import  hashlib

h = hashlib.md5()
h.update("admin".encode(encoding="utf-8"))
print(h.hexdigest())




# import  hmac
#
# h = hmac.new(b"12345",b"you ni 543")
# print(h.digest())
# print(h.hexdigest())