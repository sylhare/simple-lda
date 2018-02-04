from setuptools import setup, find_packages
from pypandoc import convert

LONG_DESCRIPTION = convert("README.md", 'rst')

setup(name='simple-lda',
      version='0.1.2',
      description='Python library for Latent Dirichlet allocation (lda)',
      long_description=LONG_DESCRIPTION,
      author='sylhare',
      author_email='sylhare@outlook.com',
      url='https://github.com/Sylhare/simple-lda',
      license='Apache License 2.0',
      tests_require=['pytest'],
      install_requires=['matplotlib>=2.1'],
      keywords=['prime',
                'fermat',
                'miller rabin',
                'math'],
      packages=find_packages(),
      package_data={
          'Licence': ['LICENCE.txt'],
          'Readme': ['README.md'],
      },
      platforms='any',
      zip_safe=False,
      test_suite='tests.test_lda',
      classifiers=[
          "Development Status :: 2 - Pre-Alpha",
          "Programming Language :: Python",
          "Programming Language :: Python :: 3.5",
          "Environment :: Other Environment",
          "Intended Audience :: Science/Research",
          "Intended Audience :: Education",
          "Natural Language :: English",
          "License :: OSI Approved :: Apache Software License",
          "Operating System :: OS Independent",
          "Topic :: Software Development :: Libraries",
          "Topic :: Software Development :: Libraries :: Python Modules",
          "Topic :: Text Processing",
          "Topic :: Utilities"]
      )