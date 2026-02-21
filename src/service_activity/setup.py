from setuptools import find_packages, setup

package_name = 'service_activity'

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
    maintainer_email='deswarnavo@gmail.com',
    description='TODO: Package description',
    license='apache-2.0',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            "num_pub = service_activity.number_publisher:main",
            "num_count = service_activity.number_counter:main",
            "num_srv = service_activity.number_service:main",
        ],
    },
)
