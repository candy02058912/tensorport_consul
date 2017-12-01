from setuptools import setup, find_packages

setup(
    name='tensorport_consul',
    version=1.0.0,
    py_modules=[
        'api', 'serializer', 'settings', 'utils',
    ],
    packages=find_packages(),
    include_package_data=True,
    python_requires='>2.6, !=3.0.*, !=3.1.*, !=3.2.*, <4',
    install_requires=[
        'requests',
    ],
    entry_points='''
        [console_scripts]
    ''',

    author="TensorPort",
    author_email="info@tensorport.com",
    description="TensorPort Consul API library.",
    license="Apache Software License",
    keywords="",
    url="http://tensorport.com",
)
