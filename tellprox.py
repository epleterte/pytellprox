#!/usr/bin/env python3

import requests

DEBUG=False

# class TellProx(host,port = '8080'):
#   def __init__():
#     self.host = host
#     self.port = port
#   def toggle_device(id):
#

def toggle_device(id, host, port = '8080'):
  isnum = id
  try:
    isnum += 1
  except TypeError:
    return False
  payload = {'id': id}
  r = requests.get('http://%s:%s/json/device/toggle?key=&id=%s' % (host,port,id))
  if DEBUG:
    print(r.url)
  # I think the response needs parsing...but let's assume this works:
  if r.status_code == requests.codes.ok:
    return True
  return False

def enable_device(id, host, port = '8080'):
  isnum = id
  try:
    isnum += 1
  except TypeError:
    return False
  payload = {'id': id}
  r = requests.get('http://%s:%s/json/device/turnon?key=&id=%s' % (host,port,id))
  if DEBUG:
    print(r.url)
  # I think the response needs parsing...but let's assume this works:
  if r.status_code == requests.codes.ok:
    return True
  return False

def disable_device(id, host, port = '8080'):
  isnum = id
  try:
    isnum += 1
  except TypeError:
    return False
  payload = {'id': id}
  r = requests.get('http://%s:%s/json/device/turnoff?key=&id=%s' % (host,port,id))
  if DEBUG:
    print(r.url)
  # I think the response needs parsing...but let's assume this works:
  if r.status_code == requests.codes.ok:
    return True
  return False
