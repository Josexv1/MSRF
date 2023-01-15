```
v0.4b Release Notes:
- Persistent Dark Mode
	- When Dark Mode is toggled, it will be updated in the configuration.yaml file, which loads every time the program is run. 
- Long press on the "Last Exec" cell for the account to force execute only that account
- Error Reporting
	- Errors that cause fatal errors in a module (critical errors) will be logged using the Error Reporting module. 
	- This will create a zipfile in the ./errors directory in the same location as the executable. 
	- the errors directory will contain all errors thrown by the application. 
	- Error Information
		- Account data (Same account data used for earning points, this information does not contain any account credentials, only account information like: point count, available promotions, etc.) 
		- Browser screenshot at the time of the error. This may include the account name, and potentially the account email. If you plan on sharing this (such as in a Github issue), you may want to cover any personal information
		- A traceback. This is the exception raised by python. 
		- The HTML page at the time of the error. This helps in determining exactly why an error happened, but this file will have personal information, such as your email address and name. You may not want to include this when sharing this with other people. If you are familiar with HTML structure, you can find and remove that personal information before sharing. 
		- the url that the exception occured on.
	- This module is primarily made to help me find and address problems with the scrapers, but also to give you a simple way to report errors when they happen. 


I currently do not have a full test suite going for this project, and its very likely that there are problems within this update. If it is not working for you, please try the previous version (v0.3b) for the time being.
```


