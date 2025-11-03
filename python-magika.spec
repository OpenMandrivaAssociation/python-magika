Name:		python-magika
Version:	1.0.1
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/m/magika/magika-%{version}.tar.gz
Summary:	A tool to determine the content type of a file with deep learning
URL:		https://github.com/google/magika
License:	Apache-2.0
Group:		Development/Python
BuildRequires:	python
BuildRequires:  python3dist(hatchling)
BuildRequires:  pkgconfig(libonnxruntime)
Requires:  python3dist(click)
Requires:  python3dist(python-dotenv)
Requires:  python3dist(numpy)
Requires:  python3dist(onnxruntime)

BuildSystem:	python
BuildArch:	noarch

%description
Magika is a novel AI-powered file type detection tool that relies on the recent advance of deep learning to provide accurate detection. 
Under the hood, Magika employs a custom, highly optimized model that only weighs about a few MBs, and enables precise file identification within milliseconds, even when running on a single CPU. 
Magika has been trained and evaluated on a dataset of ~100M samples across 200+ content types (covering both binary and textual file formats), 
and it achieves an average ~99% accuracy on our test set.

%files
