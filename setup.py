from cx_Freeze import setup, Executable
import sys

buildOptions = dict(packages = ["matplotlib","missingno","tkinter", "pandas", "datetime"],  # 1
excludes = [""])

exe = [Executable("main.py")]  # 2

# 3
setup(
    name= 'AutoPreprocessing',
    version = '0.1',
    author = "DaegiYeo, JingyoLee, SuminKim",
    description = "help data preprocessing",
    options = dict(build_exe = buildOptions),
    executables = exe
)