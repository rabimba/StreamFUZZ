# StreamFUZZ
==========

## Description ##

A RTSP based Stream Fuzzer in Python

StreamFuzz is a Real Time Streaming Protocol Server Fuzzer(a python script near about 600 lines)coded by myself.
This fuzzer uses 6 basic crafting and 9 advanced crafting technique to test any target application.

## Key Features: ##

1)This fuzzer uses 6 basic crafting technique with OPTIONS,DESCRIBE,SETUP,PLAY,GET_PARAMETER,TEARDOWN,PAUSE etc rtsp commands and 9 advanced crafting technique to test any target application.
2)Ability to fuzz with Metasploit Pattern (pattern_create.rb) can be helpful to find offset.

## How to use?? ##

1)First edit "rtsp.conf" file with your favorite text editor.Change the Parameters as per your requirement.You should get parameters description in the configuration file.
2)Give Write permission to LOG.TXT (chmod 777 README.TXT)
3)Give execution permission to "StreamFuzz.py" file.(chmod 777 StreamFuzz.py)
4)In shell type "python StreamFuzz.py".Now the script will show your preferences provided in the configuration file.If the information are correct then press enter to start fuzzing.
5)The program will always save the last successful request in LOG.TXT file.When the target crashes go to LOG.TXT file to check the Buffer length and the exact request sent.
