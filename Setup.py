from setuptools import setup, find_packages

setup(name='TMS_less',
      version='0.1',
      description='Only for lesson',
      long_description='Only for lesson',
      classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Topic :: Text Processing :: Linguistic',
      ],
      keywords='lesson',
      url='http://github.com/storborg/funniest',
      author='Quwassar',
      author_email='quwassar@gmail.com',
      license='MIT',
      packages=find_packages(),
      install_requires=[
          'requests', 'datetime',
      ],
      include_package_data=True,
      zip_safe=False)