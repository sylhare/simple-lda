from setuptools import setup, find_packages


def get_long_description():
    try:
        import pypandoc

        pypandoc.convert_file('README.md', 'rst', outputfile="readme.rst")
        with open("readme.rst", 'r') as f:
            readme = f.read()
    except ImportError:
        readme = 'Python library for Latent Dirichlet allocation (lda)'
        print("Install pypandoc and pandoc to generate long description")

    return readme


setup(name='simple-lda',
      version='0.3.0',
      description='Python library for Latent Dirichlet allocation (lda)',
      long_description=get_long_description(),
      author='sylhare',
      author_email='sylhare@outlook.com',
      url='https://github.com/Sylhare/simple-lda',
      license='Apache License 2.0',
      tests_require=['pytest'],
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
