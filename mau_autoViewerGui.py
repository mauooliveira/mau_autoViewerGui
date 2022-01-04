#--------------------------------------------------
# mau_autoViewerGui.py
# version: 2.0.0
# last updated: 04.01.22 (DD.MM.YY)
#--------------------------------------------------

import nuke

def autoViewerGui():
    #FOR EACH SELECTED NODE
    for i in nuke.selectedNodes():
        #EVALUATE CLASS
        if i.Class() == "Switch":
            #BEING A SWITCH SET/REMOVE EXPRESSION ON THE WHICH KNOB
            a = i.knob("which").hasExpression()
            if a == True:
                k = i.knob("which")
                k.setAnimated()
                k.setValue(0)
                k.clearAnimated()
            else:
                i.knob("which").setExpression('[python {1-nuke.executing()}]')
        #IF IS A VIEWER JUST PASS        
        elif i.Class() == "Viewer":
            pass
        #IF ANY OTHER TYPE OF NODE SET/REMOVE EXPRESSION TO THE DISABLE KNOB
        else:
            a = i.knob("disable").isAnimated()
            if a == True:
                i.knob("disable").clearAnimated()
                i.knob("disable").setValue(False)
            else:
                i.knob("disable").setExpression('[python {1-nuke.executing()}]')
