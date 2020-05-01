from setuptools import setup


setup(name="tap-pipedrive",
      version="1.0.6",
      description="Singer.io tap for extracting data from the Pipedrive API",
      author="Stitch",
      author_email="dev@stitchdata.com",
      url="http://singer.io",
      classifiers=["Programming Language :: Python :: 3 :: Only"],
      py_modules=["tap_pipedrive"],
      install_requires=[
          "pendulum==2.1.0",
          "singer-python>=5.8.1, <5.9",
          "requests==2.22.0",
      ],
      entry_points="""
          [console_scripts]
          tap-pipedrive=tap_pipedrive.cli:main
      """,
      packages=["tap_pipedrive",
                "tap_pipedrive.streams",
                "tap_pipedrive.streams.recents",
                "tap_pipedrive.streams.recents.dynamic_typing"],
      include_package_data=True,
)
