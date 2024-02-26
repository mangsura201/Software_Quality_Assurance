Installation
============

OnlineBankingManagementSystem is hosted on GitHub and is publicly available at https://github.com/mangsura201/Software_Quality_Assurance.git. The entire repository can be cloned to your machine directly from GitHub, downloaded as a compressed folder, or individual files can be downloaded. Repository directories and files are described below.

Operating Systems
-----------------

The OnlineBankingManagementSystem Python code is cross-platform (Windows, Mac, Linux), and code for the `View` and `Model` packages has been tested on Windows (10) operating systems.

Dependencies
------------

1. Python version 3.10 or above is recommended.
2. Python IDE: `Visual Studio Code`.

Installing Python
-----------------

Python can be installed from a number of sources, including https://www.python.org/downloads/. Anaconda is another option which provides additional tools for Python https://www.anaconda.com/download/. This is a recommended option for novice users. Python version 3.10 or above is recommended.

.. code-block:: bash

    Step 1: Select Version of Python to Install.
    Step 2: Download Python Executable Installer.
    Step 3: Run Executable Installer.
    Step 4: Verify Python Was Installed On Windows.
    Step 5: Verify Pip Was Installed.
    Step 6: Add Python Path to Environment Variables (Optional)
    Step 7: Install virtualnv (Optional)

Check Python Version on Windows
-------------------------------

To check if you already have Python on your Windows machine, first open a command-line application, such as PowerShell. With the command line open, type in the following command and press `enter`.

.. code-block:: bash

    python --version
    or
    python -v

Installing Modules and Our Django Project
-----------------------------------------

Python modules can be installed with `pip`.

1. Make sure `pip` is up-to-date. From a terminal or the Anaconda command prompt, enter the following.

.. code-block:: bash

    pip install --upgrade pip

2. Download the project code from the main branch of the repository to your local directory.

.. code-block:: bash

    git clone https://github.com/mangsura201/Software_Quality_Assurance.git

3. Navigate into the project directory.

.. code-block:: bash
   
    cd project_directory

4. Install all project dependencies using the following command:

.. code-block:: bash

    pip install -r requirements.txt

5. Make development database migrations by running the following command:

.. code-block:: bash

    python manage.py makemigrations

6. Make development database models by running the following command:

.. code-block:: bash

    python manage.py migrate

7. Reset Django admin password.

.. code-block:: bash

    python manage.py createsuperuser

8. Run This Django project.

.. code-block:: bash

    python manage.py runserver

Installing Visual Studio Code
-----------------------------

Follow the link https://code.visualstudio.com/docs

Installing Django in Visual Studio Code
---------------------------------------

Follow the link https://code.visualstudio.com/docs/python/tutorial-django