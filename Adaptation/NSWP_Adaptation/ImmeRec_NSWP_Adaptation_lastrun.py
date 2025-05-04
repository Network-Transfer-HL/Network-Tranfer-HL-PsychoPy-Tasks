#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.1.1),
    on Wed Mar 16 21:16:14 2022
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
expName = 'ImmediateRecall_NSWP'  # from the Builder filename that created this script
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
    originPath='/Users/charlotte/Desktop/DOCUMENTS/UNI/MEDIZIN/PROMOTION/Behaviour/PsychoPy/Adaptation/NSWP_Adaptation/ImmeRec_NSWP_Adaptation_lastrun.py',
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
    text='Im Folgenden wird Ihnen für sieben Sekunden auf der linken Seite des Bildschirms ein Wort gezeigt.\n\nAuf der rechten Seite werden vier Antwortmöglichkeiten zu sehen sein. \n\n-> Weiter mit einem Mausklick',
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
    text='Bitte antworten Sie immer erst, wenn die Pfeile zwischen den Antwortmöglichkeiten auftauchen.\nSie haben dann noch 4 Sekunden um mit einem Mausklick das korrekte Wortpaar aus der Lernphase zu vervollständigen.\n\nNach Ihrer Antwort wird Ihnen das richtige Wortpaar angezeigt.\n\nZwischen den Aufgaben wird es kurze Pausen geben.\n\n-> Weiter mit einem Mausklick',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
mouseNext3 = event.Mouse(win=win)
x, y = [None, None]
mouseNext3.mouseClock = core.Clock()

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
Pfeile = visual.ImageStim(
    win=win,
    name='Pfeile', 
    image='Pfeile.png', mask=None, anchor='center',
    ori=45, pos=(0.35, 0), size=(0.315, 0.191),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=0.0)
mouse_resp = event.Mouse(win=win)
x, y = [None, None]
mouse_resp.mouseClock = core.Clock()
Stim_Background = visual.ImageStim(
    win=win,
    name='Stim_Background', 
    image='white.png', mask=None, anchor='center',
    ori=0, pos=(-0.5, 0), size=(0.4, 0.24),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-2.0)
topLeft = visual.ImageStim(
    win=win,
    name='topLeft', 
    image='white.png', mask=None, anchor='center',
    ori=0, pos=(0.1, 0.2), size=(0.4, 0.24),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-3.0)
bottomLeft = visual.ImageStim(
    win=win,
    name='bottomLeft', 
    image='white.png', mask=None, anchor='center',
    ori=0, pos=(0.1, -0.2), size=(0.4, 0.24),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-4.0)
topRight = visual.ImageStim(
    win=win,
    name='topRight', 
    image='white.png', mask=None, anchor='center',
    ori=0, pos=(0.6, 0.2), size=(0.4, 0.24),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-5.0)
bottomRight = visual.ImageStim(
    win=win,
    name='bottomRight', 
    image='white.png', mask=None, anchor='center',
    ori=0, pos=(0.6, -0.2), size=(0.4, 0.24),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-6.0)
Stimulus = visual.TextStim(win=win, name='Stimulus',
    text='',
    font='Arial',
    pos=(-0.5, 0), height=0.07, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-7.0);
topLeftTxt = visual.TextStim(win=win, name='topLeftTxt',
    text='',
    font='Arial',
    pos=(0.1, 0.2), height=0.07, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-8.0);
bottomLeftTxt = visual.TextStim(win=win, name='bottomLeftTxt',
    text='',
    font='Arial',
    pos=(0.1, -0.2), height=0.07, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-9.0);
topRightTxt = visual.TextStim(win=win, name='topRightTxt',
    text='',
    font='Arial',
    pos=(0.6, 0.2), height=0.07, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-10.0);
bottomRightTxt = visual.TextStim(win=win, name='bottomRightTxt',
    text='',
    font='Arial',
    pos=(0.6, -0.2), height=0.07, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-11.0);

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

# Initialize components for Routine "Correct"
CorrectClock = core.Clock()
Cue_Background = visual.ImageStim(
    win=win,
    name='Cue_Background', 
    image='white.png', mask=None, anchor='center',
    ori=0, pos=(-0.4, 0), size=(0.63, 0.382),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=0.0)
Target_Background = visual.ImageStim(
    win=win,
    name='Target_Background', 
    image='white.png', mask=None, anchor='center',
    ori=0, pos=(0.4, 0), size=(0.63, 0.382),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-1.0)
