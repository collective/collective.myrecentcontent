from setuptools import setup, find_packages
import os

version = '0.1'

tests_require = ['plone.app.testing']

setup(name='collective.myrecentcontent',
      version=version,
      description="A dropdown menu of links to content recently acted upon.",
      long_description=open("README.rst").read() + "\n" +
                       open(os.path.join("CHANGES.rst")).read(),
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='Plone',
      author='Ross Patterson',
      author_email='me@rpatterson.net',
      url='http://github.com/rpatterson/collective.upgrade',
      license='GPL',
      packages=find_packages('src', exclude=['ez_setup']),
      package_dir = {'':'src'},
      namespace_packages=['collective'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
          'plone.app.contentmenu',
      ],
      tests_require=tests_require,
      extras_require=dict(test=tests_require),
      test_suite = 'collective.upgrade.tests.test_suite',
      scripts=['run-portal-upgrades'],
      entry_points="""
      # -*- Entry points: -*-
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
