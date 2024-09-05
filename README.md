# CS50-Finance

## Introduction
This is one of the assignments provided in CS50x - Introduction to Computer Science.

The goal of the exercise is to:

* Implement a website that allow user to "buy" and "sell" stock and the following functions:
* Complete the implementation of register, to enble the user to register for an account via a form.
* Complete the implementation of quote, to enable the user to look up a stock’s current price.
* Complete the implementation of buy, to enable the user to buy stocks.
* Complete the implementation of index, to display an HTML table summarizing, for current logged in user, which stocks the user owns, the numbers of shares owned, the current price of each stock, and the total value of each holding (i.e., shares times price). Also display the user’s current cash balance along with a grand total (i.e., stocks’ total value plus cash).
* Complete the implementation of sell, to enable the user to sell shares of a stock (that he or she owns).
* Complete the implementation of history, to display an HTML table summarizing all of a user’s transactions ever, listing row by row each and every buy and every sell.

Apart from the function required and the built in function provided in this exercise, I  added some of my own functions to the website:

* Allow user to change their password
* Allow the user to add more cash

If you want more information click [here](https://cs50.harvard.edu/x/2023/psets/9/finance/)

## Built With
* HTML for website strcuture
* Flask for backend development
* Bootstrap for design
* [IEX API](https://iexcloud.io/) to get the stocks values in real time
* sqlite3 for storing users information (username and hashed password) and the transaction record (bought or sold)

## Website
Every user after registered will have $10000 by default

* Login Page:
![Login Page](/CS50%20finance%20Screenshot/LogIn.png)

* Register Page:
![Register Page](/CS50%20finance%20Screenshot/Register.png)

* Index Page:
  This is the homepage of the website which also contains the History table of the user.
![Index Page](/CS50%20finance%20Screenshot/Index.png)

* Quote Page (Input the stock symbol for checking the stock info): 
![Quote Page](/CS50%20finance%20Screenshot/Quote.png)

* Quoted Page (The inputted stock symbol is displayed):
![Quoted Page](/CS50%20finance%20Screenshot/Quoted.png)

* Buy page (Input the stock symbol and number of shares to buy):
![Buy Page](/CS50%20finance%20Screenshot/Buy.png)

* Bought Page (The bought stock is displayed at the history):
![Bought Page](/CS50%20finance%20Screenshot/Bought.png)

* Sell Page (Input the stock that you have bought in the drop-down list and input the number of shares to sell): 
![Sell Page](/CS50%20finance%20Screenshot/Sell.png)

* Sold Page (The sold stock is displayed at the history):
![Sold Page](/CS50%20finance%20Screenshot/Sold.png)

* History page (Show all your action on the page such as sell, buy): 
![History Page](/CS50%20finance%20Screenshot/History.png)

* Add Cash Page: 
![Add Page](/CS50%20finance%20Screenshot/Add.png)

* Added Cash Page:
![Added Page](/CS50%20finance%20Screenshot/Added.png)

* Change Password (Allow user to change their password but cannot input the new password same as current password): 
![Change Password](/CS50%20finance%20Screenshot/ChangePassword.png)

## Reference
* Bootstrap
* W3School
* Stack Overflow
# CX50x-Finance