CueWord = visual.TextStim(win=win, name='CueWord',
    text='',
    font='Arial',
    pos=(-0.4, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
TargetWord = visual.TextStim(win=win, name='TargetWord',
    text='',
    font='Arial',
    pos=(0.4, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);

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
gotValidClick = False  # until a click is received
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
thisExp.addData('mouseNext.started', mouseNext.tStart)
thisExp.addData('mouseNext.stopped', mouseNext.tStop)
thisExp.nextEntry()
# the Routine "Anleitung1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Anleitung2"-------
continueRoutine = True
# update component parameters for each repeat
# setup some python lists for storing info about the mouseNext3
gotValidClick = False  # until a click is received
# keep track of which components have finished
Anleitung2Components = [Anleitungstext2, mouseNext3]
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
    # *mouseNext3* updates
    if mouseNext3.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mouseNext3.frameNStart = frameN  # exact frame index
        mouseNext3.tStart = t  # local t and not account for scr refresh
        mouseNext3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mouseNext3, 'tStartRefresh')  # time at next scr refresh
        mouseNext3.status = STARTED
        prevButtonState = mouseNext3.getPressed()  # if button is down already this ISN'T a new click
    if mouseNext3.status == STARTED:  # only update if started and not finished!
        buttons = mouseNext3.getPressed()
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
thisExp.addData('mouseNext3.started', mouseNext3.tStart)
thisExp.addData('mouseNext3.stopped', mouseNext3.tStop)
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
    trialList=data.importConditions('NSWP_ImmRec_Stimulus_List.xlsx', selection='0:6'),
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
    Stimulus.setText(Cue)
    topLeftTxt.setText(L1)
    bottomLeftTxt.setText(L2)
    topRightTxt.setText(R1)
    bottomRightTxt.setText(R2)
    # keep track of which components have finished
    AbfrageComponents = [Pfeile, mouse_resp, Stim_Background, topLeft, bottomLeft, topRight, bottomRight, Stimulus, topLeftTxt, bottomLeftTxt, topRightTxt, bottomRightTxt]
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
                        iter([topLeft, bottomLeft, topRight, bottomRight])
                        clickableList = [topLeft, bottomLeft, topRight, bottomRight]
                    except:
                        clickableList = [[topLeft, bottomLeft, topRight, bottomRight]]
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
                    if gotValidClick:
                        continueRoutine = False  # abort routine on response
        
        # *Stim_Background* updates
        if Stim_Background.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Stim_Background.frameNStart = frameN  # exact frame index
            Stim_Background.tStart = t  # local t and not account for scr refresh
            Stim_Background.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Stim_Background, 'tStartRefresh')  # time at next scr refresh
            Stim_Background.setAutoDraw(True)
        if Stim_Background.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Stim_Background.tStartRefresh + 7.0-frameTolerance:
                # keep track of stop time/frame for later
                Stim_Background.tStop = t  # not accounting for scr refresh
                Stim_Background.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Stim_Background, 'tStopRefresh')  # time at next scr refresh
                Stim_Background.setAutoDraw(False)
        
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
            if tThisFlipGlobal > topLeft.tStartRefresh + 7.0-frameTolerance:
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
            if tThisFlipGlobal > bottomLeft.tStartRefresh + 7.0-frameTolerance:
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
            if tThisFlipGlobal > topRight.tStartRefresh + 7.0-frameTolerance:
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
            if tThisFlipGlobal > bottomRight.tStartRefresh + 7.0-frameTolerance:
                # keep track of stop time/frame for later
                bottomRight.tStop = t  # not accounting for scr refresh
                bottomRight.frameNStop = frameN  # exact frame index
                win.timeOnFlip(bottomRight, 'tStopRefresh')  # time at next scr refresh
                bottomRight.setAutoDraw(False)
        
        # *Stimulus* updates
        if Stimulus.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Stimulus.frameNStart = frameN  # exact frame index
            Stimulus.tStart = t  # local t and not account for scr refresh
            Stimulus.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Stimulus, 'tStartRefresh')  # time at next scr refresh
            Stimulus.setAutoDraw(True)
        if Stimulus.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Stimulus.tStartRefresh + 7.0-frameTolerance:
                # keep track of stop time/frame for later
                Stimulus.tStop = t  # not accounting for scr refresh
                Stimulus.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Stimulus, 'tStopRefresh')  # time at next scr refresh
                Stimulus.setAutoDraw(False)
        
        # *topLeftTxt* updates
        if topLeftTxt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            topLeftTxt.frameNStart = frameN  # exact frame index
            topLeftTxt.tStart = t  # local t and not account for scr refresh
            topLeftTxt.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(topLeftTxt, 'tStartRefresh')  # time at next scr refresh
            topLeftTxt.setAutoDraw(True)
        if topLeftTxt.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > topLeftTxt.tStartRefresh + 7.0-frameTolerance:
                # keep track of stop time/frame for later
                topLeftTxt.tStop = t  # not accounting for scr refresh
                topLeftTxt.frameNStop = frameN  # exact frame index
                win.timeOnFlip(topLeftTxt, 'tStopRefresh')  # time at next scr refresh
                topLeftTxt.setAutoDraw(False)
        
        # *bottomLeftTxt* updates
        if bottomLeftTxt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            bottomLeftTxt.frameNStart = frameN  # exact frame index
            bottomLeftTxt.tStart = t  # local t and not account for scr refresh
            bottomLeftTxt.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(bottomLeftTxt, 'tStartRefresh')  # time at next scr refresh
            bottomLeftTxt.setAutoDraw(True)
        if bottomLeftTxt.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > bottomLeftTxt.tStartRefresh + 7.0-frameTolerance:
                # keep track of stop time/frame for later
                bottomLeftTxt.tStop = t  # not accounting for scr refresh
                bottomLeftTxt.frameNStop = frameN  # exact frame index
                win.timeOnFlip(bottomLeftTxt, 'tStopRefresh')  # time at next scr refresh
                bottomLeftTxt.setAutoDraw(False)
        
        # *topRightTxt* updates
        if topRightTxt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            topRightTxt.frameNStart = frameN  # exact frame index
            topRightTxt.tStart = t  # local t and not account for scr refresh
            topRightTxt.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(topRightTxt, 'tStartRefresh')  # time at next scr refresh
            topRightTxt.setAutoDraw(True)
        if topRightTxt.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > topRightTxt.tStartRefresh + 7.0-frameTolerance:
                # keep track of stop time/frame for later
                topRightTxt.tStop = t  # not accounting for scr refresh
                topRightTxt.frameNStop = frameN  # exact frame index
                win.timeOnFlip(topRightTxt, 'tStopRefresh')  # time at next scr refresh
                topRightTxt.setAutoDraw(False)
        
        # *bottomRightTxt* updates
        if bottomRightTxt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            bottomRightTxt.frameNStart = frameN  # exact frame index
            bottomRightTxt.tStart = t  # local t and not account for scr refresh
            bottomRightTxt.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(bottomRightTxt, 'tStartRefresh')  # time at next scr refresh
            bottomRightTxt.setAutoDraw(True)
        if bottomRightTxt.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > bottomRightTxt.tStartRefresh + 7.0-frameTolerance:
                # keep track of stop time/frame for later
                bottomRightTxt.tStop = t  # not accounting for scr refresh
                bottomRightTxt.frameNStop = frameN  # exact frame index
                win.timeOnFlip(bottomRightTxt, 'tStopRefresh')  # time at next scr refresh
                bottomRightTxt.setAutoDraw(False)
        
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
    trials.addData('Stim_Background.started', Stim_Background.tStartRefresh)
    trials.addData('Stim_Background.stopped', Stim_Background.tStopRefresh)
    trials.addData('topLeft.started', topLeft.tStartRefresh)
    trials.addData('topLeft.stopped', topLeft.tStopRefresh)
    trials.addData('bottomLeft.started', bottomLeft.tStartRefresh)
    trials.addData('bottomLeft.stopped', bottomLeft.tStopRefresh)
    trials.addData('topRight.started', topRight.tStartRefresh)
    trials.addData('topRight.stopped', topRight.tStopRefresh)
    trials.addData('bottomRight.started', bottomRight.tStartRefresh)
    trials.addData('bottomRight.stopped', bottomRight.tStopRefresh)
    trials.addData('Stimulus.started', Stimulus.tStartRefresh)
    trials.addData('Stimulus.stopped', Stimulus.tStopRefresh)
    trials.addData('topLeftTxt.started', topLeftTxt.tStartRefresh)
    trials.addData('topLeftTxt.stopped', topLeftTxt.tStopRefresh)
    trials.addData('bottomLeftTxt.started', bottomLeftTxt.tStartRefresh)
    trials.addData('bottomLeftTxt.stopped', bottomLeftTxt.tStopRefresh)
    trials.addData('topRightTxt.started', topRightTxt.tStartRefresh)
    trials.addData('topRightTxt.stopped', topRightTxt.tStopRefresh)
    trials.addData('bottomRightTxt.started', bottomRightTxt.tStartRefresh)
    trials.addData('bottomRightTxt.stopped', bottomRightTxt.tStopRefresh)
    
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
    trials.addData('Fixation.started', Fixation.tStartRefresh)
    trials.addData('Fixation.stopped', Fixation.tStopRefresh)
    # the Routine "ISIs" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Correct"-------
    continueRoutine = True
    routineTimer.add(3.000000)
    # update component parameters for each repeat
    CueWord.setText(Cue)
    TargetWord.setText(Target)
    # keep track of which components have finished
    CorrectComponents = [Cue_Background, Target_Background, CueWord, TargetWord]
    for thisComponent in CorrectComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    CorrectClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Correct"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = CorrectClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=CorrectClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Cue_Background* updates
        if Cue_Background.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Cue_Background.frameNStart = frameN  # exact frame index
            Cue_Background.tStart = t  # local t and not account for scr refresh
            Cue_Background.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Cue_Background, 'tStartRefresh')  # time at next scr refresh
            Cue_Background.setAutoDraw(True)
        if Cue_Background.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Cue_Background.tStartRefresh + 3.0-frameTolerance:
                # keep track of stop time/frame for later
                Cue_Background.tStop = t  # not accounting for scr refresh
                Cue_Background.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Cue_Background, 'tStopRefresh')  # time at next scr refresh
                Cue_Background.setAutoDraw(False)
        
        # *Target_Background* updates
        if Target_Background.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Target_Background.frameNStart = frameN  # exact frame index
            Target_Background.tStart = t  # local t and not account for scr refresh
            Target_Background.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Target_Background, 'tStartRefresh')  # time at next scr refresh
            Target_Background.setAutoDraw(True)
        if Target_Background.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Target_Background.tStartRefresh + 3.0-frameTolerance:
                # keep track of stop time/frame for later
                Target_Background.tStop = t  # not accounting for scr refresh
                Target_Background.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Target_Background, 'tStopRefresh')  # time at next scr refresh
                Target_Background.setAutoDraw(False)
        
        # *CueWord* updates
        if CueWord.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            CueWord.frameNStart = frameN  # exact frame index
            CueWord.tStart = t  # local t and not account for scr refresh
            CueWord.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(CueWord, 'tStartRefresh')  # time at next scr refresh
            CueWord.setAutoDraw(True)
        if CueWord.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > CueWord.tStartRefresh + 3.0-frameTolerance:
                # keep track of stop time/frame for later
                CueWord.tStop = t  # not accounting for scr refresh
                CueWord.frameNStop = frameN  # exact frame index
                win.timeOnFlip(CueWord, 'tStopRefresh')  # time at next scr refresh
                CueWord.setAutoDraw(False)
        
        # *TargetWord* updates
        if TargetWord.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            TargetWord.frameNStart = frameN  # exact frame index
            TargetWord.tStart = t  # local t and not account for scr refresh
            TargetWord.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(TargetWord, 'tStartRefresh')  # time at next scr refresh
            TargetWord.setAutoDraw(True)
        if TargetWord.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > TargetWord.tStartRefresh + 3.0-frameTolerance:
                # keep track of stop time/frame for later
                TargetWord.tStop = t  # not accounting for scr refresh
                TargetWord.frameNStop = frameN  # exact frame index
                win.timeOnFlip(TargetWord, 'tStopRefresh')  # time at next scr refresh
                TargetWord.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in CorrectComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Correct"-------
    for thisComponent in CorrectComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('Cue_Background.started', Cue_Background.tStartRefresh)
    trials.addData('Cue_Background.stopped', Cue_Background.tStopRefresh)
    trials.addData('Target_Background.started', Target_Background.tStartRefresh)
    trials.addData('Target_Background.stopped', Target_Background.tStopRefresh)
    trials.addData('CueWord.started', CueWord.tStartRefresh)
    trials.addData('CueWord.stopped', CueWord.tStopRefresh)
    trials.addData('TargetWord.started', TargetWord.tStartRefresh)
    trials.addData('TargetWord.stopped', TargetWord.tStopRefresh)
    
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
