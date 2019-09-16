#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# Author:shichao
# File: .py

import xml.etree.ElementTree as ET

tree = ET.parse("xmltest.xml")
root = tree.getroot()

# 只遍历year 节点
for node in root.iter('year'):
    print(node.tag, node.text)



# 修改
for node in root.iter('year'):
    new_year = int(node.text) + 1
    node.text = str(new_year)
    node.set("updated", "yes")

tree.write("xmltest.xml")



# 只遍历year 节点
for node in root.iter('year'):
    print(node.tag, node.text)