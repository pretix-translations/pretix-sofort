import os
from distutils.command.build import build

from django.core import management
from setuptools import setup, find_packages


try:
    with open(os.path.join(os.path.dirname(__file__), 'README.rst'), encoding='utf-8') as f:
        long_description = f.read()
except:
    long_description = ''


class CustomBuild(build):
    def run(self):
        management.call_command('compilemessages', verbosity=1)
        build.run(self)


cmdclass = {
    'build': CustomBuild
}


setup(
    name='pretix-sofort',
    version='1.3.1',
    description='pretix payment via Klarna Sofort',
    long_description=long_description,
    url='https://github.com/pretix/pretix-sofort',
    author='Raphael Michel',
    author_email='michel@rami.io',
    license='Apache Software License',

    install_requires=['lxml'],
    packages=find_packages(exclude=['tests', 'tests.*']),
    include_package_data=True,
    cmdclass=cmdclass,
    entry_points="""
[pretix.plugin]
pretix_sofort=pretix_sofort:PretixPluginMeta
""",
)
