# duino-discordbot

Before proceeding, there's few things that i assume yo already have:
1. Discord bot
2. Arduino board/generic
3. Arduino software

THe package that you should have for python:
1. discord.py
2. pyserial

The Steps:
1. Open the minimalduinobot.py program
2. copy your Bot(discord bot) token to the program
3. open your arduino software
4. upload the code duinoreceiver.ino to your board
5. keep the usb connection
6. on the minimalduinobot.py program on line 7, you need to add the communication port from your board connected, example "COM5"
7. run the python script
8. go to your server that has your discord bot
9. type the prefix command "!gf" followed by "on" or "off", you can change the prefix later.
10. wait for python and arduino process it
11. the onboard LED should glow after you send the command "!gf on"
