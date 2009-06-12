from setuptools import setup, find_packages
import os

version = '0.1dev'

setup(
    name='oc-themes-andy',
    version=version,
    description='',
    classifiers=[
        "Framework :: Plone",
        "Framework :: Zope2",
        "Framework :: Zope3",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
    keywords='',
    author='The Open Planning Project',
    author_email='',
    url='',
    license='GPL',
    packages=find_packages(exclude=['ez_setup']),
    namespace_packages=['opencore', 'opencore.themes'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools',
        ],
    entry_points="""
      # -*- Entry points: -*-
      [distutils.commands]
      zinstall = topp.utils.setup_command:zinstall
      [opencore.versions]
      oc-themes-andy = opencore.themes.andy
      [topp.zcmlloader]
      opencore = opencore.themes.andy
        """,
    )
