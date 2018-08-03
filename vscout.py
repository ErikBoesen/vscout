#!/usr/bin/env python3

import npyscreen
import os
import json


DATA_PATH = os.getenv('HOME') + '/scoutdata.json'

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
        # TODO: Choose a color other than white for CONTROL
        'CONTROL'     : 'WHITE_BLACK',
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
        self.controls = {
            'submit': self.form.add(npyscreen.ButtonPress, name='Submit', when_pressed_function=self.store),
        }
        # TODO: Reimplement position/alliance selectors to help scouts
        self.inputs = {
            'team': self.form.add(npyscreen.TitleText, name='Team #'),
            # TODO: This might make sense as a slider if it actually adjusted its end to match the number of matches in the competition, but it would need WiFi.
            'match': self.form.add(npyscreen.TitleSlider, name='Match #'),
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
        # TODO: npyscreen's documentation says with NSAppManaged this isn't necessary.
        # If it's removed now, however, the form isn't opened. Need to investigate further.
        self.form.edit()

    def clear(self):
        match = self.inputs['match'].value
        for key in self.inputs.keys():
            self.inputs[key].value = None
        self.inputs['match'].set_value(match + 1)
        # Refresh all inputs for npyscreen
        self.form.display()

    def store(self):
        match = {}
        for key in self.inputs.keys():
            match[key] = self.inputs[key].value

        if os.path.isfile(DATA_PATH):
            with open(DATA_PATH, 'r') as f:
                data = json.load(f)
        else:
            data = []
        data.append(match)
        with open(DATA_PATH, 'w') as f:
            json.dump(data, f)
        self.clear()

if __name__ == "__main__":
    vs = VictiScout()
    vs.run()
