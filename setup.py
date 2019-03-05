import os
import sys
from setuptools import setup, find_packages
from tethys_apps.app_installation import custom_develop_command, custom_install_command

# -- Apps Definition -- #
app_package = 'hello_world'
release_package = 'tethysapp-' + app_package
app_class = 'hello_world.app:HelloWorld'
app_package_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'tethysapp', app_package)

# -- Python Dependencies -- #
dependencies = []

setup(
    name=release_package,
    version='0.0.1',
    tags='&quot;first app&quot;,&quot;learning&quot;,&quot;don&#39;t judge&quot;',
    description='This is a great first app that I am making',
    long_description='',
    keywords='',
    author='Dan Ames',
    author_email='dan.ames@byu.edu',
    url='',
    license='Open Source',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    namespace_packages=['tethysapp', 'tethysapp.' + app_package],
    include_package_data=True,
    zip_safe=False,
    install_requires=dependencies,
    cmdclass={
        'install': custom_install_command(app_package, app_package_dir, dependencies),
        'develop': custom_develop_command(app_package, app_package_dir, dependencies)
    }
)
