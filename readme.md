# Automatic Project Launcher

## Before we start

> 🗘 ➞ Still working on it. 
>
> ✔ ➞ Working.

The following project was tested in DeepinOS and its code base was created in MacOS. Maybe (or not) some modifications are necessary, in cases of SOs other than those two.

🗘 **Warn1:** In the Chrome browser, you need to install the [ChromeDriver](http://chromedriver.chromium.org/downloads) so that everything works fine.

🗘 **Warn2:** In the Firefox browser, you need to install the [geckodriver](https://github.com/mozilla/geckodriver) so that everything works fine.

🗘 **Warn3:** Still not working perfectly well, There are still **inconsistencies**.

> **🝰 New update:** This project has been **successfully tested** on **windows**, step settings below:
>  
> * Download [Chromedriver](https://chromedriver.storage.googleapis.com/index.html?path=75.0.3770.8/). (At the time of this update the current version is at 75.0.*)
> * Unzip and save to a new folder. ( `C:\Webdrivers` preferably ).
> * Set the path folder in the system environment variables. ( `path` preferably ).

That said, let's go.

## What I Do

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

Base code for this project in: [ProjectInitializationAutomation](https://github.com/KalleHallden/ProjectInitializationAutomation).

Made by: [KalleHallden](https://github.com/KalleHallden).

`Made with ❤.`
