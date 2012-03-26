#-*-coding:utf-8
from django.http import HttpResponse
from taobaoapi import *
import urllib, urllib2, hashlib, time, json

def index(requset):
    return HttpResponse("Hello world.")

