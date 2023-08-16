

![Rock, Paper, Scissors image](documentation/rps.jpg)


[Link to live project](https://rock-paper-scissorspp3-18513f12fbb5.herokuapp.com/)

## Table of Content

1. [Introduction](#introduction)
2. [Existing Features](#existing-features)
3. [Features to implement in future](#features-to-implement-in-future)
4. [Colour](#colour)
5. [Google Sheet Access](#google-sheet-access)
6. [Flow-Chart](#flow-chart)
7. [Testing](#testing)
8. [Bug ](#bug)
9. [Deployment ](#deployment)
10. [Technologies Used ](#Technologies-Used)
11. [Credits ](#credits)
12. [Acknowledgments ](#acknowledgments)



## Introduction
- Rock, Paper, Scissors is a game that can solve any conflict and is quite possibly the best sport in the entire world!
- It is a 2 player game and can be played anywhere.
- The rules are simple: Rock beats Scissors, Scissors beats Paper, and Paper beats Rock.
- The users score is saved on Google sheets, which can later be recalled for display and total score for there last 10 games is also added together. 

## Existing Features

### Welcome Message
- When a new game starts the welcome message is displayed.
- The user is welcomed with an emoji of a Rock, Paper and Scissors.

### Username Input
- The user is asked for a user name, this user name will be used to save there score.

### Menu selection
- After the user name is entered the menu selection appears.
- From the menu area -
    * The user can play the game.
    * Read the instructions.
    * Read their score. 
    * Change user name.
    * Exit the game

<details>
<summary>Features Image</summary>

![Welcome Message](documentation/welcome.png)
![Menu](documentation/menuoption.png)

</details>

### Game Area
- In the game area the user is asked to enter either R for Rock, P for Paper, and S for Scissors.
- If another letter or number is entered as error will appear, That input isn't valid. Please enter 'R' OR 'P' OR 'S'!".
- The computers choice is random, and the computers result is checked againest the user choice.
- The users and computers choice is displayed to the user and if it's a Win, Loae or Draw.
- The user has a choice to continue to play for ever, or they can exit the game or go back to the menu.
- It is at this point the number of wins and total games played are saved to google sheets for later display.

![Game Play](documentation/gameplay.png)

### New User Name
- A new player can enter there username without exiting the game and starting the game again.

### Score Area
- This area shows the current user there score.
- The user can see there results for the last 10 games that they have played.
- The user can search for other users by there user name.
<details>
<summary>Features Image</summary>

![score Play](documentation/scorearea.png)   
![score Play](documentation/scorearea1.png)
</details>

[Back to contents](#introduction)

## Features to implement in future
- Count the number of times the user entered P, R or S, to see if the user has a preference.
- Create a leader board for the top 10 highest scores.
- Create a login, so that there is only 1 person per username.


## Colour
- Colour for the win result and lose result text was selected, as it is more initially noticeable to see a Green colour for a win and a Red colour for a lose. 
- A draw result was left as white.

    ![Font Colour](documentation/colours.png)


## Google Sheet Access 

Googlesheet is used to store, usernames and game won along with total games played.
![Google Sheet](documentation/googlesheet.png)


## Flow-Chart
A flow chart for this game created with the help of Lucid [Web-Site](https://lucid.app/documents#/dashboard)

![Flow Chart](documentation/flowchart.png)

## Testing
- Testing has been implemented throughout the entire project mainly debugging through running the program in the CodeAnyWhere terminal.
- Tested in both CodeAnyWhere terminal and Heroku terminal.
- CI Python linter/Syntax checker [pep8ci](https://pep8ci.herokuapp.com/)

- A space was enter in as a user name, and played the game, and in goolge sheets (image below) there was no username in the 1st column. A score and total games was entered, but no user name. Code was added to stop spaces only being entered as a username. If spaces are only entered an error message appears.

    ![Space entered Username](documentation/testnouser.png)

- An error message will appear on the user input just after the intro title if only spaces are entered. 
- An error message will also appear on the user input if a new user is entered from the main menu if only spaces are entered.
- A username was enter and then setected 1 on main menu to play game and when the 1st option comes up, to enter R,P,S or leave the area, I entered M to go back to the menu and a Zero score was recorded. Code was entered to stop this from happening.
    ![Didn't enter R,P,S](documentation/nogameplay.png)

- A New user was entered and didn't play the game, the score was checked and an error "The user doesn't exist". So a line was added to say "If this is your first time here please play the game to view a score.".
- There was feedback to say that it would be nice if there was a date added when the game was played. Code was added to implement this.
- Code was addded to limit the lenght of usernames to 12 or less characters. This stops users having usernames that could be 50-100 characters in length.

![13 characters error](documentation/charlenerrorgif.gif)

- A test check was completed.

    ![Testcheck](documentation/testcheck.png)


## Bug
- There was a bug when saving the results to google sheets. In the image below it can be seen that the results for Tom's first go is in Row 2 and the results for wins and total games are also in row 2. When the game is played again the results for win and total games don't go into the next row they went into Column A. The same happened for the 3rd and 4ft and so on. 

    ![Sheets Bug](documentation/bug.png)

- I selected H for the win column and tested the code then and this worked, I then tested column's C,D,E,F,G to append the results and the same issue would happen. 
- The work around for this was to append the results for wins in column H and for total games into column T.
    ![Sheets Bug](documentation/bug1.png)


[Back to contents](#introduction)

## Deployment
- Heroku was used to deploy the website.
- It is assumed here that GitHub accounts are already set up.
- In CodeAnyWhere a \n needs to added at the end of the text inside the input method, for a software quirk.
- To create our list of requirements, we  use the following command in the terminal.
- The requirements.txt file was populated using the command "pip3 freeze > requirements.txt' in CodeAnyWhere.
- Commit them and push the changes up to Github from CodeAnyWhere.
- Create our account with [Heroku](https://id.heroku.com/login).
- Heroku will then send you a confirmation email, click the linl and login.
- In Heroku clicking on the button 'New' and select 'Create New App'.
- The app name on Heroku has to be unique.
- Then you can select your region.
- Then click “Create app”.
- Go the settings tabs.
- Then config vars and upload the creds.json file.
- In the field for key, enter CREDS.
- Copy the entire creds.json file, and paste it into the value field here.
- Click “Add”.
- Next step is to Add buildpack”. The 1st buildpack is Python, then click “Save changes”.
- The other buildpack  we need is called node.js click Save again.
- The order for the buildpacks is important also so its Python on top, and node.js underneath.
- Project settings are completed, Next step is in the deploy section.
- Github was selectted, for deployment method.
- Connect to GitHut, and search for the Github repository name. Then click connect.
- From here you can select Automatic or Manual deploy.
- Automatic deploy will re-deploy the application every time the project is "git pushed".
- If you select "Manual deploy", after the project has been built, click "view" to see the deployed page.
- “App was successfully deployed” message will appear, and a link to the deployed app.
- Click on the link to test for error's.
 


## Technologies Used
- [Google Spreadsheets](https://docs.google.com/spreadsheets/create)
- [CodeAnyWhere](https://app.codeanywhere.com/#state=474b05ff-3f92-4cdc-8752-6dd304bf7e9a&session_state=e2fb87e6-7eb8-4b49-8a19-ca79f4ba4e72&code=afcf483d-faf2-41da-977d-ef9081c5a331.e2fb87e6-7eb8-4b49-8a19-ca79f4ba4e72.7f856e59-e31e-4c70-a17f-bc37660636b2)
- [GitHub](https://github.com/)
- [Heroku](https://www.heroku.com/about)
- [LucidCharts](https://www.lucidchart.com/pages/)

[Back to contents](#introduction)



## Credits
- Google Developers site was a great tool for research to access and edit Google sheet: [Google Developers](https://developers.google.com/sheets/api/guides/create).
- To create font colour and background colour: [Python font colour](https://www.lihaoyi.com/post/BuildyourownCommandLinewithANSIescapecodes.html).
- To transfer variables from one function to another: [stackoverflow global statement](https://stackoverflow.com/questions/10506973/can-not-increment-global-variable-from-function-in-python).
- Code for Dates: [w3schools](https://www.w3schools.com/python/python_datetime.asp).
- Code to clear screen: [geeksforgeek](https://www.geeksforgeeks.org/clear-screen-python/).
- Code to type slow: [stackoverflow](https://stackoverflow.com/questions/4099422/printing-slowly-simulate-typing).
- In the display and calculating of the scores, inspiration and research was found at the following sites,
    - [strip() Method](https://www.w3schools.com/python/ref_string_strip.asp),
    - [Last Records](https://www.geeksforgeeks.org/get-last-n-records-of-a-pandas-dataframe/),
    - [Print in Python](https://stackoverflow.com/questions/69472788/how-to-get-columns-titles-from-googlesheets-to-print-in-python),
    - [Search Row for Data](https://stackoverflow.com/questions/63033616/python-google-sheets-check-in-which-row-the-data-is).
    - [Search Column for Data](https://stackoverflow.com/questions/61599272/google-sheets-search-column-for-value-using-python).
    - [Iterate Rows for Data](https://stackoverflow.com/questions/74547789/iterate-over-pandas-rows-and-using-shift-in-if-statement).
    - [Sum Count Results](https://stackoverflow.com/questions/75196357/sum-last-n-rows-of-df-count-results-into-one-row).
    - [Google Sheets Guide](https://understandingdata.com/posts/the-comprehensive-guide-to-google-sheets-with-python/).
    - [Read/Write Google Sheets Guide](https://aryanirani123.medium.com/read-and-write-data-in-google-sheets-using-python-and-the-google-sheets-api-6e206a242f20).
    - [Appending Rows Google Sheets Guide](https://stackoverflow.com/questions/63775455/python-gspread-api-not-appending-rows-if-multiple-functions-called).
    - [Invalid user name for spaces/nothong](https://stackoverflow.com/questions/51764409/how-to-prevent-user-from-inputting-spaces-nothing-in-python).
    - [Getting the sum from an array](https://stackoverflow.com/questions/65100023/how-do-i-get-the-sum-of-a-row-in-an-array)


## Acknowledgments

- Thank you to my mentor Elaine Roche who helped with points and tips and gave me very good advice and feedback on how to plan and execute this project and who provided me with lots of pointers for my project.
