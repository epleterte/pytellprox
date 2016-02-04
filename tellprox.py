#!/usr/bin/env python3


import requests

DEBUG=False

class TellProx():
  def __init__(port='8080', host):
    self.host = host
    self.port = port

  def toggle_device(self, id):
    isnum = id
    try:
      isnum += 1
    except TypeError:
      return False
    payload = {'id': id}
    r = requests.get('http://%s:%s/json/device/toggle?key=&id=%s' % (self.host, self.port, id))
    if DEBUG:
      print(r.url)
    # I think the response needs parsing...but let's assume this works:
    if r.status_code == requests.codes.ok:
      return True
    return False

  def enable_device(self, id):
    isnum = id
    try:
      isnum += 1
    except TypeError:
      return False
    payload = {'id': id}
    r = requests.get('http://%s:%s/json/device/turnon?key=&id=%s' % (self.host, self.port, id))
    if DEBUG:
      print(r.url)
    # I think the response needs parsing...but let's assume this works:
    if r.status_code == requests.codes.ok:
      return True
    return False

  def disable_device(self, id):
    isnum = id
    try:
      isnum += 1
    except TypeError:
      return False
    payload = {'id': id}
    r = requests.get('http://%s:%s/json/device/turnoff?key=&id=%s' % (self.host, self.port, id))
    if DEBUG:
      print(r.url)
    # I think the response needs parsing...but let's assume this works:
    if r.status_code == requests.codes.ok:
      return True
    return False

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
