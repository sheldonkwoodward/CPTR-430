# sheldon woodward
# 4/14/18

from setuptools import setup

setup(name='sw_cptr_430',
      version='1.0.0',
      packages=['river_crossing'],
      entry_points={
          'console_scripts': [
              'river_crossing = river_crossing.__main__:main'
          ]
      },
      )