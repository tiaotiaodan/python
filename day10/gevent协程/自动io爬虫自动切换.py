#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# Author:shichao
# File: .py

from gevent import monkey;

monkey.patch_all()   #把我当前程序的所有的io操作给我单独的做上标记
import gevent
from urllib.request import urlopen


def f(url):
    print('GET: %s' % url)
    resp = urlopen(url)
    data = resp.read()
    print('%d bytes received from %s.' % (len(data), url))


gevent.joinall([
    gevent.spawn(f, 'https://www.python.org/'),
    gevent.spawn(f, 'https://www.yahoo.com/'),
    gevent.spawn(f, 'https://github.com/'),
])