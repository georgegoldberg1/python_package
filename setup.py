"""File to setup mypackage3 to be available globally (in conda env)"""

from setuptools import setup

setup(name='mypackage3',
      version='0.1',
      description='test package requiring pandas',
      url='http://github.com/storborg/funniest',
      author='George Goldberg',
      author_email='xxxxxxx@example.com',
      license='MIT',
      packages=['mypackage3'],
      install_requires=[
          'pandas',
      ],
      zip_safe=False)

# NOTE FROM https://python-packaging.readthedocs.io/en/latest/dependencies.html
# setup(
#     ...
#     dependency_links=['http://github.com/user/repo/tarball/master#egg=package-1.0']
#     ...
# )

# ❯ python setup.py --help
# Common commands: (see '--help-commands' for more)

#   setup.py build      will build the package underneath 'build/'
#   setup.py install    will install the package

# Global options:
#   --verbose (-v)      run verbosely (default)
#   --quiet (-q)        run quietly (turns verbosity off)
#   --dry-run (-n)      don't actually do anything
#   --help (-h)         show detailed help message
#   --no-user-cfg       ignore pydistutils.cfg in your home directory
#   --command-packages  list of packages that provide distutils commands

# Information display options (just display information, ignore any commands)
#   --help-commands     list all available commands
#   --name              print package name
#   --version (-V)      print package version
#   --fullname          print <package name>-<version>
#   --author            print the author's name
#   --author-email      print the author's email address
#   --maintainer        print the maintainer's name
#   --maintainer-email  print the maintainer's email address
#   --contact           print the maintainer's name if known, else the author's
#   --contact-email     print the maintainer's email address if known, else the
#                       author's
#   --url               print the URL for this package
#   --license           print the license of the package
#   --licence           alias for --license
#   --description       print the package description
#   --long-description  print the long package description
#   --platforms         print the list of platforms
#   --classifiers       print the list of classifiers
#   --keywords          print the list of keywords
#   --provides          print the list of packages/modules provided
#   --requires          print the list of packages/modules required
#   --obsoletes         print the list of packages/modules made obsolete