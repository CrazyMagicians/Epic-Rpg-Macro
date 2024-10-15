import discord #main module
import asyncio #for bot developement
import time #time related functions
#PAID version /import numpy #captcha image data reading
#PAID version /import cv2 #captcha
import pprint #for session data viewing
import captcha_bypasser #PAID version /bypassing epic guard
import options_resolver #user options parser
import ctypes #for alert box
from random import randint #for random intervals

#options data
userOptions = options_resolver.importData()

#global constants
userToken = userOptions["user_token"]
userMentionText = userOptions["user_mention_text"]
channelID = int(userOptions["channel_id"])
randomIntervals = userOptions["random_interval"] == "true"

#global variables
lowPriorityQueue = []
highPriorityQueue = []
jailed = False
paused = False
sessionData = {"command_data":{"hunt":0,"adventure":0,"farm":0,"training":0,"work":0,"quest":0},"stats_data":{"coins":0,"xp":0,"levels":0},"loot_data":{"mob_drops":{"wolf skin":0,"zombie eye":0,"unicorn horn":0,"mermaid hair":0,"chip":0,"dragon scale":0},"lootbox_drops":{"common":0,"uncommon":0,"rare":0,"epic":0,"edgy":0,"omega":0,"godly":0},"work_drops":{"banana":0,"apple":0,"ruby":0,"normie fish":0,"golden fish":0,"epic fish":0,"wooden log":0,"epic log":0,"super log":0,"mega log":0,"hyper log":0,"ultra log":0},"farm_drops":{"carrot":0,"potato":0,"bread":0}},"misc":{"cards":0,"guard_events":0,"personal_events":0}}

#extra functionality
userSeedFinished = False
runtimeErrors = []
userID = int(userMentionText.replace("<","").replace(">","").replace("@",""))
startTime = time.time()

def extractData(data,dataType): #not used currently; extract data from embeds/stats
    pass

def alertBox(title,message):
    ctypes.windll.user32.MessageBoxW(0, message, title, 0x00001000)

async def rdCheck(msg):
        global userOptions,highPriorityQueue,lowPriorityQueue,userSeedFinished
        if "hunt" in msg:
            sessionData["command_data"]["hunt"] += 1
            lowPriorityQueue.append("rpg hunt")
        if "adventure" in msg:
            sessionData["command_data"]["adventure"] += 1
            lowPriorityQueue.append("rpg heal")
            if userOptions["life_boost_before_adv"] != "none":
                lowPriorityQueue.append("rpg withdraw all")
                lowPriorityQueue.append("rpg buy life boost "+userOptions["life_boost_before_adv"])
                lowPriorityQueue.append("rpg deposit all")
            if userOptions["adventure_area"] != "none":
                lowPriorityQueue.append("rpg area "+userOptions["adventure_area"])
                lowPriorityQueue.append("rpg adv")
                lowPriorityQueue.append("rpg area "+userOptions["current_area"])
            else:
                lowPriorityQueue.append("rpg adv")
        if "daily" in msg:
            lowPriorityQueue.append("rpg daily")
        if "weekly" in msg:
            lowPriorityQueue.append("rpg weekly")
        if "lootbox" in msg:
            if userOptions["lootbox_type"] != "none":
                lowPriorityQueue.append("rpg withdraw 420666")
                lowPriorityQueue.append("rpg buy "+userOptions["lootbox_type"])
                lowPriorityQueue.append("rpg deposit all")
        if "training" in msg:
            sessionData["command_data"]["training"] += 1
            lowPriorityQueue.append("rpg tr")
        if "quest" in msg: #To be done
            pass
            #lowPriorityQueue.append("rpg quest")
        if "farm" in msg:
            sessionData["command_data"]["farm"] += 1
            if userOptions["seed"] != "none" and not userSeedFinished:
                lowPriorityQueue.append("rpg farm "+userOptions["seed"])
            else:
                lowPriorityQueue.append("rpg farm")                                   
        if "vote" in msg:
            pass #ultra low work
        if "horse breed" in msg:
            pass #ultra low work
        if "duel" in msg:
            pass #ultra low work
        if "arena" in msg:
            pass #ultra low work
        if "miniboss" in msg:
            pass #ultra low work
        if "chop" in msg:
            sessionData["command_data"]["work"] += 1
            lowPriorityQueue.append("rpg "+userOptions["work_command"])

