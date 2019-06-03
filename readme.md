# Initializer Project Automation

## Before we start

The following project was tested in DeepinOS and its code base was created in MacOS. Maybe (or not) some modifications are necessary, in cases of SOs other than those two.

That said, let's go.

## What I Do.

I'm a small project that automates the creation of repositories on both the computer and the GitHub platform.

## Requirements

- Python 3.x
  - Selenium (available on pip)
    - webdriver (module to be used)
  - Sys (native)
  - Os (native)

## How to install

- Clone this project:
  > `git clone https://github.com/silv4b/initproject.git`

## How to use

(create)

- Into the folder, run:
  > `Python3 onfolder.py <arg1> <arg2> <arg3>`

(remove)

- Into the folder, run:
  > `Python3 remove.py <arg1> <arg2> <arg3>`

  Where:
  - arg1 = github username
  - arg2 = github password
  - arg3 = github repository name

Ps1: In the chrome browser, you may need to install the [ChromeDriver](http://chromedriver.chromium.org/downloads) so that everything works fine.

Ps2: Still not working perfectly well, the repositories are created, but the stop conditions have not yet been implemented.

Base code for this project in: [ProjectInitializationAutomation](https://github.com/KalleHallden/ProjectInitializationAutomation).

Made by: [KalleHallden](https://github.com/KalleHallden).

`Made with ❤.`
