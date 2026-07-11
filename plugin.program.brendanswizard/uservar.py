import xbmcaddon
import os

#########################################################
#         Global Variables - DON'T EDIT!!!              #
#########################################################
ADDON_ID = xbmcaddon.Addon().getAddonInfo('id')
PATH = xbmcaddon.Addon().getAddonInfo('path')
ART = os.path.join(PATH, 'resources', 'media')
#########################################################

#########################################################
#        User Edit Variables                            #
#########################################################
ADDONTITLE = '[COLOR gold][B]Brendans[/B][/COLOR] Wizard'
BUILDERNAME = 'Brendans Wizard'
EXCLUDES = [ADDON_ID, 'repository.brendansbuild']
BUILDFILE = 'https://user805643.github.io/BrendansBuild/builds/builds.txt'
UPDATECHECK = 0
APKFILE = 'http://'
YOUTUBETITLE = ''
YOUTUBEFILE = 'http://'
ADDONFILE = 'http://'
ADVANCEDFILE = 'http://'
#########################################################

#########################################################
#        Theming Menu Items                             #
#########################################################
ICONBUILDS = os.path.join(ART, 'builds.png')
ICONMAINT = os.path.join(ART, 'maintenance.png')
ICONSPEED = os.path.join(ART, 'speed.png')
ICONAPK = os.path.join(ART, 'apkinstaller.png')
ICONADDONS = os.path.join(ART, 'addoninstaller.png')
ICONYOUTUBE = os.path.join(ART, 'youtube.png')
ICONSAVE = os.path.join(ART, 'savedata.png')
ICONTRAKT = os.path.join(ART, 'keeptrakt.png')
ICONREAL = os.path.join(ART, 'keepdebrid.png')
ICONLOGIN = os.path.join(ART, 'keeplogin.png')
ICONCONTACT = os.path.join(ART, 'information.png')
ICONSETTINGS = os.path.join(ART, 'settings.png')
HIDESPACERS = 'No'
SPACER = '='

COLOR1 = 'gold'
COLOR2 = 'white'
THEME1 = u'[COLOR {color1}][I]([COLOR {color1}][B]Brendans[/B][/COLOR][COLOR {color2}] Wizard[COLOR {color1}])[/I][/COLOR] [COLOR {color2}]{{}}[/COLOR]'.format(color1=COLOR1, color2=COLOR2)
THEME2 = u'[COLOR {color1}]{{}}[/COLOR]'.format(color1=COLOR1)
THEME3 = u'[COLOR {color1}]{{}}[/COLOR]'.format(color1=COLOR1)
THEME4 = u'[COLOR {color1}]Current Build:[/COLOR] [COLOR {color2}]{{}}[/COLOR]'.format(color1=COLOR1, color2=COLOR2)
THEME5 = u'[COLOR {color1}]Current Theme:[/COLOR] [COLOR {color2}]{{}}[/COLOR]'.format(color1=COLOR1, color2=COLOR2)

HIDECONTACT = 'No'
CONTACT = 'Thank you for choosing Brendans Wizard.\n\nRepository: https://user805643.github.io/BrendansBuild/'
CONTACTICON = os.path.join(ART, 'qricon.png')
CONTACTFANART = 'http://'
#########################################################

#########################################################
#        Auto Update For Those With No Repo             #
#########################################################
AUTOUPDATE = 'Yes'
#########################################################

#########################################################
#        Auto Install Repo If Not Installed             #
#########################################################
AUTOINSTALL = 'Yes'
REPOID = 'repository.brendansbuild'
REPOADDONXML = 'https://raw.githubusercontent.com/user805643/BrendansBuild/main/addons.xml'
REPOZIPURL = 'https://raw.githubusercontent.com/user805643/BrendansBuild/main/zips/repository.brendansbuild/'
#########################################################

#########################################################
#        Notification Window                            #
#########################################################
ENABLE = 'Yes'
NOTIFICATION = 'http://'
HEADERTYPE = 'Text'
FONTHEADER = 'Font14'
HEADERMESSAGE = '[COLOR gold][B]Brendans[/B][/COLOR] Wizard'
HEADERIMAGE = 'http://'
FONTSETTINGS = 'Font13'
BACKGROUND = 'http://'
#########################################################