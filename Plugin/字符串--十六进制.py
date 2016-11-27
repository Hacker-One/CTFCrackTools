#coding=utf-8

import binascii
def run(data):
  code = binascii.b2a_hex(data)
  return code
