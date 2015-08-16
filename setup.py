from setuptools import setup

setup(name='namegen',
      version='0.1',
      description='Player, city, and team name generator',
      url='http://github.com/jamietr1/baseball-century',
      author='Jamie Todd Rubin',
      author_email='jamie@jamietoddrubin.com',
      license='MIT',
      packages=['namegen'],
      package_dir={'namegen': 'namegen'},
      package_data={'namegen': ['namegen/data/*.txt']},
      install_requires=[
      
      ],
      scripts=['bin/namegen-get'],
      include_package_data=True,
      zip_safe=False)
