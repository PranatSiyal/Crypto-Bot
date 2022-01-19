import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.dailyfx.com/bitcoin")

wallet = float(input("How much would you like to invest: "))
ogAmount = wallet
workingWallet = wallet

time.sleep(5)

btc = driver.find_element_by_xpath('//*[@id="dfx-instrumentPageBar-BITCOIN"]/div[1]/div/div[1]/div[2]/div[1]')
startPrice = float(btc.get_attribute('data-value'))
btcPurchased = wallet/startPrice
startUserPrice = btcPurchased*startPrice
ogPrice = startUserPrice
print(startUserPrice)


def buy():
    global wallet
    global workingWallet
    global ogAmount

    if wallet >= ogAmount:
        workingWallet = ogAmount
        wallet = wallet - ogAmount
    elif wallet < ogAmount:
        ogAmount = wallet
        workingWallet = wallet
        wallet = 0

def sell():
    global wallet
    global workingWallet

    wallet += workingWallet
    workingWallet = 0


while True:

    currentPrice = float(btc.get_attribute('data-value'))
    currentUserPrice = btcPurchased*currentPrice

    if currentUserPrice != startUserPrice:

        print("Current Rate: ", currentPrice)
        print("Current Price: ", currentUserPrice)
        print("Price Change: ", currentUserPrice-startUserPrice)
        print("OG Price: ", ogPrice)

        if currentUserPrice > ogPrice:
            if currentUserPrice > startUserPrice:
                income = btcPurchased*currentPrice
                wallet += (income-workingWallet)
                btcPurchased = ogAmount / currentPrice
                startUserPrice = btcPurchased * currentPrice
                print("Wallet: ", wallet)
                continue

        elif currentUserPrice < ogPrice:

            if currentUserPrice < startUserPrice:

                now = time.time()
                future = now + 7

                while True:
                    if time.time() > future:
                        print("Entered OG Lowering")
                        income = btcPurchased * currentPrice
                        wallet += (income - workingWallet)
                        print("Wallet: ", wallet)
                        btcPurchased = ogAmount / startPrice
                        startUserPrice = btcPurchased * currentPrice
                        ogPrice = currentUserPrice
                        break
                else:
                    continue


        startUserPrice = currentUserPrice
