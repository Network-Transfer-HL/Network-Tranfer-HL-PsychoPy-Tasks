﻿#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2020.2.10),
    on June 07, 2021, at 22:18
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
prefs.hardware['audioLib'] = 'pyo'
from psychopy import sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2020.2.10'
expName = 'Lernen_NSWP'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='H:\\Luebeck\\Projects\\Juniorfoerderung\\Tasks\\Pilot\\NSWP\\Lernen_NSWP_Pilot_v2.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=[1366, 768], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "StartLernphase"
StartLernphaseClock = core.Clock()
Wilkommen = visual.TextStim(win=win, name='Wilkommen',
    text='Herzlich Willkommen!\n\nIn der folgenden Lernphase werden Ihnen 60 Wortpaare mit Pausen dazwischen präsentiert. Nach der Hälfte haben Sie eine kleine Pause.\n\nBitte versuchen Sie sich möglichst viele Wortpaare zu merken.\nEs ist hilfreich, die unsinnigen Wörter mit Ihnen vertrauten Bilddarstellungen zu verbinden.\n\nUm die Lernphase zu starten, drücken Sie bitte die Maustaste.\n\nViel Erfolg!',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
mouse = event.Mouse(win=win)
x, y = [None, None]
mouse.mouseClock = core.Clock()

# Initialize components for Routine "WaitingforScanner"
WaitingforScannerClock = core.Clock()
Wait_for_Scanner = visual.TextStim(win=win, name='Wait_for_Scanner',
    text='Warte auf Scanner',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
ScannerStart = keyboard.Keyboard()

# Initialize components for Routine "PreStimulus"
PreStimulusClock = core.Clock()
Kreuz = visual.ImageStim(
    win=win,
    name='Kreuz', 
    image='Kreuz.png', mask=None,
    ori=0, pos=(0, 0), size=(0.15, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Initialize components for Routine "WordPairPresentation"
WordPairPresentationClock = core.Clock()
Word1 = visual.TextBox2(
     win, text='default text', font='Arial',
     pos=(-0.4, 0),     letterHeight=0.12,
     size=(0.63, 0.382), borderWidth=2.0,
     color='black', colorSpace='rgb',
     opacity=1,
     bold=True, italic=False,
     lineSpacing=1.0,
     padding=0.12,
     anchor='center',
     fillColor='white', borderColor='white',
     flipHoriz=False, flipVert=False,
     editable=False,
     name='Word1',
     autoLog=True,
)
Word2 = visual.TextBox2(
     win, text='default text', font='Arial',
     pos=(0.4, 0),     letterHeight=0.12,
     size=(0.63,0.382), borderWidth=2.0,
     color='black', colorSpace='rgb',
     opacity=1,
     bold=True, italic=False,
     lineSpacing=1.0,
     padding=0.12,
     anchor='center',
     fillColor='white', borderColor='white',
     flipHoriz=False, flipVert=False,
     editable=False,
     name='Word2',
     autoLog=True,
)
Wort1 = visual.TextStim(win=win, name='Wort1',
    text='default text',
    font='Arial',
    pos=(-0.4, 0), height=0.12, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "ISIs"
ISIsClock = core.Clock()
Fixation = visual.ImageStim(
    win=win,
    name='Fixation', 
    image='Kreuz.png', mask=None,
    ori=0, pos=(0, 0), size=(0.15, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=0.0)

# Initialize components for Routine "PauseStart"
PauseStartClock = core.Clock()
Pause1 = visual.TextStim(win=win, name='Pause1',
    text='Kleine Pause',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp = keyboard.Keyboard()

# Initialize components for Routine "WaitingforScanner"
WaitingforScannerClock = core.Clock()
Wait_for_Scanner = visual.TextStim(win=win, name='Wait_for_Scanner',
    text='Warte auf Scanner',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
ScannerStart = keyboard.Keyboard()

# Initialize components for Routine "PreStimulus"
PreStimulusClock = core.Clock()
Kreuz = visual.ImageStim(
    win=win,
    name='Kreuz', 
    image='Kreuz.png', mask=None,
    ori=0, pos=(0, 0), size=(0.15, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Initialize components for Routine "WordPairPresentation"
WordPairPresentationClock = core.Clock()
Word1 = visual.TextBox2(
     win, text='default text', font='Arial',
     pos=(-0.4, 0),     letterHeight=0.12,
     size=(0.63, 0.382), borderWidth=2.0,
     color='black', colorSpace='rgb',
     opacity=1,
     bold=True, italic=False,
     lineSpacing=1.0,
     padding=0.12,
     anchor='center',
     fillColor='white', borderColor='white',
     flipHoriz=False, flipVert=False,
     editable=False,
     name='Word1',
     autoLog=True,
)
Word2 = visual.TextBox2(
     win, text='default text', font='Arial',
     pos=(0.4, 0),     letterHeight=0.12,
     size=(0.63,0.382), borderWidth=2.0,
     color='black', colorSpace='rgb',
     opacity=1,
     bold=True, italic=False,
     lineSpacing=1.0,
     padding=0.12,
     anchor='center',
     fillColor='white', borderColor='white',
     flipHoriz=False, flipVert=False,
     editable=False,
     name='Word2',
     autoLog=True,
)
Wort1 = visual.TextStim(win=win, name='Wort1',
    text='default text',
    font='Arial',
    pos=(-0.4, 0), height=0.12, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "ISIs"
ISIsClock = core.Clock()
Fixation = visual.ImageStim(
    win=win,
    name='Fixation', 
    image='Kreuz.png', mask=None,
    ori=0, pos=(0, 0), size=(0.15, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=0.0)

# Initialize components for Routine "EndeLernphase"
EndeLernphaseClock = core.Clock()
TextEnde = visual.TextStim(win=win, name='TextEnde',
    text='Ende\n\nVielen Dank ',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "StartLernphase"-------
continueRoutine = True
# update component parameters for each repeat
# setup some python lists for storing info about the mouse
mouse.x = []
mouse.y = []
mouse.leftButton = []
mouse.midButton = []
mouse.rightButton = []
mouse.time = []
gotValidClick = False  # until a click is received
mouse.mouseClock.reset()
# keep track of which components have finished
StartLernphaseComponents = [Wilkommen, mouse]
for thisComponent in StartLernphaseComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
StartLernphaseClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "StartLernphase"-------
while continueRoutine:
    # get current time
    t = StartLernphaseClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=StartLernphaseClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Wilkommen* updates
    if Wilkommen.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Wilkommen.frameNStart = frameN  # exact frame index
        Wilkommen.tStart = t  # local t and not account for scr refresh
        Wilkommen.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Wilkommen, 'tStartRefresh')  # time at next scr refresh
        Wilkommen.setAutoDraw(True)
    # *mouse* updates
    if mouse.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mouse.frameNStart = frameN  # exact frame index
        mouse.tStart = t  # local t and not account for scr refresh
        mouse.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mouse, 'tStartRefresh')  # time at next scr refresh
        mouse.status = STARTED
        prevButtonState = mouse.getPressed()  # if button is down already this ISN'T a new click
    if mouse.status == STARTED:  # only update if started and not finished!
        buttons = mouse.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                x, y = mouse.getPos()
                mouse.x.append(x)
                mouse.y.append(y)
                buttons = mouse.getPressed()
                mouse.leftButton.append(buttons[0])
                mouse.midButton.append(buttons[1])
                mouse.rightButton.append(buttons[2])
                mouse.time.append(mouse.mouseClock.getTime())
                # abort routine on response
                continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in StartLernphaseComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "StartLernphase"-------
for thisComponent in StartLernphaseComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('Wilkommen.started', Wilkommen.tStartRefresh)
thisExp.addData('Wilkommen.stopped', Wilkommen.tStopRefresh)
# store data for thisExp (ExperimentHandler)
if len(mouse.x): thisExp.addData('mouse.x', mouse.x[0])
if len(mouse.y): thisExp.addData('mouse.y', mouse.y[0])
if len(mouse.leftButton): thisExp.addData('mouse.leftButton', mouse.leftButton[0])
if len(mouse.midButton): thisExp.addData('mouse.midButton', mouse.midButton[0])
if len(mouse.rightButton): thisExp.addData('mouse.rightButton', mouse.rightButton[0])
if len(mouse.time): thisExp.addData('mouse.time', mouse.time[0])
thisExp.addData('mouse.started', mouse.tStart)
thisExp.addData('mouse.stopped', mouse.tStop)
thisExp.nextEntry()
# the Routine "StartLernphase" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "WaitingforScanner"-------
continueRoutine = True
# update component parameters for each repeat
ScannerStart.keys = []
ScannerStart.rt = []
_ScannerStart_allKeys = []
# keep track of which components have finished
WaitingforScannerComponents = [Wait_for_Scanner, ScannerStart]
for thisComponent in WaitingforScannerComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
WaitingforScannerClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "WaitingforScanner"-------
while continueRoutine:
    # get current time
    t = WaitingforScannerClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=WaitingforScannerClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Wait_for_Scanner* updates
    if Wait_for_Scanner.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Wait_for_Scanner.frameNStart = frameN  # exact frame index
        Wait_for_Scanner.tStart = t  # local t and not account for scr refresh
        Wait_for_Scanner.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Wait_for_Scanner, 'tStartRefresh')  # time at next scr refresh
        Wait_for_Scanner.setAutoDraw(True)
    
    # *ScannerStart* updates
    waitOnFlip = False
    if ScannerStart.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        ScannerStart.frameNStart = frameN  # exact frame index
        ScannerStart.tStart = t  # local t and not account for scr refresh
        ScannerStart.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(ScannerStart, 'tStartRefresh')  # time at next scr refresh
        ScannerStart.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(ScannerStart.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(ScannerStart.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if ScannerStart.status == STARTED and not waitOnFlip:
        theseKeys = ScannerStart.getKeys(keyList=['s'], waitRelease=False)
        _ScannerStart_allKeys.extend(theseKeys)
        if len(_ScannerStart_allKeys):
            ScannerStart.keys = _ScannerStart_allKeys[-1].name  # just the last key pressed
            ScannerStart.rt = _ScannerStart_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in WaitingforScannerComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "WaitingforScanner"-------
for thisComponent in WaitingforScannerComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('Wait_for_Scanner.started', Wait_for_Scanner.tStartRefresh)
thisExp.addData('Wait_for_Scanner.stopped', Wait_for_Scanner.tStopRefresh)
# check responses
if ScannerStart.keys in ['', [], None]:  # No response was made
    ScannerStart.keys = None
thisExp.addData('ScannerStart.keys',ScannerStart.keys)
if ScannerStart.keys != None:  # we had a response
    thisExp.addData('ScannerStart.rt', ScannerStart.rt)
thisExp.addData('ScannerStart.started', ScannerStart.tStartRefresh)
thisExp.addData('ScannerStart.stopped', ScannerStart.tStopRefresh)
thisExp.nextEntry()
# the Routine "WaitingforScanner" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "PreStimulus"-------
continueRoutine = True
routineTimer.add(1.000000)
# update component parameters for each repeat
# keep track of which components have finished
PreStimulusComponents = [Kreuz]
for thisComponent in PreStimulusComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
PreStimulusClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "PreStimulus"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = PreStimulusClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=PreStimulusClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Kreuz* updates
    if Kreuz.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Kreuz.frameNStart = frameN  # exact frame index
        Kreuz.tStart = t  # local t and not account for scr refresh
        Kreuz.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Kreuz, 'tStartRefresh')  # time at next scr refresh
        Kreuz.setAutoDraw(True)
    if Kreuz.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > Kreuz.tStartRefresh + 1.0-frameTolerance:
            # keep track of stop time/frame for later
            Kreuz.tStop = t  # not accounting for scr refresh
            Kreuz.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Kreuz, 'tStopRefresh')  # time at next scr refresh
            Kreuz.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in PreStimulusComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "PreStimulus"-------
for thisComponent in PreStimulusComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('Kreuz.started', Kreuz.tStartRefresh)
thisExp.addData('Kreuz.stopped', Kreuz.tStopRefresh)

# set up handler to look after randomisation of conditions etc
Encode1 = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('NSWP_Lernen_Stimulus_List.xlsx', selection='0:30'),
    seed=None, name='Encode1')
thisExp.addLoop(Encode1)  # add the loop to the experiment
thisEncode1 = Encode1.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisEncode1.rgb)
if thisEncode1 != None:
    for paramName in thisEncode1:
        exec('{} = thisEncode1[paramName]'.format(paramName))

for thisEncode1 in Encode1:
    currentLoop = Encode1
    # abbreviate parameter names if possible (e.g. rgb = thisEncode1.rgb)
    if thisEncode1 != None:
        for paramName in thisEncode1:
            exec('{} = thisEncode1[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "WordPairPresentation"-------
    continueRoutine = True
    routineTimer.add(3.000000)
    # update component parameters for each repeat
    Word1.setText(Cue)
    Word2.setText(Target)
    Wort1.setText(Cue)
    # keep track of which components have finished
    WordPairPresentationComponents = [Word1, Word2, Wort1]
    for thisComponent in WordPairPresentationComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    WordPairPresentationClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "WordPairPresentation"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = WordPairPresentationClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=WordPairPresentationClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Word1* updates
        if Word1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Word1.frameNStart = frameN  # exact frame index
            Word1.tStart = t  # local t and not account for scr refresh
            Word1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Word1, 'tStartRefresh')  # time at next scr refresh
            Word1.setAutoDraw(True)
        if Word1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Word1.tStartRefresh + 3.0-frameTolerance:
                # keep track of stop time/frame for later
                Word1.tStop = t  # not accounting for scr refresh
                Word1.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Word1, 'tStopRefresh')  # time at next scr refresh
                Word1.setAutoDraw(False)
        
        # *Word2* updates
        if Word2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Word2.frameNStart = frameN  # exact frame index
            Word2.tStart = t  # local t and not account for scr refresh
            Word2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Word2, 'tStartRefresh')  # time at next scr refresh
            Word2.setAutoDraw(True)
        if Word2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Word2.tStartRefresh + 3.0-frameTolerance:
                # keep track of stop time/frame for later
                Word2.tStop = t  # not accounting for scr refresh
                Word2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Word2, 'tStopRefresh')  # time at next scr refresh
                Word2.setAutoDraw(False)
        
        # *Wort1* updates
        if Wort1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Wort1.frameNStart = frameN  # exact frame index
            Wort1.tStart = t  # local t and not account for scr refresh
            Wort1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Wort1, 'tStartRefresh')  # time at next scr refresh
            Wort1.setAutoDraw(True)
        if Wort1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Wort1.tStartRefresh + 3.0-frameTolerance:
                # keep track of stop time/frame for later
                Wort1.tStop = t  # not accounting for scr refresh
                Wort1.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Wort1, 'tStopRefresh')  # time at next scr refresh
                Wort1.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in WordPairPresentationComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "WordPairPresentation"-------
    for thisComponent in WordPairPresentationComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    Encode1.addData('Word1.started', Word1.tStartRefresh)
    Encode1.addData('Word1.stopped', Word1.tStopRefresh)
    Encode1.addData('Word2.started', Word2.tStartRefresh)
    Encode1.addData('Word2.stopped', Word2.tStopRefresh)
    Encode1.addData('Wort1.started', Wort1.tStartRefresh)
    Encode1.addData('Wort1.stopped', Wort1.tStopRefresh)
    
    # ------Prepare to start Routine "ISIs"-------
    continueRoutine = True
    # update component parameters for each repeat
    jitter = random() * 3.3 + 1.7
    jitter = round(jitter, 1)
    thisExp.addData('jitter', jitter)
    # keep track of which components have finished
    ISIsComponents = [Fixation]
    for thisComponent in ISIsComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    ISIsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "ISIs"-------
    while continueRoutine:
        # get current time
        t = ISIsClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=ISIsClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Fixation* updates
        if Fixation.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Fixation.frameNStart = frameN  # exact frame index
            Fixation.tStart = t  # local t and not account for scr refresh
            Fixation.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Fixation, 'tStartRefresh')  # time at next scr refresh
            Fixation.setAutoDraw(True)
        if Fixation.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Fixation.tStartRefresh + jitter-frameTolerance:
                # keep track of stop time/frame for later
                Fixation.tStop = t  # not accounting for scr refresh
                Fixation.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Fixation, 'tStopRefresh')  # time at next scr refresh
                Fixation.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ISIsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "ISIs"-------
    for thisComponent in ISIsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    Encode1.addData('Fixation.started', Fixation.tStartRefresh)
    Encode1.addData('Fixation.stopped', Fixation.tStopRefresh)
    # the Routine "ISIs" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'Encode1'


# ------Prepare to start Routine "PauseStart"-------
continueRoutine = True
# update component parameters for each repeat
key_resp.keys = []
key_resp.rt = []
_key_resp_allKeys = []
# keep track of which components have finished
PauseStartComponents = [Pause1, key_resp]
for thisComponent in PauseStartComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
PauseStartClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "PauseStart"-------
while continueRoutine:
    # get current time
    t = PauseStartClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=PauseStartClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Pause1* updates
    if Pause1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Pause1.frameNStart = frameN  # exact frame index
        Pause1.tStart = t  # local t and not account for scr refresh
        Pause1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Pause1, 'tStartRefresh')  # time at next scr refresh
        Pause1.setAutoDraw(True)
    
    # *key_resp* updates
    waitOnFlip = False
    if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp.frameNStart = frameN  # exact frame index
        key_resp.tStart = t  # local t and not account for scr refresh
        key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
        key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp.status == STARTED and not waitOnFlip:
        theseKeys = key_resp.getKeys(keyList=['enter', 'space'], waitRelease=False)
        _key_resp_allKeys.extend(theseKeys)
        if len(_key_resp_allKeys):
            key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
            key_resp.rt = _key_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in PauseStartComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "PauseStart"-------
