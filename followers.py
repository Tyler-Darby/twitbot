from TwitterFollowBot import TwitterBot

bot = TwitterBot()

print("""
    Created by @tylerdarby_ (Github: @PHPApple)
    Wrapper created by: https://github.com/rhiever/TwitterFollowBot
 _____        _ _   _            ______    _ _               ______       _   
|_   _|      (_) | | |           |  ___|  | | |              | ___ \     | |  
  | |_      ___| |_| |_ ___ _ __ | |_ ___ | | | _____      __| |_/ / ___ | |_ 
  | \ \ /\ / / | __| __/ _ \ '__||  _/ _ \| | |/ _ \ \ /\ / /| ___ \/ _ \| __|
  | |\ V  V /| | |_| ||  __/ |   | || (_) | | | (_) \ V  V / | |_/ / (_) | |_ 
  \_/ \_/\_/ |_|\__|\__\___|_|   \_| \___/|_|_|\___/ \_/\_/  \____/ \___/ \__|
    I'm not liable for your misuse of the Twitter API. 
    Don't blame me if you get banned for using this. 

  """)
config = {
  "debug": True
}

def debugMessage(msg):
  if config["debug"]:
    print(msg)

def statusMessage(msg):
  print("[!] " + msg)

def promptMessage(msg):
  return input("[+] " + msg + "\n -")

def followKeyword():
  # This follows the keywords that you choose. Works with hashtags. 
  statusMessage("Action: Follow keyword.")
  keywords = promptMessage("Type the keywords you would like to follow based upon, then type the number of tweets to follow.\n For example: cute funny lol 1000")
  keywords = keywords.split(" ")
  num = len(keywords) - 1
  int(num)
  for x in range(0, num):
    statusMessage("Currently on keyword: " + keywords[x])
    bot.auto_follow(keywords[x], count=keywords[num])
  statusMessage("All done! Exiting the bot now. Re-run the bot to utilize more functions.")

# Actions dictionary. Used to call our functions.
actions = {
  '1': followKeyword
}

# Script Init.
statusMessage("Welcome to TwitterBot. Please select one of the actions from the list below. Type the number of the action you choose.")
print("""
[1] Follow keyword
[2] Sync followers (Use with caution)
[3] Unfollow who isn't following you (Exceptions: List)
[4] Mute all people you followed (Exceptions: List)
  """)

action = promptMessage("Type the number of the action you would like to use. Example: 1");

if actions[action]:
  actions[action]()
else:
  statusMessage("That is not an action. Please try another action.")
