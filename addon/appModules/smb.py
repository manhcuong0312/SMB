#Small add-on to make the main windows of Sao Mai Braille program accessible to NVDA
#Copyright 2022 - 2025 by Sao Mai technology team
import appModuleHandler
import NVDAObjects.window
import keyboardHandler #use to send keystroke to SMB program
import time
import scriptHandler
from scriptHandler import script
#from core import callLater
import ui #test and debug

# the next two lines make this add-on translatable
import addonHandler
addonHandler.initTranslation()


class AppModule(appModuleHandler.AppModule):
           
    def event_gainFocus(self, obj, nextHandler):
        NVDAObjects.window.windowClassMap['TSRichViewEdit']='Edit'
        NVDAObjects.window.windowClassMap['TSRVRichViewEdit']='Edit'
        NVDAObjects.window.windowClassMap['TSRVRichViewHeaderFooterEdit']='Edit'
        NVDAObjects.window.windowClassMap['TSRVRichViewNoteEdit']='Edit'
        NVDAObjects.window.windowClassMap['TDBSRichViewEdit']='Edit'
        NVDAObjects.window.windowClassMap['TInnerDBRichViewEdit']='Edit'
        NVDAObjects.window.windowClassMap['TDBSRVRichViewHeaderFooterEdit']='Edit'
        NVDAObjects.window.windowClassMap['TDBSRVRichViewNoteEdit']='Edit'
        nextHandler()

    @script(
    # Translators: Describes the Insert equation dialog.
        description = _("Call Insert equation dialog the old way."),
        gesture = "kb:alt+f9")
        
    def script_InsertEquation (self, gesture):
        time.sleep(0.5)
        keyboardHandler.KeyboardInputGesture.fromName("control+shift+q").send()
        #ui.message ("Insert equation") #debug

    @script(
    # Translators: Describes the Insert picture dialog.
        description = _("Call Insert picture dialog the old way."),
        gesture = "kb:alt+f10")

    def script_InsertPicture (self, gesture):
        time.sleep(0.5)
        keyboardHandler.KeyboardInputGesture.fromName("control+shift+g").send()
        #ui.message ("Insert equation") #debug
        
    @script(
    # Translators: Describes the Insert Music Score  dialog.
        description = _("Call Insert Music Score  dialog the old way."),
        gesture = "kb:alt+f11")

    def script_InsertMusicScore (self, gesture):
        time.sleep(0.5)
        keyboardHandler.KeyboardInputGesture.fromName("control+shift+m").send()
        #ui.message ("Insert equation") #debug