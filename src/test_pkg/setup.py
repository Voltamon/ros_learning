from setuptools import find_packages, setup

package_name = 'test_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
         ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='voltamon48',
    maintainer_email='voltamon48@todo.todo',
    description='TODO: Package description',
    license='Apache-2.0',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            "test_node = test_pkg.test_node:main",
            "temp_node = test_pkg.template_node:main",
            "topic_node = test_pkg.topic_node:main",
            "sub_node = test_pkg.sub_node:main",
            "srv_node = test_pkg.server_node:main",
            "client_node = test_pkg.client_node:main"
        ],
    },
)
