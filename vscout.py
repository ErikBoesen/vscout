#!/usr/bin/env python3

import npyscreen

class VictisTheme(npyscreen.ThemeManager):
    default_colors = {
        'DEFAULT'     : 'WHITE_BLACK',
        'FORMDEFAULT' : 'WHITE_BLACK',
        'NO_EDIT'     : 'BLUE_BLACK',
        'STANDOUT'    : 'CYAN_BLACK',
        'CURSOR'      : 'WHITE_BLACK',
        'CURSOR_INVERSE': 'BLACK_WHITE',
        'LABEL'       : 'RED_BLACK',
        'LABELBOLD'   : 'WHITE_BLACK',
        'CONTROL'     : 'YELLOW_BLACK',
        'IMPORTANT'   : 'GREEN_BLACK',
        'SAFE'        : 'GREEN_BLACK',
        'WARNING'     : 'YELLOW_BLACK',
        'DANGER'      : 'RED_BLACK',
        'CRITICAL'    : 'BLACK_RED',
        'GOOD'        : 'GREEN_BLACK',
        'GOODHL'      : 'GREEN_BLACK',
        'VERYGOOD'    : 'BLACK_GREEN',
        'CAUTION'     : 'YELLOW_BLACK',
        'CAUTIONHL'   : 'BLACK_YELLOW',
    }

class VictiScout(npyscreen.NPSAppManaged):

    def main(self):
        npyscreen.setTheme(VictisTheme)
        self.form = npyscreen.Form(name='VictiScout',)
        self.special = {
            'team': self.form.add(npyscreen.TitleText, name='Team #'),
            # TODO: This might make sense as a slider if it actually adjusted its end to match the number of matches in the competition, but it would need WiFi.
            'match': self.form.add(npyscreen.TitleSlider, name='Match #'),
            'alliance': self.form.add(npyscreen.TitleSelectOne, name='Alliance', values=['Red', 'Blue'], max_height=3, scroll_exit=True),
            'start-position': self.form.add(npyscreen.TitleSelectOne, name='Start', values=['Left', 'Center', 'Right'], max_height=4, scroll_exit=True),
        }
        self.controls = {
            'submit': self.form.add(npyscreen.Button, name='Submit'),
        }
        self.inputs = {
            'auto-line': self.form.add(npyscreen.Checkbox, name='AUTO Crossed Line'),
            # TODO: These really shouldn't be sliders.
            'auto-scale': self.form.add(npyscreen.TitleSlider, out_of=8, name='AUTO Scale Cubes'),
            'auto-switch': self.form.add(npyscreen.TitleSlider, out_of=8, name='AUTO Switch Cubes'),

            'scale': self.form.add(npyscreen.TitleSlider, out_of=16, name='Scale Cubes'),
            'switch': self.form.add(npyscreen.TitleSlider, out_of=16, name='Switch Cubes'),
            'opposition-switch': self.form.add(npyscreen.TitleSlider, out_of=16, name='Opposition Switch Cubes'),
            'vault': self.form.add(npyscreen.TitleSlider, out_of=10, name='Vault Cubes'),
            'climbed': self.form.add(npyscreen.Checkbox, name='Climbed?'),
            'climb-assists': self.form.add(npyscreen.TitleSlider, out_of=2, name='Climb assists'),

            # TODO: Full advice
            'notes': self.form.add(npyscreen.TitleMultiLine, name='Notes'),
        }
        """text = self.form.add(npyscreen.TitleText, name="Text:",)
        filename = self.form.add(npyscreen.TitleFilename, name="Filename:")
        filename_title = self.form.add(npyscreen.TitleFilenameCombo, name="Filename2:")
        date = self.form.add(npyscreen.TitleDateCombo, name="Date:")
        slider = self.form.add(npyscreen.TitleSlider, out_of=12, name="Slider")
        multiline = self.form.add(npyscreen.MultiLineEdit,
                             value="try typing here!\nMutiline text, press ^R to reself.format.\n",
                             max_height=5, rely=9)
        radio = self.form.add(npyscreen.TitleSelectOne, max_height=4, value=[1,], name="Pick One",
                         values=["Option1","Option2","Option3"], scroll_exit=True)
        multiselect = self.form.add(npyscreen.TitleMultiSelect, max_height =-2, value=[1,], name="Pick Several",
                               values=["Option1","Option2","Option3"], scroll_exit=True)
        """

        # This lets the user interact with the Form.
        self.form.edit()

if __name__ == "__main__":
    vs = VictiScout()
    vs.run()
