#!/usr/bin/env python

from setuptools import setup, Command, find_packages

setup(name='gym_unity',
      version='0.0.1',
      description='Unity Machine Learning Agents Gym Interface',
      license='Apache License 2.0',
      author='Unity Technologies',
      author_email='ML-Agents@unity3d.com',
      url='https://github.com/Unity-Technologies/ml-agents',
      packages=['gym_unity'],
      install_requires = ['gym', 'unityagents']
     )
