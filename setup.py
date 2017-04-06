from setuptools import setup

setup(
    name="extra-kata",
    description="extra kata",
    version=1.1,
    author="Ben Shields",
    author_email="",
    license="MIT",
    package_dir={'': 'src'},
    py_modules=["forbes", "string_pyramid"],
    install_requires=[],
    extras_require={"test": ["pytest", "pytest-watch", "pytest-cov", "tox"]},
    entry_points={}
)