for thisComponent in PauseStartComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('Pause1.started', Pause1.tStartRefresh)
thisExp.addData('Pause1.stopped', Pause1.tStopRefresh)
# check responses
if key_resp.keys in ['', [], None]:  # No response was made
    key_resp.keys = None
thisExp.addData('key_resp.keys',key_resp.keys)
if key_resp.keys != None:  # we had a response
    thisExp.addData('key_resp.rt', key_resp.rt)
thisExp.addData('key_resp.started', key_resp.tStartRefresh)
thisExp.addData('key_resp.stopped', key_resp.tStopRefresh)
thisExp.nextEntry()
# the Routine "PauseStart" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "WaitingforScanner"-------
continueRoutine = True
# update component parameters for each repeat
ScannerStart.keys = []
ScannerStart.rt = []
_ScannerStart_allKeys = []
# keep track of which components have finished
WaitingforScannerComponents = [Wait_for_Scanner, ScannerStart]
for thisComponent in WaitingforScannerComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
WaitingforScannerClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "WaitingforScanner"-------
while continueRoutine:
    # get current time
    t = WaitingforScannerClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=WaitingforScannerClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Wait_for_Scanner* updates
    if Wait_for_Scanner.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Wait_for_Scanner.frameNStart = frameN  # exact frame index
        Wait_for_Scanner.tStart = t  # local t and not account for scr refresh
        Wait_for_Scanner.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Wait_for_Scanner, 'tStartRefresh')  # time at next scr refresh
        Wait_for_Scanner.setAutoDraw(True)
    
    # *ScannerStart* updates
    waitOnFlip = False
    if ScannerStart.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        ScannerStart.frameNStart = frameN  # exact frame index
        ScannerStart.tStart = t  # local t and not account for scr refresh
        ScannerStart.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(ScannerStart, 'tStartRefresh')  # time at next scr refresh
        ScannerStart.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(ScannerStart.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(ScannerStart.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if ScannerStart.status == STARTED and not waitOnFlip:
        theseKeys = ScannerStart.getKeys(keyList=['s'], waitRelease=False)
        _ScannerStart_allKeys.extend(theseKeys)
        if len(_ScannerStart_allKeys):
            ScannerStart.keys = _ScannerStart_allKeys[-1].name  # just the last key pressed
            ScannerStart.rt = _ScannerStart_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in WaitingforScannerComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "WaitingforScanner"-------
for thisComponent in WaitingforScannerComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('Wait_for_Scanner.started', Wait_for_Scanner.tStartRefresh)
thisExp.addData('Wait_for_Scanner.stopped', Wait_for_Scanner.tStopRefresh)
# check responses
if ScannerStart.keys in ['', [], None]:  # No response was made
    ScannerStart.keys = None
thisExp.addData('ScannerStart.keys',ScannerStart.keys)
if ScannerStart.keys != None:  # we had a response
    thisExp.addData('ScannerStart.rt', ScannerStart.rt)
thisExp.addData('ScannerStart.started', ScannerStart.tStartRefresh)
thisExp.addData('ScannerStart.stopped', ScannerStart.tStopRefresh)
thisExp.nextEntry()
# the Routine "WaitingforScanner" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "PreStimulus"-------
continueRoutine = True
routineTimer.add(1.000000)
# update component parameters for each repeat
# keep track of which components have finished
PreStimulusComponents = [Kreuz]
for thisComponent in PreStimulusComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
PreStimulusClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "PreStimulus"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = PreStimulusClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=PreStimulusClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Kreuz* updates
    if Kreuz.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Kreuz.frameNStart = frameN  # exact frame index
        Kreuz.tStart = t  # local t and not account for scr refresh
        Kreuz.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Kreuz, 'tStartRefresh')  # time at next scr refresh
        Kreuz.setAutoDraw(True)
    if Kreuz.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > Kreuz.tStartRefresh + 1.0-frameTolerance:
            # keep track of stop time/frame for later
            Kreuz.tStop = t  # not accounting for scr refresh
            Kreuz.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Kreuz, 'tStopRefresh')  # time at next scr refresh
            Kreuz.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in PreStimulusComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "PreStimulus"-------
