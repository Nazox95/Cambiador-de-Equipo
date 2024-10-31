#Now take care, maybe you have other side bar, in this tut i was used a random side bar
#but you need find the sidebar class.
#Find your class Sidebar like
class SystemsWindow(ui.ScriptWindow):
#below others functions add
 self.Equipo2 = self.GetChild("Equipo")
#like this
class SystemsWindow(ui.ScriptWindow):
						[..]
						self.expandBtn = self.GetChild("ExpandBtn")
            self.minBtn = self.GetChild("MinimizeBtn")
            self.Clima2 = self.GetChild("Clima")
            self.Calendario2 = self.GetChild("Calendario")
            self.Equipo2 = self.GetChild("Equipo")
            self.Gremio2 = self.GetChild("Gremio")
            self.Nazox2 = self.GetChild("Nazox")

#Not in the same function few lines after add
						self.Equipo2.SetEvent(ui.__mem_func__(self._Equipo2))
#Like
						[...]
            self.expandBtn.SetEvent(ui.__mem_func__(self.OpenInventory))
            self.minBtn.SetEvent(ui.__mem_func__(self.CloseInventory))
            self.Equipo2.SetEvent(ui.__mem_func__(self._Equipo2))
            self.Gremio2.SetEvent(ui.__mem_func__(self._Gremio2))
            self.Nazox2.SetEvent(ui.__mem_func__(self._Nazox2))

#Now after add with others def
    def _Equipo2(self):
        import uifastequip
        self.uuifastequipDlg = uifastequip.changeequip()
        self.uuifastequipDlg.Show()

#Like this
		[...]
    def _Gremio2(self):
        import constInfo
        net.SendChatPacket("/blablaba")    

    def _Equipo2(self):
        import uifastequip
        self.uuifastequipDlg = uifastequip.changeequip()
        self.uuifastequipDlg.Show()
