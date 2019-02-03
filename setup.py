import setuptools

with open("README.md", "r") as fd:
	long_description = fd.read()

setuptools.setup(
	name="lti-arithmetic",
	version="1.0.0",
	author="James Wilson",
	author_email="jmw@jmw.name",
	description="Arithmetical manipulation for scipy.signal.lti TransferFunction",
	long_description=long_description,
	long_description_content_type="text/markdown",
	url="https://github.com/jmwilson/lti-arithmetic",
	install_requires=[
		"numpy>=1.4",
		"scipy",
	],
	py_modules=["ltiarithmetic"],
	classifiers=[
		"License :: OSI Approved :: MIT License",
		"Topic :: Scientific/Engineering",
	],
)
