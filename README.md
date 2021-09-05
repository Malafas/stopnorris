# STOPNORRIS
Essay on Acceptance and Integration Testing with RobotFramework.  
Test specification presented in Docs\stopnorris.pptx

Run all tests: 
```
robot -d Logs Tests\
```

Run only one test suite: 
```
robot -d Logs Tests\FE\stopwatch.robot
robot -d Logs Tests\BE\chucknorris.robot
```

## Dependencies

- [Python](https://www.python.org/downloads/)
- [Chrome](https://www.google.com/intl/en-US/chrome/)
- [ChromeDriver](https://chromedriver.chromium.org/downloads) (compatible with installed Chrome version)

### Libraries

- _Automation Tool_  
[RobotFramework](https://github.com/robotframework/robotframework)

- _Web_  
[SeleniumLibrary](https://github.com/robotframework/SeleniumLibrary)  
[BrowserLibrary](https://github.com/MarketSquare/robotframework-browser)

- _Webservices_  
[RequestsLibrary](https://github.com/MarketSquare/robotframework-requests)  
[JSONLibrary](https://github.com/robotframework-thailand/robotframework-jsonlibrary)