for thisComponent in PreStimulusComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('Kreuz.started', Kreuz.tStartRefresh)
thisExp.addData('Kreuz.stopped', Kreuz.tStopRefresh)

# set up handler to look after randomisation of conditions etc
Encode2 = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('NSWP_Lernen_Stimulus_List.xlsx', selection='31:60'),
    seed=None, name='Encode2')
thisExp.addLoop(Encode2)  # add the loop to the experiment
thisEncode2 = Encode2.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisEncode2.rgb)
if thisEncode2 != None:
    for paramName in thisEncode2:
        exec('{} = thisEncode2[paramName]'.format(paramName))

for thisEncode2 in Encode2:
    currentLoop = Encode2
    # abbreviate parameter names if possible (e.g. rgb = thisEncode2.rgb)
    if thisEncode2 != None:
        for paramName in thisEncode2:
            exec('{} = thisEncode2[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "WordPairPresentation"-------
    continueRoutine = True
    routineTimer.add(3.000000)
    # update component parameters for each repeat
    Word1.setText(Cue)
    Word2.setText(Target)
    Wort1.setText(Cue)
    # keep track of which components have finished
    WordPairPresentationComponents = [Word1, Word2, Wort1]
    for thisComponent in WordPairPresentationComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    WordPairPresentationClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "WordPairPresentation"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = WordPairPresentationClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=WordPairPresentationClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Word1* updates
        if Word1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Word1.frameNStart = frameN  # exact frame index
            Word1.tStart = t  # local t and not account for scr refresh
            Word1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Word1, 'tStartRefresh')  # time at next scr refresh
            Word1.setAutoDraw(True)
        if Word1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Word1.tStartRefresh + 3.0-frameTolerance:
                # keep track of stop time/frame for later
                Word1.tStop = t  # not accounting for scr refresh
                Word1.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Word1, 'tStopRefresh')  # time at next scr refresh
                Word1.setAutoDraw(False)
        
        # *Word2* updates
        if Word2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Word2.frameNStart = frameN  # exact frame index
            Word2.tStart = t  # local t and not account for scr refresh
            Word2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Word2, 'tStartRefresh')  # time at next scr refresh
            Word2.setAutoDraw(True)
        if Word2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Word2.tStartRefresh + 3.0-frameTolerance:
                # keep track of stop time/frame for later
                Word2.tStop = t  # not accounting for scr refresh
                Word2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Word2, 'tStopRefresh')  # time at next scr refresh
                Word2.setAutoDraw(False)
        
        # *Wort1* updates
        if Wort1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Wort1.frameNStart = frameN  # exact frame index
            Wort1.tStart = t  # local t and not account for scr refresh
            Wort1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Wort1, 'tStartRefresh')  # time at next scr refresh
            Wort1.setAutoDraw(True)
        if Wort1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Wort1.tStartRefresh + 3.0-frameTolerance:
                # keep track of stop time/frame for later
                Wort1.tStop = t  # not accounting for scr refresh
                Wort1.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Wort1, 'tStopRefresh')  # time at next scr refresh
                Wort1.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in WordPairPresentationComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "WordPairPresentation"-------
    for thisComponent in WordPairPresentationComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    Encode2.addData('Word1.started', Word1.tStartRefresh)
    Encode2.addData('Word1.stopped', Word1.tStopRefresh)
    Encode2.addData('Word2.started', Word2.tStartRefresh)
    Encode2.addData('Word2.stopped', Word2.tStopRefresh)
    Encode2.addData('Wort1.started', Wort1.tStartRefresh)
    Encode2.addData('Wort1.stopped', Wort1.tStopRefresh)
    
    # ------Prepare to start Routine "ISIs"-------
    continueRoutine = True
    # update component parameters for each repeat
    jitter = random() * 3.3 + 1.7
    jitter = round(jitter, 1)
    thisExp.addData('jitter', jitter)
    # keep track of which components have finished
    ISIsComponents = [Fixation]
    for thisComponent in ISIsComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    ISIsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "ISIs"-------
    while continueRoutine:
        # get current time
        t = ISIsClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=ISIsClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Fixation* updates
        if Fixation.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Fixation.frameNStart = frameN  # exact frame index
            Fixation.tStart = t  # local t and not account for scr refresh
            Fixation.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Fixation, 'tStartRefresh')  # time at next scr refresh
            Fixation.setAutoDraw(True)
        if Fixation.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Fixation.tStartRefresh + jitter-frameTolerance:
                # keep track of stop time/frame for later
                Fixation.tStop = t  # not accounting for scr refresh
                Fixation.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Fixation, 'tStopRefresh')  # time at next scr refresh
                Fixation.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ISIsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "ISIs"-------
    for thisComponent in ISIsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    Encode2.addData('Fixation.started', Fixation.tStartRefresh)
    Encode2.addData('Fixation.stopped', Fixation.tStopRefresh)
    # the Routine "ISIs" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'Encode2'