async def responseResolver(message):
    global lowPriorityQueue,highPriorityQueue,sessionData,jailed,paused,userToken,userID,userMentionText,channelID,userOptions,runtimeErrors,userSeedFinished,alertBox,rdCheck
    msg = message.content.lower()
    if message.author.id == userID:
        if "sb session t" == msg:
            lowPriorityQueue.append("```"+pprint.pformat(sessionData)+"```")
            return
        elif "sb session" == msg:
            print(pprint.pformat(sessionData))
            return
        elif "sb uptime t" == msg:
            highPriorityQueue.append(str(time.time()-startTime)+" seconds")
            return
        elif "sb uptime" == msg:
            print(str(time.time()-startTime)+" seconds")
            return
        elif "sb pause" == msg:
            if not paused:
                paused = True
            else:
                highPriorityQueue.append("worker is already paused")
            return
        elif "sb start" == msg:
            if paused:
                paused = False
            else:
                highPriorityQueue.append("worker is already running")
            return

    elif message.author.id == 1213487623688167494: #navi lite user id
        if userMentionText in msg:
            _temp = message.content.replace(userMentionText,"")
            if "heal" in _temp:
                highPriorityQueue.append("rpg heal")
                return
            if "YES" in _temp:
                highPriorityQueue.append("YES")
            elif "NO" in _temp:
                highPriorityQueue.append("NO")
            elif "1" in _temp:
                highPriorityQueue.append("1")
            elif "2" in _temp:
                highPriorityQueue.append("2")
            elif "3" in _temp:
                highPriorityQueue.append("3")                                
            elif "4" in _temp:
                highPriorityQueue.append("4")
            elif "5" in _temp:
                highPriorityQueue.append("5")                
            elif "6" in _temp:
                highPriorityQueue.append("6")
            elif "A" in _temp:
                highPriorityQueue.append("a")
            elif "B" in _temp:
                highPriorityQueue.append("b")
            elif "E" in _temp:
                highPriorityQueue.append("e")
            elif "L" in _temp:
                highPriorityQueue.append("l")
            elif "N" in _temp:
                highPriorityQueue.append("n")
            elif "P" in _temp:
                highPriorityQueue.append("p")
            else:
                runtimeErrors.append(time.strftime("%Y/%m/%d %H:%M:%S - unexcpected helper response "+_temp)) 
        if "hunt" in msg:
            sessionData["command_data"]["hunt"] += 1
            lowPriorityQueue.append("rpg hunt")
        elif "adventure" in msg:
            sessionData["command_data"]["adventure"] += 1
            lowPriorityQueue.append("rpg heal")
            if userOptions["life_boost_before_adv"] != "none":
                lowPriorityQueue.append("rpg withdraw all")
                lowPriorityQueue.append("rpg buy life boost "+userOptions["life_boost_before_adv"])
                lowPriorityQueue.append("rpg deposit all")
            if userOptions["adventure_area"] != "none":
                lowPriorityQueue.append("rpg area "+userOptions["adventure_area"])
                lowPriorityQueue.append("rpg adv")
                lowPriorityQueue.append("rpg area "+userOptions["current_area"])
            else:
                lowPriorityQueue.append("rpg adv")
        elif "daily" in msg:
            lowPriorityQueue.append("rpg daily")
        elif "weekly" in msg:
            lowPriorityQueue.append("rpg weekly")
        elif "lootbox" in msg:
            if userOptions["lootbox_type"] != "none":
                lowPriorityQueue.append("rpg withdraw 420666")
                lowPriorityQueue.append("rpg buy "+userOptions["lootbox_type"])
                lowPriorityQueue.append("rpg deposit all")
        elif "training" in msg:
            sessionData["command_data"]["training"] += 1
            lowPriorityQueue.append("rpg tr")
        elif "quest" in msg: #To be done
            pass
            #lowPriorityQueue.append("rpg quest")
        elif "farm" in msg:
            sessionData["command_data"]["farm"] += 1
            if userOptions["seed"] != "none" and not userSeedFinished:
                lowPriorityQueue.append("rpg farm "+userOptions["seed"])
            else:
                lowPriorityQueue.append("rpg farm")                                   
        elif "vote" in msg:
            pass #ultra low work
        elif "horse breed" in msg:
            pass #ultra low work
        elif "duel" in msg:
            pass #ultra low work
        elif "arena" in msg:
            pass #ultra low work
        elif "miniboss" in msg:
            pass #ultra low work
        elif "is back from adventure" in msg:
            pass #low work
        elif "heal" in msg:
            lowPriorityQueue.append("rpg heal")
        elif "work" in msg:
            sessionData["command_data"]["work"] += 1
            lowPriorityQueue.append("rpg "+userOptions["work_command"])
    
    if message.author.id == 555955826880413696: #Epic Rpg user id
        if len(message.embeds) != 0:
            embedDict = message.embeds[0].to_dict()
            if "hunt a defenseless monster" in str(embedDict):
                sessionData["misc"]["personal_events"] += 1
                highPriorityQueue.append(userOptions["zombie_horde_event_response"])
                highPriorityQueue.append("rpg area "+userOptions["current_area"])
            elif "matter how much you look around" in str(embedDict):
                sessionData["misc"]["personal_events"] += 1
                highPriorityQueue.append("move")
                highPriorityQueue.append("fight")
            elif "You planted a seed, but for some reason it's not growing up" in str(embedDict):
                sessionData["misc"]["personal_events"] += 1
                highPriorityQueue.append("fight")
            elif "You have encountered a mysterious man" in str(embedDict):
                sessionData["misc"]["personal_events"] += 1
                highPriorityQueue.append("cry")
            elif "God accidentally dropped" in str(embedDict) or "I have a special trade today" in str(embedDict):
                sessionData["misc"]["personal_events"] += 1
                lowPriorityQueue.append(embedDict["fields"][0]["value"].splitlines()[1].replace("**","").lower())
            elif "Check the long version of this command with " in str(embedDict):
                await rdCheck(str(embedDict["fields"]))
        else:
            if "we have to check you are actually playing" in msg:
                sessionData["misc"]["guard_events"] += 1
                jailed = True
                alertBox("Epic Rpg Macro","EPIC GUARD ALERT!")
            elif "everything seems fine" in msg:
                jailed = False
            elif "seed to farm, buy one" in msg:
                lowPriorityQueue.append("rpg withdraw all")
                lowPriorityQueue.append("rpg buy seed 10")
                lowPriorityQueue.append("rpg farm")
            elif "you do not have this type of seed" in msg:
                userSeedFinished = True
                lowPriorityQueue.append("rpg farm")
            elif userOptions["seed"] + "seed" in msg:
                if userSeedFinished:
                    userSeedFinished = False
            elif "found and killed a" in msg:
                msgLines = msg.splitlines()
                sessionData["stats_data"]["coins"] += int(msgLines[1].split(" ")[1].replace(",",""))
                sessionData["stats_data"]["xp"] += int(msgLines[1].split(" ")[4].replace(",",""))
                for drop in sessionData["loot_data"]["mob_drops"]:
                    if drop in msg:
                        sessionData["loot_data"]["mob_drops"][drop] += 1
                for lootbox in sessionData["loot_data"]["lootbox_drops"]:
                    if lootbox+" lootbox" in msg:
                        sessionData["loot_data"]["lootbox_drops"][lootbox] += 1
                if "card" in msg:
                    sessionData["misc"]["cards"] += 1
            elif "seed in the ground" in msg:
                for item in sessionData["loot_data"]["farm_drops"]:
                    if item in msg:
                        sessionData["loot_data"]["farm_drops"][item] += [int(word) for word in msg.splitlines()[1].split() if word.isdigit()][0]
                if "leveled up" in msg:
                    sessionData["stats_data"]["xp"] += [int(word) for word in msg.replace(",","").splitlines()[-2].split() if word.isdigit()][0]
                else:
                    sessionData["stats_data"]["xp"] += [int(word) for word in msg.replace(",","").splitlines()[-1].split() if word.isdigit()][0]
            elif "well done" in msg:
                sessionData["stats_data"]["xp"] += [int(word) for word in msg.replace(",","").splitlines()[1].split() if word.isdigit()][0]
            else:
                if not "training" in msg:
                    for item in sessionData["loot_data"]["work_drops"]:
                        if item in msg:
                            numOfDrops = [int(word) for word in msg.split() if word.isdigit()]
                            if len(numOfDrops) == 1:
                                sessionData["loot_data"]["work_drops"][item] += numOfDrops[0]
            if "leveled up" in msg:
                sessionData["stats_data"]["levels"] += 1

