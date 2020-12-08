from setuptools import setup, find_packages, find_namespace_packages
import subprocess

setup(
  name='gbtc_tracker',
  #version=version,
  package_data={'gbtc_tracker.config': ['*.ini']},
  include_package_data=True,
  packages=find_namespace_packages(),
  install_requires=[
     'coinbase',
     'termcolor'
  ],
  entry_points='''
      [console_scripts]
      track=gbtc_tracker.scripts.main:run
      ''',
)