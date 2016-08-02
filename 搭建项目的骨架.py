# -- coding: utf-8 --

# 习题46:创建一个项目的骨架

"""
项目运行所有基本内容:项目文件布局、自动化测试代码,模组,以及 安装脚本 

当你建立一个新项目的时候,只要把这个目录复制过去,改改目录的 名字,再编辑里边的文件就行了。
"""


# 1.创建骨架的目录

~ $ mkdir -p projects
~ $ cd projects/
~/projects $ mkdir skeleton
~/projects $ cd skeleton
~/projects/skeleton $ mkdir bin NAME tests docs		# NAME是项目的主文件夹,可以任意取名

# 2.配置一些初始文件
~/projects/skeleton $ touch NAME/__init__.py 

~/projects/skeleton $ touch tests/__init__.py
## 以上命令为你创建了空模组目录,以便以后添加代码

# 3.创建一个setup.py文件内容如下
try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup
	
config = {
'description': 'My Project',
'author': 'My Name',
'telephone': '3133131', # 电话

'url': 'URL to get it at.', 'download_url': 'Where to download it.', 'author_email': 'My email.',
'version': '0.1',
'install_requires': ['nose'], 'packages': ['NAME'],
'scripts': [],
'name': 'projectname'
}
setup(**config)

## 这个文件在安装项目时候会用到


# 4.创建一个简单的测试专用骨架文件 tests/NAME_tests.py Name是项目名
import os
import re
import shutil
import sys

# 判断python的版本是否 < 2.6
if sys.version_info[:2] < (2, 6):
    sys.exit('virtualenv requires Python 2.6 or higher.')

# 尝试执行这段代码
try:
    from setuptools import setup
    from setuptools.command.test import test as TestCommand

    class PyTest(TestCommand):
        user_options = [('pytest-args=', 'a', "Arguments to pass to py.test")]

        def initialize_options(self):
            TestCommand.initialize_options(self)
            self.pytest_args = []

        def finalize_options(self):
            TestCommand.finalize_options(self)
            #self.test_args = []
            #self.test_suite = True

        def run_tests(self):
            # import here, because outside the eggs aren't loaded
            import pytest
            sys.exit(pytest.main(self.pytest_args))

    setup_params = {
        'entry_points': {
            'console_scripts': ['virtualenv=virtualenv:main'],
        },
        'zip_safe': False,
        'cmdclass': {'test': PyTest},
        'tests_require': ['pytest', 'mock'],
    }
except ImportError:
    from distutils.core import setup
    if sys.platform == 'win32':
        print('Note: without Setuptools installed you will '
              'have to use "python -m virtualenv ENV"')
        setup_params = {}
    else:
        script = 'scripts/virtualenv'
        setup_params = {'scripts': [script]}


def read_file(*paths):
    here = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(here, *paths)) as f:
        return f.read()

# Get long_description from index.rst:
long_description = read_file('docs', 'index.rst')
long_description = long_description.strip().split('split here', 1)[0]
# Add release history
changes = read_file('docs', 'changes.rst')
# Only report last two releases for brevity
releases_found = 0
change_lines = []
for line in changes.splitlines():
    change_lines.append(line)
    if line.startswith('--------------'):
        releases_found += 1
    if releases_found > 2:
        break

changes = '\n'.join(change_lines[:-2]) + '\n'
changes += '`Full Changelog <https://virtualenv.pypa.io/en/latest/changes.html>`_.'
# Replace issue/pull directives
changes = re.sub(r':pull:`(\d+)`', r'PR #\1', changes)
changes = re.sub(r':issue:`(\d+)`', r'#\1', changes)

long_description += '\n\n' + changes


def get_version():
    version_file = read_file('virtualenv.py')
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


# Hack to prevent stupid TypeError: 'NoneType' object is not callable error on
# exit of python setup.py test # in multiprocessing/util.py _exit_function when
# running python setup.py test (see
# http://www.eby-sarna.com/pipermail/peak/2010-May/003357.html)
try:
    import multiprocessing  # noqa
except ImportError:
    pass

setup(
    name='virtualenv',
    version=get_version(),
    description="Virtual Python Environment builder",
    long_description=long_description,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    keywords='setuptools deployment installation distutils',
    author='Ian Bicking',
    author_email='ianb@colorstudy.com',
    maintainer='Jannis Leidel, Carl Meyer and Brian Rosner',
    maintainer_email='python-virtualenv@groups.google.com',
    url='https://virtualenv.pypa.io/',
    license='MIT',
    py_modules=['virtualenv'],
    packages=['virtualenv_support'],
    package_data={'virtualenv_support': ['*.whl']},
    **setup_params)

from nose.tools import * 
import NAME  
                    
def setup():
	print "SETUP!"
	
def teardown():
	print "TEAR DOWN!"
	
def test_basic(): 
	print "I RAN!"
	



# 5.软件包的安装
	pip – http://pypi.python.org/pypi/pip
	distribute – http://pypi.python.org/pypi/distribute
	nose – http://pypi.python.org/pypi/nose/
	virtualenv – http://pypi.python.org/pypi/virtualenv
	
	
	
	
# 6.使用这个骨架

每次你要新建一个项目时,只要做下面的 事情就可以了:
1. 拷贝这份骨架目录,把名字改成你新项目的名字。
2. 再将 NAME 模组更名为你需要的名字,它可以是你项目的名字,当然别的名字也
行。
3. 编辑 setup.py 让它包含你新项目的相关信息。
4. 重命名 tests/NAME_tests.py ,让它的名字匹配到你模组的名字。
5. 使用 nosetests 检查有无错误。
6. 开始写代码吧。

主文件夹NAME 为模组,将NAME改掉





