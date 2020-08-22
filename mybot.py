""" If you don't have library then you have to install first.
here are some library that is used in this program
pip install pyttsx3	for speak
pip install numpy	for array"""

import pyttsx3    #for speak() function
import os         #for system() function
import numpy	#for array()
os.system('cls')
print("\n\n\t\t>>>--------|PROJECT ON SOLVE THE USE CASE THEORY|--------<<<\n\n")
print("\t\t_____________________________________________________________")
print("\t\t\t\t\t>>>|My Chat Bot|<<<")
print("\t\t_____________________________________________________________")
print("\n\t\tWelcome,i am your assistant,\n\t\thow can i help?")
pyttsx3.speak("Welcome.....,i am your assistant.....,how can i help?")
os.system("color f1")                                                                              
while True:
    
  #To get input from keyboard
  print("\t\t\t\t\t\t", end='');
  getinput = input()
  p=getinput.lower()
  #print(p)
  #os.system(p)
  
  #Chrome
  if ("chrome" in p) or ("chorme" in p) or ("crome" in p) or ("cohrme" in p) or ("corome" in p):
    os.system("color 90") 
    print("\n\t\tOpening Chrome browser")
    pyttsx3.speak("Opening Chrome browser")
    os.system("start chrome")

  #don't
  elif ("don't" in p) or ("no" in p) or ("not" in p) or ("never" in p) or (("do" in p) and ("not" in p)) or ("nope" in p) or ("nah" in p):
    os.system("color a0") 
    print("\n\t\tOk")
    pyttsx3.speak("Ok")
    
  #Translate
  elif ("translate" in p) or ("traslate" in p) or ("translation" in p):
    os.system("color a0")
    print("\n\t\tOpening Google translate")
    pyttsx3.speak("Opening Google translate")
    os.system("start chrome https://translate.google.co.in/")

  #google
  elif ("google" in p) or ("googlesearch" in p) or ("search" in p) or ("google.com" in p):
    os.system("color b0")
    print("\n\t\tOpening Google")
    pyttsx3.speak("Opening Google")
    os.system("start chrome google.com")

  #Drive
  elif ("drive" in p):
    os.system("color c0")
    print("\n\t\tOpening Google drive")
    pyttsx3.speak("Opening Google drive")
    os.system("start chrome https://drive.google.com/drive/u/0/my-drive")

  #News
  elif ("news" in p):
    os.system("color d0")
    print("\n\t\tOpening News")
    pyttsx3.speak("Opening News")
    os.system("start chrome https://news.google.com/")

  #whatsapp web
  elif (("whatsapp" in p) and ("web" in p)) or ("whatsappweb" in p) or (("whatsapp" in p) and (("chrome" in p) or ("browser" in p))):
    os.system("color f0")
    print("\n\t\tOpening WhatsApp web")
    pyttsx3.speak("Opening whatsapp web")
    os.system("start chrome web.whatsapp.com")
  
  #website
  elif ("website" in p) or ("site" in p) or ("webpage" in p) or ("web" in p):
    os.system("color e0")
    print("\n\t\tEnter website name with their\n\t\tdomain")
    pyttsx3.speak("Enter website name with their domain")
    print("\t\t\t\t\t\t", end='');
    link=input()
    print("\n\t\tOpening "+link)
    pyttsx3.speak("Opening"+link)
    os.system("start chrome "+link)
      
  #whatsapp
  elif ("whatsapp" in p) or ("whatsap" in p) or ("whatsup" in p) or ("watsapp" in p) or ("watsp" in p):
    os.system("color f0")
    print("\n\t\tOpening WhatsApp")
    pyttsx3.speak("Opening whatsapp")
    os.system("start Whatsapp")
  
  #youtube
  elif ("youtube" in p) or ("utube" in p) or ("youtub" in p) or ("youthub" in p) or ("youtube.com" in p):
    os.system("color b1")
    print("\n\t\tOpening YouTube")
    pyttsx3.speak("Opening youtube")
    os.system("start chrome youtube.com")
    
  #facebook
  elif ("facebook" in p) or ("facebok" in p) or ("facebk" in p) or ("facebhook" in p) or ("facebuk" in p) or ("facebook.com" in p):
    os.system("color e1")
    print("\n\t\tOpening Facebook")
    pyttsx3.speak("Opening facebook")
    os.system("start chrome facebook.com")
    
  #instagram
  elif ("instagram" in p) or ("insta" in p) or ("istagram" in p) or ("intagram" in p) or ("intagram.com" in p):
    os.system("color f1")
    print("\n\t\tOpening Instagram")
    pyttsx3.speak("Opening instagram")
    os.system("start chrome instagram.com")
    
  #Gmail
  elif ("gmail" in p) or ("mail" in p) or ("googlemail" in p) or ("email" in p):
    os.system("color b2")
    print("\n\t\tOpening Gmail")
    pyttsx3.speak("Opening gmail")
    os.system("start chrome gmail.com")

  #twitter
  elif ("twitter" in p) or ("twiter" in p) or ("tviter" in p) or ("twiter" in p) or ("twitter.com" in p):
    os.system("color e2")
    print("\n\t\tOpening twitter")
    pyttsx3.speak("Opening twitter")
    os.system("start chrome twitter.com")

  #linkedin
  elif ("linkedin" in p) or ("linked" in p) or ("likedin" in p) or ("linkedn" in p) or ("linkeden" in p) or ("linkedin.com" in p):
    os.system("color f2")
    print("\n\t\tOpening Linkedin")
    pyttsx3.speak("Opening linkedin")
    os.system("start chrome linkedin.com")
    
  #music
  elif ("song" in p) or ("songs" in p) or ("music" in p) or ("gaana" in p) or ("sing" in p) or ("gaana.com" in p):
    os.system("color e3")
    print("\n\t\tPlaying music")
    pyttsx3.speak("Playing music")
    os.system("start chrome gaana.com")

  #amazon
  elif ("amazon" in p) or ("amazon.in" in p):
    os.system("color e3")
    print("\n\t\tOpening Amazon.in")
    pyttsx3.speak("Opening Amazon.in")
    os.system("start chrome Amazon.in")

  #flipkart
  elif ("flipkart" in p) or ("flipkart.com" in p) or ("flipcart.com" in p):
    os.system("color e3")
    print("\n\t\tOpening Flipkart.com")
    pyttsx3.speak("Opening Flipkart.com")
    os.system("start chrome Flipkart.com")

  #food reciepes
  elif ("food" in p) or ("reciepe" in p) or ("recipe" in p) or ("recepe" in p) or ("recipi" in p):
    os.system("color f3")
    print("\n\t\tFood reciepes for you")
    pyttsx3.speak("Food reciepes for you")
    os.system("start chrome https://www.bbcgoodfood.com/recipes/collection/easy-recipes")

  #unit converter
  elif (("unit" in p) and (("converter" in p) or ("convert" in p))) or ("measurement" in p):
    os.system("color b4")
    print("\n\t\tOpening Unit converter")
    pyttsx3.speak("Opening Unit converter")
    os.system("start chrome https://www.unitconverters.net/")

  #calculator
  elif ("calculator" in p) or ("calculate" in p) or ("calculation" in p) or ("calsi" in p) or ("add" in p) or ("subtract" in p) or ("devide" in p) or ("multiply" in p):
    os.system("color e4")
    print("\n\t\tOpening Calculator")
    pyttsx3.speak("Opening Calculator")
    os.system("calc")

  #camera
  elif ("camera" in p) or ("cam" in p) or ("record" in p) or ("click" in p) or ("shoot" in p) or ("cheese" in p) or ("webcam" in p) or ("photo" in p) or ("foto" in p) or ("photos" in p) or ("images" in p) or ("pic" in p):
    os.system("color f4")
    print("\n\t\tOpening Camera")
    pyttsx3.speak("Opening Camera")
    os.system("start microsoft.windows.camera:")

  #paint
  elif ("paint" in p) or ("drawing" in p) or ("art" in p) or ("sketch" in p) or ("painting" in p):
    os.system("color f4")
    print("\n\t\tOpening Paint")
    pyttsx3.speak("Opening Paint")
    os.system("mspaint")

  #cmd
  elif ("cmd" in p) or ("commandprompt" in p) or (("command" in p) and ("prompt" in p)):
    os.system("color e4")
    print("\n\t\tOpening Command Prompt")
    pyttsx3.speak("Opening Command Prompt")
    os.system("start")

  #restart
  elif ("restart" in p) or (("re" in p) and ("start" in p)) or (("re" in p) and ("boot" in p)):
    os.system("color e4")
    print("\n\t\tDo you want to Restart this pc")
    pyttsx3.speak("Do you want to restart this pc")
    print("\t\t\t\t\t\t", end='');
    y=input()
    if ("yes" in y) or ("y" in y) or ("ok" in y):
      print("\n\t\tRestart the pc")
      pyttsx3.speak("Restart pc")
      os.system("shutdown /r")
    elif ("no" in y) or ("n" in y) or ("cancel" in y) or ("deny" in y):
      print("\n\t\tOk")
      pyttsx3.speak("ok")

  #shutdown
  elif ("shutdown" in p) or (("shut" in p) and ("down" in p)) or (("shutting" in p) and ("down" in p)):
    os.system("color e4")
    print("\n\t\tDo you want to shutdown this pc")
    pyttsx3.speak("Do you want to shutdown this pc")
    print("\t\t\t\t\t\t", end='');
    y=input()
    if ("yes" in y) or ("y" in y) or ("ok" in y):
      print("\n\t\tShutdown the pc")
      pyttsx3.speak("shutdown pc")
      os.system("shutdown /s")
    elif ("no" in y) or ("n" in y) or ("cancel" in y) or ("deny" in y):
      print("\n\t\tOk")
      pyttsx3.speak("ok")

  #logoff
  elif ("logoff" in p) or (("log" in p) and ("off" in p)) or ("sleep" in p):
    os.system("color e4")
    print("\n\t\tDo you want to logoff this pc")
    pyttsx3.speak("Do you want to logoff this pc")
    print("\t\t\t\t\t\t", end='');
    y=input()
    if ("yes" in y) or ("y" in y) or ("ok" in y):
      print("\n\t\tlogoff the pc")
      pyttsx3.speak("logoff pc")
      os.system("shutdown /l")
    elif ("no" in y) or ("n" in y) or ("cancel" in y) or ("deny" in y):
      print("\n\t\tOk")
      pyttsx3.speak("ok")

  #control panel
  elif (("control" in p) and ("panel" in p)) or (("control" in p) and ("panle" in p)) or ("panel" in p) or ("controlpanel" in p) or ("controlpanle" in p):
    os.system("color b5")
    print("\n\t\tOpening Control Panel")
    pyttsx3.speak("Opening Control panel")
    os.system("control panel")

  #windows settings
  elif (("pc" in p) and ("setting" in p)) or ("settings" in p) or ("setting" in p):
    os.system("color b5")
    print("\n\t\tOpening Settings")
    pyttsx3.speak("Opening Control settings")
    os.system("start ms-settings:")

  #file explorer
  elif ("file" in p) or ("explorer" in p) or (("this" in p) and ("pc" in p)) or ("thispc" in p):
    os.system("color e5")
    print("\n\t\tOpening File explorer")
    pyttsx3.speak("Opening file explorer")
    os.system("explorer")


  #shopping
  elif ("shopping" in p) or ("purchase" in p) or ("buy" in p) or ("shop" in p) or ("shoping" in p) or (("online" in p) and ("shopping" in p)) or ("amazon" in p) or ("flipkart" in p):
    os.system("color f5")
    print("\n\t\tOpening Google shopping")
    pyttsx3.speak("Opening google shopping")
    os.system("start chrome https://www.google.com/shopping?nord=1")

  #wikipedia
  elif ("wikipedia" in p) or ("wiki" in p) or ("wikipedia.com" in p) or ("wikipedia.org" in p):
    os.system("color f6")
    print("\n\t\tOpening Wikipedia")
    pyttsx3.speak("Opening wikipedia")
    os.system("start chrome https://www.wikipedia.org/")

  #yahoo
  elif ("yahoo" in p) or ("yahoo.com" in p):
    os.system("color d7")
    print("\n\t\tOpening yahoo.com")
    pyttsx3.speak("Opening yahoo.com")
    os.system("start chrome https://in.yahoo.com/?p=us")

  #fun
  elif ("fun" in p) or ("enjoy" in p):
    os.system("color e8")
    print("\n\t\tHere are some things you \n\t\tshould try. You can say: \n\t\t'Give me a complement' or \n\t\t'Tell me a joke'")
    pyttsx3.speak("Here are some things you should try.... You can say:..'Give me a compliment'.. or 'Tell me a joke'")
    
  #Complement
  elif ("complement" in p) or ("compliment" in p):
    os.system("color f8")
    print("\n\t\tYou're as distinctive as the\n\t\tEiffel Tower")
    pyttsx3.speak("You're as distinctive as the Eiffel Tower")
   
  #joke
  elif ("joke" in p):
    os.system("color e9")
    print("\n\t\tWhat do you call a rose that\n\t\twants to go to the moon?\n\n\t\tGulab ja moon")
    pyttsx3.speak("What do you call a rose that wants to go to the moon?...........Gulab jaa moon")

  #one more
  elif (("one" in p) and ("more" in p)) or ("onemore" in p):
    os.system("color f9")
    print("\n\t\tWhat one more")
    pyttsx3.speak("What one more")

  #Games
  elif ("play" in p) or ("games" in p) or ("game" in p) or ("shooting" in p) or ("car" in p):
    os.system("color f9")
    pyttsx3.speak("I have a few option for that. Which one would you like to try?")
    print("\n\t\tMadalin stunt cars 2")
    print("\n\t\trussian car driver")
    print("\n\t\tPuppy blast")
    print("\n\t\tDowntown 1930s mafia")
    print("\t\t\t\t\t\t", end='');
    gname=input()
    if ("stunt" in gname) and (("car" in gname) or ("cars" in gname)):
      #Madalin stunt cars 2
      os.system("start chrome https://www.crazygames.com/game/madalin-stunt-cars-2")
    elif ("russian" in gname) or ("driver" in gname):
      #russian car driver
      os.system("start chrome https://www.crazygames.com/game/russian-car-driver-zil-130")
    elif ("puppy" in gname) or ("blast" in gname):
      #Puppy blast
      os.system("start chrome https://www.crazygames.com/game/puppy-blast")
    elif ("downtown" in gname) or ("mafia" in gname):
      #Downtown 1930s mafia
      os.system("start chrome https://www.crazygames.com/game/downtown-1930s-mafia")
    elif ("exit" in gname):
      os.system("color 07") 
      print("\t\t_____________________________________________________________")
      print("\t\t\t\t  Made by : Ashish Kumar\n\t\t\t  Contact: ashishchoudhary9084@gmail.com")
      print("\t\t_____________________________________________________________")
      break
    else:
      os.system("start chrome crazygames.com")
    
  #notepad
  elif ("notepad" in p) or ("editor" in p) or (("text" in p) and ("editor" in p)) or ("texteditor" in p) or ("notpad" in p):
    os.system("color a0")
    print("\n\t\tOpening Notepad")
    pyttsx3.speak("Opening notepad")  
    os.system("start notepad")
    
  #wmplayer
  elif (("player" in p) and ("media" in p)) or ("media" in p) or ("multimedia" in p) or ("videoplayer" in p) or ("video" in p):
    os.system("color b0")
    print("\n\t\tOpening Window Media Player")
    pyttsx3.speak("Opening Window media player")	
    os.system("start wmplayer")
    
  #vlc
  elif ("player" in p) or ("vlc" in p):
    os.system("color c0")
    print("\n\t\tOpening VLC Player")
    pyttsx3.speak("Opening vlc player")	
    os.system("start vlc")
    
  #msword	
  elif ("word" in p) or (("microsoft" in p) and ("word" in p)) or ("msword" in p) or ("docx" in p):
    os.system("color d0")
    print("\n\t\tOpening Microsoft word")
    pyttsx3.speak("Opening Word")
    os.system("start winword")
    
  #excel
  elif ("excel" in p) or ("msexcel" in p) or ("xls" in p):
    os.system("color e0")
    print("\n\t\tOpening Microsoft Excel")
    pyttsx3.speak("Opening excel")
    os.system("start excel")
    
  #ms access
  elif ("access" in p) or ("msaccess" in p) or ("acess" in p):
    os.system("color f0")
    print("\n\t\tOpening Microsoft Access")
    pyttsx3.speak("Opening microsoft access")
    os.system("start msaccess")
    
  #power point
  elif ("powerpoint" in p) or (("power" in p) and ("point" in p)) or ("ppt" in p):
    os.system("color b1")
    print("\n\t\tOpening PowerPoint")
    pyttsx3.speak("Opening power point")
    os.system("start powerpnt")
    
  #opera
  elif ("opera" in p) or ("opra" in p):
    os.system("color e1")
    print("\n\t\tOpening Opera browser")
    pyttsx3.speak("Opening opera browser")
    os.system("start opera")

  #how to exit	
  elif (("how" in p) and (("exit" in p) or ("quit" in p) or ("bye" in p) or ("goodbye" in p) or ("back" in p))):
    print("\n\t\tSay exit")
    pyttsx3.speak("Say exit")

  #exit	
  elif ("exit" in p) or ("quit" in p) or ("bye" in p) or ("goodbye" in p) or ("back" in p):
    os.system("color 07") 
    print("\t\t_____________________________________________________________")
    print("\t\t\t\t  Made by : Ashish Kumar\n\t\t\t  Contact: ashishchoudhary9084@gmail.com")
    print("\t\t_____________________________________________________________")
    break
  
  #help
  elif ("help" in p) or ("task" in p) or (("what" in p) and ("you" in p) and ("do" in p)):
    os.system("color f1")
    print("\n\t\tYou can say 'Run chrome'or \n\t\t'play music' or Menu")
    pyttsx3.speak("try saying... Run chrome, play music or menu")
  #menu
  elif ("menu" in p) or ("list" in p) or ("program" in p) or ("tasks" in p) or (("what" in p) and ("program" in p)) or (("what" in p) and ("website" in p)):
    os.system("color e3")
    print("\t\t_____________________________________________________________")
    print("\n\t\t\t\t\t    MENU")
    print("\t\t_____________________________________________________________")
    pyttsx3.speak("opening menu")
    print("\t\tProgram\t\tWebsites\tGames\t\t\tOther\n")
    print("\t\tChrome\t\tGoogle.com\tMadalin Stunt car\tMusic")
    print("\t\tNotepad\t\tWikipedia.org\tRussian Car driver\tSettings")
    print("\t\tVLC\t\tGaana.com\tPuppy blast\t\tUnit Converter")
    print("\t\tMedia player\tYoutube.com\tDowntown Mafia\t\tNews")
    print("\t\tOpera\t\tFacebook.com\t\t\t\tTranslate")
    print("\t\tMS Word\t\tInstagram.com\t\t\t\tDrive")
    print("\t\tMS Excel\tYahoo.com\t\t\t\tGmail")
    print("\t\tMS access\ttwitter.com\t\t\t\tShopping")
    print("\t\tPowerpoint\tlinkedin.com\t\t\t\tGoogle")
    print("\t\tWhatsapp\tWhatsapp Web\t\t\t\tFun")
    print("\t\tInstagram\tAmazon\t\t\t\t\tDate")
    print("\t\tFacebook\tFlipkart\t\t\t\tTime")
    print("\t\tYoutube\t\tOther Websites\t\t\t\tFile Explorer")
    print("\t\tTwitter\t\t\t\t\t\t\tRun")
    print("\t\tLinkedin\t\t\t\t\t\tControl Panel")
    print("\t\tCamera\t\t\t\t\t\t\tSettings")
    print("\t\tCalculator\t\t\t\t\t\tShutdown")
    print("\t\tCommand Prompt\t\t\t\t\t\tRestart")
    print("\t\tPaint\t\t\t\t\t\t\tLog Off")
    print("\t\t_____________________________________________________________\n")
    print("\n\t\tWhat do you want?")

  #Date and time
  elif ("date" in p) and ("time" in p):
    os.system("color f3")
    from datetime import datetime
    # datetime object containing current date and time
    now = datetime.now()
    #print("now =", now)
    # dd/mm/YY H:M:S
    dt_string = now.strftime("%B %d, %Y %H:%M:%S")
    print("\n\t\tdate and time\n\t\t",dt_string)
    pyttsx3.speak(dt_string)
    
  #Time
  elif ("time" in p):
    os.system("color b4")
    from datetime import datetime
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("\n\t\tCurrent Time=",current_time)
    pyttsx3.speak(current_time)
    
  #Date
  elif ("date" in p):
    os.system("color e2")
    from datetime import date
    today = date.today()
    d2 = today.strftime("%B %d, %Y")
    print("\n\t\tDate =", d2)
    pyttsx3.speak(d2)
  
  #Thank you  
  elif (("thank" in p) and ("you" in p)) or ("thankyou" in p) or ("thanku" in p):
    os.system("color f2")
    print("\n\t\tMy pleasure :)")
    pyttsx3.speak("my pleasure")
    print("\n\t\tDo you want something else \n\t\t(yes/no)")
    pyttsx3.speak("Do you want something else")
    print("\t\t\t\t\t\t", end='');
    yesno=input()
    if ("yes" in yesno) or ("y" in yesno):
      print("\n\t\tWhat do you want")
      pyttsx3.speak("what do you want")
    else:
      os.system("color 07") 
      print("\t\t_____________________________________________________________")
      print("\t\t\t\t  Made by : Ashish Kumar\n\t\t\t  Contact: ashishchoudhary9084@gmail.com")
      print("\t\t_____________________________________________________________")
      break
  elif ("about" in p) and ("you" in p):
    os.system("color f2")
    print("\n\t\tI'm your Assistant.I can \n\t\thelp you find answer, get \n\t\tthings done, and have fun")
    pyttsx3.speak("I'm your Assistant....I can help you find answer,.... get things done,... and have fun ")
  
  elif ("about" in p):
    os.system("color f1")
    print("\n\t\tWhat you want to know?")
    pyttsx3.speak("What you want to know?")  
  
  elif ("ok" in p):
    print()  
  
  elif ("my" in p) and ("name" in p):
    os.system("color e8")
    print("\n\t\tTell me, What is your name")
    pyttsx3.speak("Tell me,.. What is your name") 
    print("\t\t\t\t\t\t", end='');
    name=input()
    print("\n\t\tYour name is "+name)
    pyttsx3.speak("Your name is "+name)

  elif (("your" in p) and ("name" in p)) or (("who" in p) and ("you" in p)):
    os.system("color d7")
    print("\n\t\tI am your assistant")
    pyttsx3.speak("i am your assistant") 

  elif ("call" in p) and ("you" in p):
    os.system("color f6")
    print("\n\t\tYou can call me your Assistant")
    pyttsx3.speak("You can call me your Assistant") 

  elif ("sweet" in p) or ("beautiful" in p) or ("gorgeous" in p) or ("awesome" in p) or ("good" in p) or ("handsome" in p) or ("baby" in p):
    os.system("color f5")
    print("\n\t\tThank you :), You too")
    pyttsx3.speak("Thank you :), You too")     

  elif ("what" in p) and ("you" in p):
    os.system("color e5")
    print("\n\t\tI am here to help")
    pyttsx3.speak("I am here to help") 

  elif ("hey" in p) or ("hello" in p) or ("hi" in p) or ("hii" in p):
    os.system("color b5")
    print("\n\t\tHello,I am here to help")
    pyttsx3.speak("Hello,I am here to help")

  elif (("how" in p) and ("are" in p) and ("you" in p)) or ("hii" in p) or (("how" in p) and ("r" in p) and ("u" in p)):
    os.system("color f4")
    print("\n\t\tI am good, How can i help")
    pyttsx3.speak("I am good, How can i help")

  #run
  elif ("run" in p) or (("run" in p) and ("window" in p)) or (("window" in p) and ("r" in p)):
    os.system("color e4")
    print("\n\t\tOpening Run window")
    pyttsx3.speak("Opening run window")
    os.system("explorer.exe Shell:::{2559a1f3-21d7-11d4-bdaf-00c04f60b9f0}")


  #don't support
  else:
    print()
    print("\n\t\tdon't support")
    pyttsx3.speak("don't support")
    print("\n\t\tYou can say 'Run chrome'or \n\t\t'play music'or Menu")
    pyttsx3.speak("try saying... Run chrome, play music or Menu")
    

