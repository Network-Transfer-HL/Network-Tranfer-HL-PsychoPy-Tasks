#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.1.1),
    on Wed Mar 16 21:05:43 2022
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
expName = 'Lernen_FPA'  # from the Builder filename that created this script
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
    originPath='/Users/charlotte/Desktop/DOCUMENTS/UNI/MEDIZIN/PROMOTION/Behaviour/PsychoPy/Adaptation/FPA_Adaptation/Lernen_FPA_Adaptation_lastrun.py',
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

# Initialize components for Routine "StartLernphase"
StartLernphaseClock = core.Clock()
Wilkommen = visual.TextStim(win=win, name='Wilkommen',
    text='Herzlich Willkommen!\n\nIn der folgenden Lernphase werden Ihnen 6 gepaarte Figuren mit Pausen dazwischen präsentiert. Nach der Hälfte haben Sie eine kleine Pause.\n\nBitte versuchen Sie sich möglichst viele Figurenpaare zu merken.\nEs ist hilfreich, die unsinnigen Figuren mit Ihnen vertrauten Bilddarstellungen zu verbinden.\n\nUm die Lernphase zu starten, drücken Sie bitte die Maustaste.\n\nViel Erfolg!',
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
Kreuz = visual.ImageStim(
    win=win,
    name='Kreuz', 
    image='Kreuz.png', mask=None, anchor='center',
    ori=0, pos=(0, 0), size=(0.15, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Initialize components for Routine "FigurePairedPresentation"
FigurePairedPresentationClock = core.Clock()
FigureA = visual.ImageStim(
    win=win,
    name='FigureA', 
    image='sin', mask=None, anchor='center',
    ori=0, pos=(-0.4, 0), size=(0.63, 0.382),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=0.0)
FigureB = visual.ImageStim(
    win=win,
    name='FigureB', 
    image='sin', mask=None, anchor='center',
    ori=0, pos=(0.4, 0), size=(0.63, 0.382),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-1.0)

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

# Initialize components for Routine "FigurePairedPresentation"
FigurePairedPresentationClock = core.Clock()
FigureA = visual.ImageStim(
    win=win,
    name='FigureA', 
    image='sin', mask=None, anchor='center',
    ori=0, pos=(-0.4, 0), size=(0.63, 0.382),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=0.0)
FigureB = visual.ImageStim(
    win=win,
    name='FigureB', 
    image='sin', mask=None, anchor='center',
    ori=0, pos=(0.4, 0), size=(0.63, 0.382),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-1.0)

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
                
                continueRoutine = False  # abort routine on response
    
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
thisExp.addData('mouse.x', mouse.x)
thisExp.addData('mouse.y', mouse.y)
thisExp.addData('mouse.leftButton', mouse.leftButton)
thisExp.addData('mouse.midButton', mouse.midButton)
thisExp.addData('mouse.rightButton', mouse.rightButton)
thisExp.addData('mouse.time', mouse.time)
thisExp.addData('mouse.started', mouse.tStart)
thisExp.addData('mouse.stopped', mouse.tStop)
thisExp.nextEntry()
# the Routine "StartLernphase" was not non-slip safe, so reset the non-slip timer
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
trials = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('FPA_Lernen_Stimulus_List.xlsx', selection='0:6'),
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
    
    # ------Prepare to start Routine "FigurePairedPresentation"-------
    continueRoutine = True
    routineTimer.add(3.000000)
    # update component parameters for each repeat
    FigureA.setImage(Cue)
    FigureB.setImage(Target)
    # keep track of which components have finished
    FigurePairedPresentationComponents = [FigureA, FigureB]
    for thisComponent in FigurePairedPresentationComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    FigurePairedPresentationClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "FigurePairedPresentation"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = FigurePairedPresentationClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=FigurePairedPresentationClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *FigureA* updates
        if FigureA.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            FigureA.frameNStart = frameN  # exact frame index
            FigureA.tStart = t  # local t and not account for scr refresh
            FigureA.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(FigureA, 'tStartRefresh')  # time at next scr refresh
            FigureA.setAutoDraw(True)
        if FigureA.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > FigureA.tStartRefresh + 3.0-frameTolerance:
                # keep track of stop time/frame for later
                FigureA.tStop = t  # not accounting for scr refresh
                FigureA.frameNStop = frameN  # exact frame index
                win.timeOnFlip(FigureA, 'tStopRefresh')  # time at next scr refresh
                FigureA.setAutoDraw(False)
        
        # *FigureB* updates
        if FigureB.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            FigureB.frameNStart = frameN  # exact frame index
            FigureB.tStart = t  # local t and not account for scr refresh
            FigureB.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(FigureB, 'tStartRefresh')  # time at next scr refresh
            FigureB.setAutoDraw(True)
        if FigureB.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > FigureB.tStartRefresh + 3.0-frameTolerance:
                # keep track of stop time/frame for later
                FigureB.tStop = t  # not accounting for scr refresh
                FigureB.frameNStop = frameN  # exact frame index
                win.timeOnFlip(FigureB, 'tStopRefresh')  # time at next scr refresh
                FigureB.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in FigurePairedPresentationComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "FigurePairedPresentation"-------
    for thisComponent in FigurePairedPresentationComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('FigureA.started', FigureA.tStartRefresh)
    trials.addData('FigureA.stopped', FigureA.tStopRefresh)
    trials.addData('FigureB.started', FigureB.tStartRefresh)
    trials.addData('FigureB.stopped', FigureB.tStopRefresh)
    
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


# ------Prepare to start Routine "FigurePairedPresentation"-------
continueRoutine = True
routineTimer.add(3.000000)
# update component parameters for each repeat
FigureA.setImage(Cue)
FigureB.setImage(Target)
# keep track of which components have finished
FigurePairedPresentationComponents = [FigureA, FigureB]
for thisComponent in FigurePairedPresentationComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
FigurePairedPresentationClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "FigurePairedPresentation"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = FigurePairedPresentationClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=FigurePairedPresentationClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *FigureA* updates
    if FigureA.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        FigureA.frameNStart = frameN  # exact frame index
        FigureA.tStart = t  # local t and not account for scr refresh
        FigureA.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(FigureA, 'tStartRefresh')  # time at next scr refresh
        FigureA.setAutoDraw(True)
    if FigureA.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > FigureA.tStartRefresh + 3.0-frameTolerance:
            # keep track of stop time/frame for later
            FigureA.tStop = t  # not accounting for scr refresh
            FigureA.frameNStop = frameN  # exact frame index
            win.timeOnFlip(FigureA, 'tStopRefresh')  # time at next scr refresh
            FigureA.setAutoDraw(False)
    
    # *FigureB* updates
    if FigureB.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        FigureB.frameNStart = frameN  # exact frame index
        FigureB.tStart = t  # local t and not account for scr refresh
        FigureB.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(FigureB, 'tStartRefresh')  # time at next scr refresh
        FigureB.setAutoDraw(True)
    if FigureB.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > FigureB.tStartRefresh + 3.0-frameTolerance:
            # keep track of stop time/frame for later
            FigureB.tStop = t  # not accounting for scr refresh
            FigureB.frameNStop = frameN  # exact frame index
            win.timeOnFlip(FigureB, 'tStopRefresh')  # time at next scr refresh
            FigureB.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in FigurePairedPresentationComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "FigurePairedPresentation"-------
for thisComponent in FigurePairedPresentationComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('FigureA.started', FigureA.tStartRefresh)
thisExp.addData('FigureA.stopped', FigureA.tStopRefresh)
thisExp.addData('FigureB.started', FigureB.tStartRefresh)
thisExp.addData('FigureB.stopped', FigureB.tStopRefresh)

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
thisExp.addData('Fixation.started', Fixation.tStartRefresh)
thisExp.addData('Fixation.stopped', Fixation.tStopRefresh)
# the Routine "ISIs" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

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
if eyetracker:
    eyetracker.setConnectionState(False)
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
