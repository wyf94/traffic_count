## ! DO NOT MANUALLY INVOKE THIS setup.py, USE CATKIN INSTEAD

#from setuptools import setup
from distutils.core import setup
from catkin_pkg.python_setup import generate_distutils_setup

# fetch values from package.xml
setup_args = generate_distutils_setup(
    version='0.0.0',
    scripts=['node/boxes_fusion_node.py'],
    packages=['boxes_fusion'], 
    package_dir={'': 'src'},
    requires=['std_msgs', 'rospy', 'sensor_msgs']
)

setup(**setup_args)