# Microsoft Rewards Famer (MSRF)
![GitHub release (latest SemVer)](https://img.shields.io/github/v/release/thearyadev/msrf?color=gree&style=for-the-badge)
![Flet](https://img.shields.io/badge/FLET-cock?style=for-the-badge&logo=flutter)

This project is a automated farmer for Microsoft Rewards. It will log into given accounts and complete surveys, quizzes, and conduct bing searches. The farmer will automatically schedule runs to farm points for each account. More details on what exactly it is doing is outlined below.

**Usage of this application may get your Microsoft account permanently banned. I take no responsibility for any actions made on your account.**

This project is a rewrite of ["Microsoft-Rewards-Farmer"](https://github.com/charlesbel/Microsoft-Rewards-Farmer). The goal of this project is to move towards a documented and test driven code base. The entire code base has been restructured, and over 90% of it is re-written. Some components from the original project still exist within this one.

## Demo
![Light Mode Demo](demo/demo-light-mode.png)
![Dark Mode Demo](demo/demo-dark-mode.png)
![Add Account Demo](demo/demo-add-account.png)

## Installation

Download the zip file from the Github releases for this project. It will include everything needed to run this program, including: 
  - The main executable
  - Chrome
  - Chromedriver Binary

Run the executable to start the program.

*Note: The bundled Chrome and Chromedriver binaries will likely be outdated. This is to prevent breaking changes in Chrome and Chromedriver from affecting the program. For every major release, both bundled binaries will be updated. When using this program, you accept the risk of using unsecure software that may compromise the overall security of your system.

## Development

This project was developed in Python 3.10.8 and has **not** been tested with any other version of python. 

Install all python dependencies using the `requirements.txt` file found in the root of this project. 

```bash
python -m pip install -r requirements.txt
```

Selenium requires a Chromedriver binary and Chrome installation. This is automatically detected assuming you have correctly configured both on your machine.
This behavior can be changed temporarily for development. Browser initialization is done in the file `./util/browser/browser_setup.py`. Here you can configure custom chromedriver and chrome binary paths.

## Information
### Yields
I haven't recorded any numbers for how well this works. I do know that not all quizzes will be completed, sometimes the daily set won't fully complete, and you may not get the streak for that day. 
If the quiz types change, or new data is present that I have not designed this farmer around, they will not be completed. 

That being said, from my testing and observation, a level 2 microsoft rewards account seems to get 150-250 points per day. 
This number can be increased by manually ensuring that the daily set is completed, so that you gain streak bonuses, and that any additional quizzes or polls that the bot is unable to do are completed. 

`07/01/2023` - Some surveys don't work. Fixes maybe soon :)

### Bans
I've been developing this for about a month now. I haven't been banned on the 4 accounts that I have been testing on. After redeeming excess of $25 worth of rewards, and continuously running this daily, not one account has been banned. 

Microsoft may change their methods of banning at any time. Use accounts that you do not value, and redeem your reward as soon as you have enough points. 

I'm also not currently aware of any IP bans or rate limits for a single IP when it comes to point collection and reward redemption, as I haven't encountered this in my testing. If this concerns you, i advise you use a VPN. If this becomes a major problem I may incorporate proxy servers into this project.

### Breaking Changes
Microsoft can make changes at any time. They may break the farmer. I've designed this so that whichever component does not work, is simply skipped, outputting a critical error then continuing to the next task. 
When breaking changes are known, I will work towards fixing them. 

### Not working? 
The most common problem I've seen in testing is login problems. The prompt may say something like invalid credentials, which may be the case. 
Microsoft sometimes has other steps to the login, which I have not considered. 

If an account is continuously failing to log in, you can enter "debugging mode" by clicking the bug icon at the bottom control panel. This will show the Chrome browser that is being used by the program, and will allow you to see what is preventing the login. 

For example: 
- Invalid credentials
  - You will be able to see the program attempt to log in, and view the full error message sent by microsoft authentication
- Additional Login steps
  - "Please verify your security information". This will require you to click a button to confirm, which will block the program from running on your account.
  
If other errors are occurring, you can use debugging mode to determine why those issues are arising.

### Updates
When the program gets updated, it will reveal an update prompt. It is important to keep this app up to date, to prevent your account from getting banned. 

This project currently has no update/installer. It is just a zipped folder with an executable in it. To copy your accounts over, copy the `accounts.sqlite` file to the directory that contains the updated files. 

### Bugs & Feature Requests

Open an issue on this Github repository. Outline the problem to the best of your ability. 
Be sure to include a screenshot of the log window to show any reported errors, if any. 

- Error Reporting
	- Errors that cause fatal errors in a module (critical errors) will be logged using the Error Reporting module. 
	- This will create a zipfile in the ./errors directory in the same location as the executable. 
	- the errors directory will contain all errors thrown by the application. 
	- Error Information
		- Account data (Same account data used for earning points, this information does not contain any account credentials, only account information like: point count, available promotions, etc.) 
		- Browser screenshot at the time of the error. This may include the account name, and potentially the account email. If you plan on sharing this (such as in a Github issue), you may want to cover any personal information
		- A traceback. This is the exception raised by python. 
		- The HTML page at the time of the error. This helps in determining exactly why an error happened, but this file will have personal information, such as your email address and name. You may not want to include this when sharing this with other people. If you are familiar with HTML structure, you can find and remove that personal information before sharing. 
		- the url that the exception occurred on.
	- This module is primarily made to help me find and address problems with the scrapers, but also to give you a simple way to report errors when they happen. 

Unzip your error report, and remove any personal information from it. You can then include it in the Github issue. Without an error report, you may not get help, as it is very hard to determine what the cause of a bug in this program is. 

Please use the Github issue template for all bugs and feature requests. 

## Development Roadmap / Known Issues
- Tests
    - daily set
        - daily set contains 3 items
    - error reporting
- load accounts button to allow the user to select an `accounts.sqlite` file from a previous version/save of MSRF
- final preparations for v1.0 release.
- purge errors once the errors directory contains more than 50 entries. 
- complete documentation of all components and modules
- fix a bug where 12 points worth of PC searches are not completed. 
- fix question # count. Some start at 0 instead of 1.
- fix common problem where dashboard data fails to load due to the page not being loaded.
- suppress exceptions in waitUntilVisible where possible
- add detailed error descriptions for error report. ie: what is the farmer trying to do
- add full error trace
- add error count display in GUI.
- add an additional data field to the error report so each individual error report can include some extra data where applicable
  - for example: the task it was trying to complete at the time of the error
  - locals
  - globals
  - etc. 
- have custom logging return a log object, so that the log dump can be displayed on the screen, but also sent to the error log.
- Test usage with Chrome Portable to allow for smaller package size. 
  - The total unzipped size of this program is ~700mb. Chrome is like 70% of that. Chrome Portable is significantly smaller than that.
  - Currently unsure if it works with existing Chrome/Chromedriver applications, will be looking into this soon.
- Installer for the app, so it can be added to registered programs on the system
- Auto updater script
- Server Mode; linux support; web-ui enhancements


## Contributing

There are no contributing guidelines (for now). 


## 🚀 About Me
I'm a developer. Actively learning and looking for new and interesting opportunities. Send me a message: aryan@aryankothari.dev


## License

[Apache-2.0](/LICENSE)

