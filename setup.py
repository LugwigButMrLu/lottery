from setuptools import setup
import sys

# 如果你使用的是 Python 3
PYTHON_VERSION = sys.version_info[0:3]
if PYTHON_VERSION < (3, 6):
    raise RuntimeError("py2app requires Python 3.6 or later")

APP = ['main.py']  # 替换为你的主脚本文件名
DATA_FILES = []
OPTIONS = {
    'argv_emulation': True,
    'packages': ['PySide6','ui','frame', 'func'],
    'includes': ['PySide6', 'qfluentwidgets'],
    'iconfile': 'icon.icns',  # 如果你有图标文件
    'plist': {
        'CFBundleName': 'Lottery',
        'CFBundleVersion': '1.1.5',
        'CFBundleIdentifier': 'com.fcsoft.lottery',
        'LSUIElement': True,  # 如果你的应用不需要显示在 Dock 上，可以设置为 True
    },
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
