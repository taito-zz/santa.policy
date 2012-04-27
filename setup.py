from setuptools import find_packages
from setuptools import setup


setup(
    name='santa.policy',
    version='0.8',
    description="Turns Plone Site into Santa Claus Foundation Site.",
    long_description=open("README.rst").read(),
    # Get more strings from
    # http://pypi.python.org/pypi?:action=list_classifiers
    classifiers=[
    "Framework :: Plone",
    "Framework :: Plone :: 4.1",
    "Framework :: Plone :: 4.2",
    "Programming Language :: Python",
    ],
    keywords='',
    author='ABITA',
    author_email='taito.horiuchi@abita.fi',
    url='',
    license='BSD',
    packages=find_packages(exclude=['ez_setup']),
    namespace_packages=['santa'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'hexagonit.testing',
        'plone.browserlayer',
        'santa.theme',
        'setuptools',
    ],
    entry_points="""
    # -*- Entry points: -*-

    [z3c.autoinclude.plugin]
    target = plone
    """,
)
