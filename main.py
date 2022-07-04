# BloxSnipe - a limited snipe bot for Roblox
    # @author:      Oasis#5999
    # @version:     1.2
#
import urllib.request
import re
import time
import webbrowser

# INSTRUCTIONS
    # Step 1: Make sure you have Python installed on your computer so that you can run this program. If you don't, go to python.org and download it
    # Step 2: Modify the configuration variables below as needed
    # Step 3: Save the file and run the program, and wait. It will open the page of the item as soon as someone sells it for your target price. 
    
# NOTES
    # This does not do anything with your Roblox cookie or your personal data. This script is completely safe to use.
    # This script will not automatically buy the limited for you. It will only take you to the page, so buy it as soon as the page loads.
    # The more items you try to scan at the same time, the longer it will take (for obvious reasons)

# Configuration variables - DO NOT TOUCH OTHER PARTS OF THE SCRIPT UNLESS YOU KNOW WHAT YOU'RE DOING
        # links - put the links of the items you want to snipe. Surround the link with "" and put a comma at the end
        # range - set it to the max price you waant to snipe an item for
        # cooldown - put the number of seconds you want to refresh the pages, 2-3 is recommended
links = [
    "https://www.roblox.com/catalog/6803395856/Gucci-Guitar-Case",
    "https://www.roblox.com/catalog/6803398976/Gucci-Geometric-Bag",
    "https://www.roblox.com/catalog/9731852643/Brown-Gucci-Blondie-Bag-1-0",
    "https://www.roblox.com/catalog/9731869178/Brown-Gucci-Blondie-Bag-3-0"
]
range = 183
cooldown = 1

# Function that gets the data of the limited pages, and writes them into placeholder .txt files
def getItems(links):
    length = len(links)
    for link in links:
        x = urllib.request.urlopen(link)
        y = x.read()
        z = y.decode("utf8")
        file = open("placeholders/placeholder" + str((links.index(link) + 1)) + ".txt", "w")
        file.write(z)
        file.close()

# Function that returns the lowest prices of the items from the webpages
def getPrices(links):
    prices = []
    for link in links:
        file = open("placeholders/placeholder" + str((links.index(link) + 1)) + ".txt", "r")
        filetext = file.read()
        file.close()
        matches = re.findall('<span class="text-robux-lg wait-for-i18n-format-render ">(.*)</span>', filetext)
        prices.append(int(matches[0].replace(',', '')))
    return prices

# Function that returns whether the prices of the items match the target range or not
def checkPrices(prices, range):
    conditionals = []
    for price in prices:
        conditionals.append(price <= range)
    return conditionals
    
def main(links, range, cooldown): 
    starting = True
    counter = 0

    print('BloxSnipe succesfully started.')
  
    while starting:
        getItems(links)
        prices = getPrices(links)
        conditions = checkPrices(prices, range)
        for condition in conditions:
            if condition:
                print("Target price found!")
                webbrowser.open(links[conditions.index(condition)])
                exit()
            else:
                pass
        time.sleep(cooldown)
        counter += 1
        print('Refreshing page... (Iteration #' + str(counter) + ')')
        
# done
main(links, range, cooldown)