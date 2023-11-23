import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ass2srt",  # Replace with your own username
    version="0.0.5",
    author="zcq100",
    author_email="zcq100@gmail.com",
    description="A tool that convert .ass subtitles to .srt",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/zcq100/ass2srt",
    packages=setuptools.find_packages(),
    entry_points={
      'console_scripts':[
          'ass2srt=ass2srt:main',
      ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        'Topic :: Text Processing',
    ],
    python_requires='>=3.6',
)
