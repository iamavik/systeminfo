'''
Created on 29-Jan-2019

@author: avik
'''
from setuptools import setup
setup(name="systeminfo",version="0.1",description="Basic system information for COMP30380",url="",author="Avik Saha",author_email="avik.saha@ucdconnect.ie",licence="GPL3",packages=['systeminfo'],entry_points={'console_scripts':['comp30830_systeminfo=systeminfo.main:main']})