class DiscordClient(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
 
    async def setup_hook(self):
        #create the background task and run it in the background
        self.bg_task = self.loop.create_task(self.my_background_task())

    async def on_ready(self):
        print(f'Logged in as {self.user} (ID: {self.user.id})')
        print('----------------------------------------------')
    
    async def on_message(self,message):
        if message.channel.id == channelID:
            await responseResolver(message)
    
    async def my_background_task(self):
        global jailed,lowPriorityQueue,highPriorityQueue,paused
        lastCheck = int(time.time()) - 300
        await self.wait_until_ready()
        channel = self.get_channel(channelID)

        while not self.is_closed():
            if not paused:
                if len(highPriorityQueue) != 0 and not jailed:
                    if highPriorityQueue[0] != "":
                        await channel.send(highPriorityQueue[0])
                    print(time.strftime("%H:%M:%S "+highPriorityQueue[0]+" done"))
                    del highPriorityQueue[0]
                elif len(lowPriorityQueue) != 0 and not jailed:
                    await channel.send(lowPriorityQueue[0])
                    print(time.strftime("%H:%M:%S "+lowPriorityQueue[0]+" done"))
                    del lowPriorityQueue[0]
                
                if int(time.time()) - lastCheck >= 300 and not jailed:
                    lastCheck = int(time.time())
                    lowPriorityQueue.append("rpg rd")
                    print(time.strftime("%H:%M:%S rpg rd done"))
    
                if randomIntervals:
                    await asyncio.sleep(1+randint(0,3))
                else:
                    await asyncio.sleep(1)

UserBot = DiscordClient()
UserBot.run(userToken)
