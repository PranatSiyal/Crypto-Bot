# Crypto-Bot
## Overview
This script is used for automated trading of Bitcoin using Selenium and a web driver. It interacts with a web page displaying Bitcoin prices and performs buying and selling actions based on certain conditions. 
## Modules imported
**1.** Time
**2.** Selenium web driver
**3.** Chrome web driver
## How it works
The script prompts the user to enter the amount they would like to invest (in a wallet variable).<br/>
It finds the Bitcoin element on the page using an XPath expression and extracts the initial price.<br/>
The script defines the buy() and sell() functions for executing the buying and selling actions, respectively. These functions update the wallet and workingWallet variables accordingly.<br/>
The script enters an infinite loop and continuously checks the current price of Bitcoin on the page. <br/>
## Algorithm 
**1.** If the current price is different from the initial user price, it performs the following actions:
**2.** Prints the current rate, current price, price change, and the original price.
**3.** If the current price is higher than the original price, it checks if it is also higher than the initial user price. If so, it calculates the income, updates the wallet, recalculates the amount of Bitcoin purchased, and updates the startUserPrice. It then continues to the next iteration of the loop.
**4.** If the current price is lower than the original price, it checks if it is also lower than the initial user price. If so, it enters a while loop that waits for 7 seconds (using time.time()) and then executes the "OG Lowering" block. This block calculates the income, updates the wallet, recalculates the amount of Bitcoin purchased, updates the startUserPrice and ogPrice, and breaks out of the while loop.
**5.** Finally, it updates the startUserPrice to the current user price.
