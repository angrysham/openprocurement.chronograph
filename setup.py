import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst')).read()
CHANGES = open(os.path.join(here, 'CHANGES.rst')).read()

requires = [
    'SQLAlchemy',
    'apscheduler',
    'chaussette',
    'couchdb',
    'grequests',
    'iso8601',
    'ndg-httpsclient',
    'pbkdf2',
    'pyasn1',
    'pyopenssl',
    'pyramid',
    'pyramid_exclog',
    'pysqlite',
    'setuptools',
]

test_requires = requires + [
    'openprocurement.api',
    'openprocurement.auctions.flash',
    'webtest',
]

setup(name='openprocurement.chronograph',
      version='0.6.5-sale',
      description='openprocurement.chronograph',
      long_description=README + '\n\n' + CHANGES,
      classifiers=[
          "Programming Language :: Python",
          "Framework :: Pyramid",
          "Topic :: Internet :: WWW/HTTP",
          "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
      ],
      author='Quintagroup, Ltd.',
      author_email='info@quintagroup.com',
      url='https://github.com/prozorro-sale/openprocurement.chronograph',
      keywords='web pyramid pylons',
      packages=find_packages(),
      namespace_packages=['openprocurement'],
      include_package_data=True,
      zip_safe=False,
      install_requires=requires,
      tests_require=test_requires,
      extras_require={'test': test_requires},
      test_suite="openprocurement.chronograph.tests.test.suite",
      entry_points="""\
      [paste.app_factory]
      main = openprocurement.chronograph:main
      """,
      )
