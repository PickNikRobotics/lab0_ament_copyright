from setuptools import find_packages
from setuptools import setup

package_name = 'lab0_ament_copyright'

setup(
    name=package_name,
    version='0.0.1',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/' + package_name, ['package.xml']),
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
    ],
    install_requires=['setuptools'],
    package_data={'': [
        'template/*',
    ]},
    zip_safe=False,
    author='Tyler Weaver',
    author_email='tyler@picknik.ai',
    maintainer='Tyler Weaver',
    maintainer_email='tyler@picknik.ai',
    url='https://github.com/PickNikRobotics/lab0_ament_copyright',
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD 3-Clause License',
        'Programming Language :: Python',
        'Topic :: Software Development',
    ],
    description='Check source files for PickNik-specific copyright reference.',
    license='BSD',
    tests_require=['pytest'],
    entry_points={
        'ament_copyright.copyright_name': [
            'lab0 = lab0_ament_copyright.copyright_names:lab0',
        ],
        'ament_copyright.license': [
            'lab0_proprietary = lab0_ament_copyright.licenses:lab0_proprietary',
        ],
    },
)
