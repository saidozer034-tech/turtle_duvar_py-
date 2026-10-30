from setuptools import find_packages, setup

package_name = 'turtle_duvar_py'

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
    maintainer='said',
    maintainer_email='said@todo.todo',
    description='Duvardan kacan kaplumbaga odevi',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'duvar_kacan = turtle_duvar_py.duvar_kacan:main',
        ],
    },
)
