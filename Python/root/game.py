#Add import
import uifastequip #if this give you error try import uiFastEquip

#Find onPressKeyDict[app.DIK_F1] and add
onPressKeyDict[app.DIK_F7]    = lambda : self.__quikeqchange() #Change F7 if u want.

#Add in the end of game.py
    def __quikeqchange(self):
        import uifastequip
        self.uuifastequipDlg = uifastequip.changeequip()
        self.uuifastequipDlg.Show()
