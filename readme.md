# Scraping Data with Scrapy - Step-by-Step Guide

## Introduction

The purpose of this guide is to provide a detailed, step-by-step explanation of how to scrape data from a website using Scrapy.

## Scope

This guide covers the setup process for Scrapy, including installation instructions, and provides a walkthrough of how to start the scraping process.

## Assumptions

Before proceeding, please make sure you meet the following requirements:

-   You have some experience with Python and the command line.
-   You have a command-line interface available to interact with your computer.
-   You have a text editor installed to work with plain text files.
-   You have Python version 3.7 installed.
-   You have the pip package manager for Python installed.

## Libraries and Installations

Before running the headless scripts, ensure that the following components are present on your server:

-   64-bit server


```
$ lscpu | head -n 2
Architecture: x86_64
CPU op-mode(s): 32-bit, 64-bit
``` 

-   Python 3

rubyCopy code

```
$ python3 -V
Python 3.8.2
``` 

-   pip3


```
$ pip3 -V
pip 20.1.1 from /home/roiarthurb/.local/lib/python3.8/site-packages/pip (python 3.8)
``` 

### Step 1: Create a Virtual Environment and Activate it

To create a virtual environment, run the following command in the terminal:


```
pip install virtualenv
``` 

This command installs the virtualenv package. Once installed, create a virtual environment using the following command:



```
virtualenv <environment_name>
``` 

For Linux, activate the virtual environment using:


```
source <environment_name>/bin/activate
```
 

For Windows, use:


```
<environment_name>\Scripts\activate
``` 

### Step 2: Install Project Dependencies

Navigate to the base directory of the project and install the dependencies using the following command:

Copy code

```
pip install -r requirements.txt
``` 

## Scraping the Data

Before scraping the data, you need to configure the MySQL database to store the scraped information. Follow these steps:

1.  Create a new database in MySQL.
2.  Update the configuration in the `.env` file located in the base directory of the project. Make the following changes:


```
DB_NAME="<database_name>"
DB_USER="<username>"
DB_PASSWORD="<password>"
DB_HOST="<hostname>"  # e.g., 'localhost'
DB_PORT=<port_number>  # e.g., 3360
``` 

To start scraping, run the following command:


```
scrapy crawl netvendeur
``` 

If the script terminates for any reason and you want to resume scraping from the termination point, use the following command:

```
scraping run "scrapy crawl netvendeur -s JOBDIR=crawls/netvendeur-1"
``` 

Please note that you should replace `<environment_name>`, `<database_name>`, `<username>`, `<password>`, `<hostname>`, and `<port_number>` with the appropriate values according to your setup.

For more information and detailed instructions, please refer to the documentation.