# ------Prepare to start Routine "EndeLernphase"-------
continueRoutine = True
routineTimer.add(2.000000)
# update component parameters for each repeat
# keep track of which components have finished
EndeLernphaseComponents = [TextEnde]
for thisComponent in EndeLernphaseComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
EndeLernphaseClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "EndeLernphase"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = EndeLernphaseClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=EndeLernphaseClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *TextEnde* updates
    if TextEnde.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        TextEnde.frameNStart = frameN  # exact frame index
        TextEnde.tStart = t  # local t and not account for scr refresh
        TextEnde.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(TextEnde, 'tStartRefresh')  # time at next scr refresh
        TextEnde.setAutoDraw(True)
    if TextEnde.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > TextEnde.tStartRefresh + 2-frameTolerance:
            # keep track of stop time/frame for later
            TextEnde.tStop = t  # not accounting for scr refresh
            TextEnde.frameNStop = frameN  # exact frame index
            win.timeOnFlip(TextEnde, 'tStopRefresh')  # time at next scr refresh
            TextEnde.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in EndeLernphaseComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "EndeLernphase"-------
for thisComponent in EndeLernphaseComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('TextEnde.started', TextEnde.tStartRefresh)
thisExp.addData('TextEnde.stopped', TextEnde.tStopRefresh)

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
