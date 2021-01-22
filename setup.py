from setuptools import setup

setup(name='myquickdateutil',
      version='0.1',
      description='Quick date functions for my location',
      url='http://github.com/raph84/my_quick_date_util',
      author='raph84',
      author_email='raph.berube@gmail.com',
      license='GNU GPLv3',
      #packages=['my_quick_date_util'],
      install_requires=[
          'pytz',
      ],
      zip_safe=False)
