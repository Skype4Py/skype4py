# -*- coding: utf-8 -*-

import sys
import Skype4Py
import time
import re

def AttachmentStatusText(status):
   return skype.Convert.AttachmentStatusToText(status)

# This handler is fired when Skype attatchment status changes
def OnAttach(status): 
    print 'API attachment status: ' + AttachmentStatusText(status)
    if status == Skype4Py.apiAttachAvailable:
        skype.Attach()

def handleMessage(msg):
    res = []
    for regex, message in patterns.iteritems():
        pattern = re.compile(regex, re.I)
        if pattern.search(msg):
            res.append(message)
    if len(res) == 0:
        return None
    else:
        return ' '.join(res)

def MessageHistory(user):
    print "Something changed.... "+user
    

def MessageStatus(msg, status):
    #print status, str(msg.Body.encode('utf-8'))
    if not msg.Chat.Name == chat.Name:
        return
    if status == Skype4Py.cmsReceived:
        msgText = str(msg.Body.encode('utf-8'))
        #print "STATUS: "+str(status)
        res = handleMessage(msgText)
        if not res == None:
            msg.Chat.SendMessage(res)
        #if msg.Chat.Type in (Skype4Py.chatTypeDialog, Skype4Py.chatTypeLegacyDialog):
        #print 'GOT MSG: '+msgText
            
skype = Skype4Py.Skype()
skype.OnAttachmentStatus = OnAttach
skype.OnMessageStatus = MessageStatus
skype.OnMessageHistory = MessageHistory

patterns = {}
patterns[".*f.+rst.*"] = "Second"
patterns[".*davse.*"] = "Mente du D-Diddy?"
patterns[".*cloud.*"] = "Jeg kan anbefale Microsoft Azure."


# Starting Skype if it's not running already..
if not skype.Client.IsRunning:
    print 'Starting Skype..'
    skype.Client.Start()

# Attatching to Skype..
print 'Connecting to Skype..'
skype.Attach()

#Id on group chat
chatid = sys.argv[1]
print 'Connecting to chat with id: '+chatid

chat = None

for i in skype.Chats:
    #print i.Name
    if str(i.Name).endswith(chatid):
        chat = i
        for m in i.Members:
            print m.Handle
        break

#if not chat == None:
#    chat.SendMessage('First')

while True:
    time.sleep(1.5)

sys.exit()
