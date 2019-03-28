import os
import shutil
from setuptools import setup


if __name__ == "__main__":
    setup(
        name="egg_test",
        packages=['egg_test'],
        version="1.0",
        script_args=['--quiet', 'bdist_egg'], 
    )

    egg_name = os.listdir('dist')[0]

    os.rename(
        os.path.join('dist', egg_name),
        os.path.join('.', egg_name)
    )

    shutil.rmtree('build')
    shutil.rmtree('dist')
    shutil.rmtree('egg_test.egg-info')

