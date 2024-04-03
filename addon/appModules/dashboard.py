#appModules/dashboard.py
# Ein Teil von NonVisual Desktop Access (NVDA)
# Copyright (C) 2006-2024 NVDA Mitwirkende
# Diese Datei unterliegt der GNU General Public License.
# Weitere Informationen finden Sie in der Datei COPYING.
import appModuleHandler
import controlTypes
import api
from scriptHandler import script
import addonHandler
from NVDAObjects.UIA import ListItem, UIA
# Entfernen Sie das Kommentarzeichen (#) aus der nächsten Zeile, wenn (und sobald) die Datei zu einem Addon gehört. Dadurch werden Lokalisierungsfunktionen (Übersetzungsfunktionen) in Ihrer Datei aktiviert. Weitere Informationen finden Sie im Entwicklungshandbuch für NVDA-Addons.
#addonHandler.initTranslation()
class cyberghost_fav(UIA):
	def _get_name(self):
		l = list()
		for x in self.children:
			if x.name != "":
				l.append(x.name)
		return "; ".join(l)

class cyberghost_listitem(ListItem):
	def _get_name(self):
		l = list()
		for x in self.children:
			if x.name != "":
				l.append(x.name)
		return "; ".join(l)
class AppModule(appModuleHandler.AppModule):
	def chooseNVDAObjectOverlayClasses(self, obj, clslist):
		if obj.name in  ["CyberGhost.VPN.App", "CyberGhost.VPN.Classes.API.Manager.ServerManager.ServerItems.FavoriteItem"]:
			clslist.insert(0,cyberghost_listitem)
		if obj.UIAElement.CurrentClassName == 'DataGridCell':
			clslist.insert(0,cyberghost_fav)


