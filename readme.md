# Automatic Git Project Launcher

## Before we start

**🗘** ➞ Still working on it.  
**✔** ➞ Working well.  
**😼** ➞ Pay attention.

The following project was tested in DeepinOS and its code base was created in MacOS. Maybe (or not) some modifications are necessary, in cases of SOs other than those two.

**😼** **Warn0:** Some commands used directly in the terminal work well on Linux and MacOS systems but maybe not on Windows.

✔ **Warn1:** In the Chrome browser, you need to install the [chromeDriver](http://chromedriver.chromium.org/downloads) so that everything works fine.  
✔ **Warn2:** In the Firefox browser, you need to install the [geckodriver](https://github.com/mozilla/geckodriver) so that everything works fine.

🗘 **Warn3:** Still not working perfectly well, There are still **inconsistencies**.

**🝰 New update 1:** This project has been **successfully tested** on **WINDOWS**, step settings below:
>  
* Download [Chromedriver](https://chromedriver.storage.googleapis.com/index.html?path=75.0.3770.8/). (At the time of this update the current version is at 75.0.*)
* Unzip and save to a new folder. ( `C:\Webdrivers` preferably ).
* Set the path folder in the system environment variables. ( `path` preferably ).

That said, let's go.

## What I Do

I'm a small project that automates the creation of repositories on both the computer and the GitHub platform.

## Requirements

* Python 3.x
  * Selenium (available on pip)
    * webdriver (module to be used)
  * Sys (native)
  * Os (native)

* Git
  * GitHub Account
    * SSH (preferably)

## How to install

* Clone this project:
  > `git clone https://github.com/silv4b/initproject.git`

* Change the `path` in `funcions.py` to your repository path.
## How to use

* Into the folder, run:
  > `python3 makerepo.py <arg1> <arg2> <arg3> <action>`

  Where:
  * arg1 = github username
  * arg2 = github password
  * arg3 = github repository name
  * action:
    * `-c` to create bouth folder and repository
    * `-d` to delete bouth folder and repository

Base code for this project in: [ProjectInitializationAutomation](https://github.com/KalleHallden/ProjectInitializationAutomation).

Made by: [KalleHallden](https://github.com/KalleHallden).

`Made with ❤.`
