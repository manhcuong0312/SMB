#Small add-on to make the main windows of Sao Mai Braille program accessible to NVDA
#Written by Sao Mai technology team
import appModuleHandler
import NVDAObjects.window
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