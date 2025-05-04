#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.1.1),
    on Thu Mar 17 07:23:48 2022
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2022.1.1'
expName = 'Abfrage_FPA'  # from the Builder filename that created this script
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
    originPath='/Users/charlotte/Desktop/DOCUMENTS/UNI/MEDIZIN/PROMOTION/Behaviour/PsychoPy/Adaptation/FPA_Adaptation/Abfrage_FPA_Adaptation_lastrun.py',
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
# Setup ioHub
ioConfig = {}

# Setup iohub keyboard
ioConfig['Keyboard'] = dict(use_keymap='psychopy')

ioSession = '1'
if 'session' in expInfo:
    ioSession = str(expInfo['session'])
ioServer = io.launchHubServer(window=win, **ioConfig)
eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard(backend='iohub')

# Initialize components for Routine "Anleitung1"
Anleitung1Clock = core.Clock()
Anleitungstext1 = visual.TextStim(win=win, name='Anleitungstext1',
    text='Im Folgenden wird Ihnen auf der linken Seite des Bildschirms eine Figur gezeigt.\n\nAuf der rechten Seite werden vier Antwortmöglichkeiten zu sehen sein. \n\nBitte antworten Sie immer erst, wenn die Pfeile zwischen den Antwortmöglichkeiten auftauchen.\nSie haben dann 4 Sekunden um mit einem Mausklick das korrekte Figurenpaar aus der Lernphase zu vervollständigen.\n\n-> Weiter mit einem Mausklick',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
mouseNext = event.Mouse(win=win)
x, y = [None, None]
mouseNext.mouseClock = core.Clock()

# Initialize components for Routine "Anleitung2"
Anleitung2Clock = core.Clock()
Anleitungstext2 = visual.TextStim(win=win, name='Anleitungstext2',
    text='Bei jeder Aufgabe haben Sie insgesamt 7 Sekunden Zeit zu antworten.\n\nZwischen den Aufgaben wird es kurze Pausen geben.\n\n-> Starten mit einem Mausklick',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
mouse = event.Mouse(win=win)
x, y = [None, None]
mouse.mouseClock = core.Clock()

# Initialize components for Routine "PreStimulus"
PreStimulusClock = core.Clock()
Cross = visual.ImageStim(
    win=win,
    name='Cross', 
    image='Kreuz.png', mask=None, anchor='center',
    ori=0, pos=(0, 0), size=(0.15, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Initialize components for Routine "Abfrage"
AbfrageClock = core.Clock()
CueFigure = visual.ImageStim(
    win=win,
    name='CueFigure', 
    image='sin', mask=None, anchor='center',
    ori=0, pos=(-0.5, 0), size=(0.380, 0.220),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=0.0)
topLeft = visual.ImageStim(
    win=win,
    name='topLeft', 
    image='sin', mask=None, anchor='center',
    ori=0, pos=(0.1, 0.20), size=(0.380, 0.220),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-1.0)
bottomLeft = visual.ImageStim(
    win=win,
    name='bottomLeft', 
    image='sin', mask=None, anchor='center',
    ori=0, pos=(0.1, -0.2), size=(0.380, 0.220),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-2.0)
topRight = visual.ImageStim(
    win=win,
    name='topRight', 
    image='sin', mask=None, anchor='center',
    ori=0, pos=(0.6, 0.2), size=(0.380, 0.220),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-3.0)
bottomRight = visual.ImageStim(
    win=win,
    name='bottomRight', 
    image='sin', mask=None, anchor='center',
    ori=0, pos=(0.6, -0.2), size=(0.380, 0.220),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-4.0)
Pfeile = visual.ImageStim(
    win=win,
    name='Pfeile', 
    image='Pfeile.png', mask=None, anchor='center',
    ori=45, pos=(0.35, 0), size=(0.315, 0.191),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-5.0)
mouse_resp = event.Mouse(win=win)
x, y = [None, None]
mouse_resp.mouseClock = core.Clock()

# Initialize components for Routine "ISIs"
ISIsClock = core.Clock()
Fixation = visual.ImageStim(
    win=win,
    name='Fixation', 
    image='Kreuz.png', mask=None, anchor='center',
    ori=0, pos=(0, 0), size=(0.15, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=0.0)

# Initialize components for Routine "VielenDank"
VielenDankClock = core.Clock()
Ende = visual.TextStim(win=win, name='Ende',
    text='Ende\n\nVielen Dank!',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "Anleitung1"-------
continueRoutine = True
# update component parameters for each repeat
# setup some python lists for storing info about the mouseNext
mouseNext.x = []
mouseNext.y = []
mouseNext.leftButton = []
mouseNext.midButton = []
mouseNext.rightButton = []
mouseNext.time = []
gotValidClick = False  # until a click is received
mouseNext.mouseClock.reset()
# keep track of which components have finished
Anleitung1Components = [Anleitungstext1, mouseNext]
for thisComponent in Anleitung1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Anleitung1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Anleitung1"-------
while continueRoutine:
    # get current time
    t = Anleitung1Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Anleitung1Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Anleitungstext1* updates
    if Anleitungstext1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Anleitungstext1.frameNStart = frameN  # exact frame index
        Anleitungstext1.tStart = t  # local t and not account for scr refresh
        Anleitungstext1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Anleitungstext1, 'tStartRefresh')  # time at next scr refresh
        Anleitungstext1.setAutoDraw(True)
    # *mouseNext* updates
    if mouseNext.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mouseNext.frameNStart = frameN  # exact frame index
        mouseNext.tStart = t  # local t and not account for scr refresh
        mouseNext.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mouseNext, 'tStartRefresh')  # time at next scr refresh
        mouseNext.status = STARTED
        prevButtonState = mouseNext.getPressed()  # if button is down already this ISN'T a new click
    if mouseNext.status == STARTED:  # only update if started and not finished!
        buttons = mouseNext.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                x, y = mouseNext.getPos()
                mouseNext.x.append(x)
                mouseNext.y.append(y)
                buttons = mouseNext.getPressed()
                mouseNext.leftButton.append(buttons[0])
                mouseNext.midButton.append(buttons[1])
                mouseNext.rightButton.append(buttons[2])
                mouseNext.time.append(mouseNext.mouseClock.getTime())
                
                continueRoutine = False  # abort routine on response
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Anleitung1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Anleitung1"-------
for thisComponent in Anleitung1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('Anleitungstext1.started', Anleitungstext1.tStartRefresh)
thisExp.addData('Anleitungstext1.stopped', Anleitungstext1.tStopRefresh)
# store data for thisExp (ExperimentHandler)
thisExp.addData('mouseNext.x', mouseNext.x)
thisExp.addData('mouseNext.y', mouseNext.y)
thisExp.addData('mouseNext.leftButton', mouseNext.leftButton)
thisExp.addData('mouseNext.midButton', mouseNext.midButton)
thisExp.addData('mouseNext.rightButton', mouseNext.rightButton)
thisExp.addData('mouseNext.time', mouseNext.time)
thisExp.addData('mouseNext.started', mouseNext.tStart)
thisExp.addData('mouseNext.stopped', mouseNext.tStop)
thisExp.nextEntry()
# the Routine "Anleitung1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Anleitung2"-------
continueRoutine = True
# update component parameters for each repeat
# setup some python lists for storing info about the mouse
gotValidClick = False  # until a click is received
# keep track of which components have finished
Anleitung2Components = [Anleitungstext2, mouse]
for thisComponent in Anleitung2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Anleitung2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Anleitung2"-------
while continueRoutine:
    # get current time
    t = Anleitung2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Anleitung2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Anleitungstext2* updates
    if Anleitungstext2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Anleitungstext2.frameNStart = frameN  # exact frame index
        Anleitungstext2.tStart = t  # local t and not account for scr refresh
        Anleitungstext2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Anleitungstext2, 'tStartRefresh')  # time at next scr refresh
        Anleitungstext2.setAutoDraw(True)
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
                continueRoutine = False  # abort routine on response    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Anleitung2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Anleitung2"-------
for thisComponent in Anleitung2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('Anleitungstext2.started', Anleitungstext2.tStartRefresh)
thisExp.addData('Anleitungstext2.stopped', Anleitungstext2.tStopRefresh)
# store data for thisExp (ExperimentHandler)
thisExp.addData('mouse.started', mouse.tStart)
thisExp.addData('mouse.stopped', mouse.tStop)
thisExp.nextEntry()
# the Routine "Anleitung2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "PreStimulus"-------
continueRoutine = True
routineTimer.add(1.000000)
# update component parameters for each repeat
# keep track of which components have finished
PreStimulusComponents = [Cross]
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
    
    # *Cross* updates
    if Cross.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Cross.frameNStart = frameN  # exact frame index
        Cross.tStart = t  # local t and not account for scr refresh
        Cross.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Cross, 'tStartRefresh')  # time at next scr refresh
        Cross.setAutoDraw(True)
    if Cross.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > Cross.tStartRefresh + 1.0-frameTolerance:
            # keep track of stop time/frame for later
            Cross.tStop = t  # not accounting for scr refresh
            Cross.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Cross, 'tStopRefresh')  # time at next scr refresh
            Cross.setAutoDraw(False)
    
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
thisExp.addData('Cross.started', Cross.tStartRefresh)
thisExp.addData('Cross.stopped', Cross.tStopRefresh)

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('FPA_Abfrage_Stimulus_List.xlsx', selection='0:6'),
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "Abfrage"-------
    continueRoutine = True
    routineTimer.add(7.000000)
    # update component parameters for each repeat
    CueFigure.setImage(Cue)
    topLeft.setImage(L1)
    bottomLeft.setImage(L2)
    topRight.setImage(R1)
    bottomRight.setImage(R2)
    # setup some python lists for storing info about the mouse_resp
    mouse_resp.x = []
    mouse_resp.y = []
    mouse_resp.leftButton = []
    mouse_resp.midButton = []
    mouse_resp.rightButton = []
    mouse_resp.time = []
    mouse_resp.clicked_name = []
    gotValidClick = False  # until a click is received
    mouse_resp.mouseClock.reset()
    # keep track of which components have finished
    AbfrageComponents = [CueFigure, topLeft, bottomLeft, topRight, bottomRight, Pfeile, mouse_resp]
    for thisComponent in AbfrageComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    AbfrageClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Abfrage"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = AbfrageClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=AbfrageClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *CueFigure* updates
        if CueFigure.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            CueFigure.frameNStart = frameN  # exact frame index
            CueFigure.tStart = t  # local t and not account for scr refresh
            CueFigure.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(CueFigure, 'tStartRefresh')  # time at next scr refresh
            CueFigure.setAutoDraw(True)
        if CueFigure.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > CueFigure.tStartRefresh + 7-frameTolerance:
                # keep track of stop time/frame for later
                CueFigure.tStop = t  # not accounting for scr refresh
                CueFigure.frameNStop = frameN  # exact frame index
                win.timeOnFlip(CueFigure, 'tStopRefresh')  # time at next scr refresh
                CueFigure.setAutoDraw(False)
        
        # *topLeft* updates
        if topLeft.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            topLeft.frameNStart = frameN  # exact frame index
            topLeft.tStart = t  # local t and not account for scr refresh
            topLeft.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(topLeft, 'tStartRefresh')  # time at next scr refresh
            topLeft.setAutoDraw(True)
        if topLeft.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > topLeft.tStartRefresh + 7-frameTolerance:
                # keep track of stop time/frame for later
                topLeft.tStop = t  # not accounting for scr refresh
                topLeft.frameNStop = frameN  # exact frame index
                win.timeOnFlip(topLeft, 'tStopRefresh')  # time at next scr refresh
                topLeft.setAutoDraw(False)
        
        # *bottomLeft* updates
        if bottomLeft.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            bottomLeft.frameNStart = frameN  # exact frame index
            bottomLeft.tStart = t  # local t and not account for scr refresh
            bottomLeft.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(bottomLeft, 'tStartRefresh')  # time at next scr refresh
            bottomLeft.setAutoDraw(True)
        if bottomLeft.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > bottomLeft.tStartRefresh + 7-frameTolerance:
                # keep track of stop time/frame for later
                bottomLeft.tStop = t  # not accounting for scr refresh
                bottomLeft.frameNStop = frameN  # exact frame index
                win.timeOnFlip(bottomLeft, 'tStopRefresh')  # time at next scr refresh
                bottomLeft.setAutoDraw(False)
        
        # *topRight* updates
        if topRight.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            topRight.frameNStart = frameN  # exact frame index
            topRight.tStart = t  # local t and not account for scr refresh
            topRight.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(topRight, 'tStartRefresh')  # time at next scr refresh
            topRight.setAutoDraw(True)
        if topRight.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > topRight.tStartRefresh + 7-frameTolerance:
                # keep track of stop time/frame for later
                topRight.tStop = t  # not accounting for scr refresh
                topRight.frameNStop = frameN  # exact frame index
                win.timeOnFlip(topRight, 'tStopRefresh')  # time at next scr refresh
                topRight.setAutoDraw(False)
        
        # *bottomRight* updates
        if bottomRight.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            bottomRight.frameNStart = frameN  # exact frame index
            bottomRight.tStart = t  # local t and not account for scr refresh
            bottomRight.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(bottomRight, 'tStartRefresh')  # time at next scr refresh
            bottomRight.setAutoDraw(True)
        if bottomRight.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > bottomRight.tStartRefresh + 7-frameTolerance:
                # keep track of stop time/frame for later
                bottomRight.tStop = t  # not accounting for scr refresh
                bottomRight.frameNStop = frameN  # exact frame index
                win.timeOnFlip(bottomRight, 'tStopRefresh')  # time at next scr refresh
                bottomRight.setAutoDraw(False)
        
        # *Pfeile* updates
        if Pfeile.status == NOT_STARTED and tThisFlip >= 3.0-frameTolerance:
            # keep track of start time/frame for later
            Pfeile.frameNStart = frameN  # exact frame index
            Pfeile.tStart = t  # local t and not account for scr refresh
            Pfeile.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Pfeile, 'tStartRefresh')  # time at next scr refresh
            Pfeile.setAutoDraw(True)
        if Pfeile.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Pfeile.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                Pfeile.tStop = t  # not accounting for scr refresh
                Pfeile.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Pfeile, 'tStopRefresh')  # time at next scr refresh
                Pfeile.setAutoDraw(False)
        # *mouse_resp* updates
        if mouse_resp.status == NOT_STARTED and t >= 3.0-frameTolerance:
            # keep track of start time/frame for later
            mouse_resp.frameNStart = frameN  # exact frame index
            mouse_resp.tStart = t  # local t and not account for scr refresh
            mouse_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse_resp, 'tStartRefresh')  # time at next scr refresh
            mouse_resp.status = STARTED
            prevButtonState = mouse_resp.getPressed()  # if button is down already this ISN'T a new click
        if mouse_resp.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > mouse_resp.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                mouse_resp.tStop = t  # not accounting for scr refresh
                mouse_resp.frameNStop = frameN  # exact frame index
                win.timeOnFlip(mouse_resp, 'tStopRefresh')  # time at next scr refresh
                mouse_resp.status = FINISHED
        if mouse_resp.status == STARTED:  # only update if started and not finished!
            buttons = mouse_resp.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    try:
                        iter([topRight, topLeft, bottomRight, bottomLeft])
                        clickableList = [topRight, topLeft, bottomRight, bottomLeft]
                    except:
                        clickableList = [[topRight, topLeft, bottomRight, bottomLeft]]
                    for obj in clickableList:
                        if obj.contains(mouse_resp):
                            gotValidClick = True
                            mouse_resp.clicked_name.append(obj.name)
                    x, y = mouse_resp.getPos()
                    mouse_resp.x.append(x)
                    mouse_resp.y.append(y)
                    buttons = mouse_resp.getPressed()
                    mouse_resp.leftButton.append(buttons[0])
                    mouse_resp.midButton.append(buttons[1])
                    mouse_resp.rightButton.append(buttons[2])
                    mouse_resp.time.append(mouse_resp.mouseClock.getTime())
                    
                    continueRoutine = False  # abort routine on response
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in AbfrageComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Abfrage"-------
    for thisComponent in AbfrageComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('CueFigure.started', CueFigure.tStartRefresh)
    trials.addData('CueFigure.stopped', CueFigure.tStopRefresh)
    trials.addData('topLeft.started', topLeft.tStartRefresh)
    trials.addData('topLeft.stopped', topLeft.tStopRefresh)
    trials.addData('bottomLeft.started', bottomLeft.tStartRefresh)
    trials.addData('bottomLeft.stopped', bottomLeft.tStopRefresh)
    trials.addData('topRight.started', topRight.tStartRefresh)
    trials.addData('topRight.stopped', topRight.tStopRefresh)
    trials.addData('bottomRight.started', bottomRight.tStartRefresh)
    trials.addData('bottomRight.stopped', bottomRight.tStopRefresh)
    trials.addData('Pfeile.started', Pfeile.tStartRefresh)
    trials.addData('Pfeile.stopped', Pfeile.tStopRefresh)
    # store data for trials (TrialHandler)
    trials.addData('mouse_resp.x', mouse_resp.x)
    trials.addData('mouse_resp.y', mouse_resp.y)
    trials.addData('mouse_resp.leftButton', mouse_resp.leftButton)
    trials.addData('mouse_resp.midButton', mouse_resp.midButton)
    trials.addData('mouse_resp.rightButton', mouse_resp.rightButton)
    trials.addData('mouse_resp.time', mouse_resp.time)
    trials.addData('mouse_resp.clicked_name', mouse_resp.clicked_name)
    trials.addData('mouse_resp.started', mouse_resp.tStart)
    trials.addData('mouse_resp.stopped', mouse_resp.tStop)
    
    # ------Prepare to start Routine "ISIs"-------
    continueRoutine = True
    # update component parameters for each repeat
    jitter = random() * 3.3 + 1.7
    jitter = round(jitter, 1)
    thisExp.addData('jitter',jitter)
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
    trials.addData('Fixation.started', Fixation.tStartRefresh)
    trials.addData('Fixation.stopped', Fixation.tStopRefresh)
    # the Routine "ISIs" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials'


# ------Prepare to start Routine "VielenDank"-------
continueRoutine = True
routineTimer.add(2.000000)
# update component parameters for each repeat
# keep track of which components have finished
VielenDankComponents = [Ende]
for thisComponent in VielenDankComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
VielenDankClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "VielenDank"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = VielenDankClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=VielenDankClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Ende* updates
    if Ende.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Ende.frameNStart = frameN  # exact frame index
        Ende.tStart = t  # local t and not account for scr refresh
        Ende.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Ende, 'tStartRefresh')  # time at next scr refresh
        Ende.setAutoDraw(True)
    if Ende.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > Ende.tStartRefresh + 2-frameTolerance:
            # keep track of stop time/frame for later
            Ende.tStop = t  # not accounting for scr refresh
            Ende.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Ende, 'tStopRefresh')  # time at next scr refresh
            Ende.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in VielenDankComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "VielenDank"-------
for thisComponent in VielenDankComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('Ende.started', Ende.tStartRefresh)
thisExp.addData('Ende.stopped', Ende.tStopRefresh)

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
if eyetracker:
    eyetracker.setConnectionState(False)
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
