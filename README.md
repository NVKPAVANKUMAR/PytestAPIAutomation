# pytest-automation-framework

This repo contains example tests for https://automationexercise.com/api_list

## Python Setup

Python setup can be complicated. This section documents how to set up your machine for Python test automation
development.

### Python Installation and Tools

This project requires Python 3. You can download the latest Python version from Python.org. Follow the appropriate
installation instructions for your operating system.

You should have basic Python programming skills before attempting this project. Learning the language is always a
prerequisite for learning automation. If you need help learning Python, check out this article: How Do I Start Learning
Python?

You should also have a good Python editor/IDE. Good choices include PyCharm and Visual Studio Code.

You will also need Git if you want to clone this repository locally. If you are new to Git, try learning the basics.

### Python Installation Troubleshooting

Unfortunately, installing Python properly can be complicated, especially if Python was previously installed on your
machine. To verify your Python installation, enter python --version at the command line. You should see the proper
version printed.

If the python command doesn't work or doesn’t print the expected version number, then try using the python3 command
instead. If that still doesn't work, then the correct Python installation might not be included in your system path.
Find the directory into which Python was installed, manually add it to the system path, relaunch the command line, and
try running Python again.

### Virtual Environments

Running pip install will install the pytest package globally for the whole system. Installing Python packages globally
is okay for this project, but it typically isn't a best practice in the "read world." Instead, each project should
manage its own dependencies locally using a virtual environment. Virtual environments let projects avoid unnecessary
dependencies and version mismatches.

For simplicity, this project will not use or teach virtual environments. If you would like to learn virtual environments
on your own, then RealPython's article Python Virtual Environments: A Primer is an excellent place to start.

### Package Versions

The requirements.txt file contains the versions for each package used in this project.

## Running Tests

To run the example tests from the command line, run python -m pytest from the project root directory. This command will
discover and run all tests in the project.


