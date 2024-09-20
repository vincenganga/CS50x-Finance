# CS50x-Finance

## Introduction
This is one of the assignments provided in CS50x - Introduction to Computer Science.

The goal of the exercise is to:

* Implement a website that allows users to "buy" and "sell" stock with the following functions:
* Complete the implementation of a registration system, enabling users to register for an account.
* Complete the implementation of a quote feature, allowing users to look up the current price of a stock.
* Complete the implementation of a buying system, enabling users to buy stocks.
* Complete the implementation of an index page to display an HTML table summarizing which stocks the logged-in user owns, how many shares, the current price of each stock, and the total value of each holding (i.e., shares times price). Also display the user's current cash balance and a grand total (i.e., the total value of stocks plus cash).
* Complete the implementation of a selling system to allow users to sell shares of stocks they own.
* Complete the implementation of a history page that displays an HTML table summarizing all of a user’s transactions, showing each buy and sell action.

In addition to the required functions, I added some extra features to the website:

* Allow users to change their password.
* Allow users to add more cash to their account.

For more information, click [here](https://cs50.harvard.edu/x/2023/psets/9/finance/).

## Built With
* HTML for website structure.
* Flask for backend development.
* Bootstrap for design.
* [IEX API](https://iexcloud.io/) to fetch real-time stock prices.
* sqlite3 for storing user information (username, hashed passwords) and transaction records (bought or sold stocks).

## Website
After registering, each user will have a default cash balance of $10,000.

* **Login Page**:
![Login Page](/CS50%20finance%20Screenshot/LogIn.png)

* **Register Page**:
![Register Page](/CS50%20finance%20Screenshot/Register.png)

* **Index Page**:
  This is the homepage of the website, which also contains the history of the user's transactions.
![Index Page](/CS50%20finance%20Screenshot/Index.png)

* **Quote Page** (Enter the stock symbol to check the stock info): 
![Quote Page](/CS50%20finance%20Screenshot/Quote.png)

* **Quoted Page** (Displays the info of the entered stock symbol):
![Quoted Page](/CS50%20finance%20Screenshot/Quoted.png)

* **Buy Page** (Enter the stock symbol and the number of shares to buy):
![Buy Page](/CS50%20finance%20Screenshot/Buy.png)

* **Bought Page** (The bought stock is displayed in the user's history):
![Bought Page](/CS50%20finance%20Screenshot/Bought.png)

* **Sell Page** (Select the stock you own from the drop-down list and enter the number of shares to sell): 
![Sell Page](/CS50%20finance%20Screenshot/Sell.png)

* **Sold Page** (The sold stock is displayed in the user's history):
![Sold Page](/CS50%20finance%20Screenshot/Sold.png)

* **History Page** (Shows all user actions, such as buy and sell transactions): 
![History Page](/CS50%20finance%20Screenshot/History.png)

* **Add Cash Page**: 
![Add Page](/CS50%20finance%20Screenshot/Add.png)

* **Added Cash Page**:
![Added Page](/CS50%20finance%20Screenshot/Added.png)

* **Change Password** (Allows users to change their password, but the new password cannot be the same as the current one): 
![Change Password](/CS50%20finance%20Screenshot/ChangePassword.png)

## References
* Bootstrap
* W3School
* Stack Overflow
