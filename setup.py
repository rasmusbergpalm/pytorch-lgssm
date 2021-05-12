from setuptools import setup

setup(name='lgssm',
      version='1.0.0',
      description='A minimal Linear Gaussian State Space Model for pytorch.',
      url='git@github.com:rasmusbergpalm/pytorch-lgssm.git',
      maintainer='Rasmus Berg Palm',
      maintainer_email='rasmusbergpalm@gmail.com',
      license='MIT',
      packages=['lgssm'],
      zip_safe=False,
      install_requires=[
          'torch>=1.4.0'
      ])
