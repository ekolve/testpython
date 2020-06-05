from setuptools import setup, find_packages
import re
import subprocess





git_tag_version = (
    subprocess.check_output("git describe --tags", shell=True)
    .decode("ascii")
    .strip()
)



if not re.match(r'^[0-9]+\.[0-9]+\.[0-9]+', git_tag_version):
    raise Exception("Invalid git tag version number: %s" % git_tag_version)

VERSION = git_tag_version



setup(name='ekolve-testpython',
      version=VERSION,
      description='testdescribe',
      long_description="test long",
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.3',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: 3.7'
      ],
      keywords='test keyword',
      url='https://github.com/ekolve/testpython',
      author='eric kolve',
      author_email='ekolve@gmail.com',
      license='Apache',
      packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
      install_requires=[
          'requests'
      ],
      include_package_data=False)


