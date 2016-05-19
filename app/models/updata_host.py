#!/bin/env python
import salt.client
import os,sys
import django

BASE_DIR = "/cms/app"
area_name = 'staging'
group_name = "APP"
#BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if BASE_DIR not in sys.path:
  sys.path.append(BASE_DIR)

def get_host_info(hostname='*'):
  client = salt.client.LocalClient()
  ret = client.cmd(hostname,'grains.items')
  return ret

def write_database():
  for hostname in info:
    ip = info[hostname]['ipv4'][1]
    area = Area.objects.get(area_name = area_name)
    a = Group.objects.get(group_name = group_name)
    host = Host(host_name=hostname,area=area,host_lip=ip,group=a,host_wip='null')
    host.save()

if __name__ == "__main__":
  os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app1.settings")
  django.setup()
  from app1.models import *
  info = get_host_info()
  write_database()


