#!/usr/bin/env python3

import npyscreen

class VictiScout(npyscreen.NPSApp):
    def main(self):
        form = npyscreen.Form(name="VictiScout",)
        self.special = {
            'team': form.add(npyscreen.TitleText, name='Team #'),
            'match': form.add(npyscreen.TitleSlider, name='Match #'),
            'alliance': form.add(npyscreen.TitleSelectOne, name='Alliance', values=['Red', 'Blue']),
            'start-position': form.add(npyscreen.TitleSelectOne, name='Start Position', values=['Left', 'Center', 'Right']),
        }
        self.inputs = {
            'auto-line': form.add(npyscreen.Checkbox, name='AUTO Crossed Line'),
            # TODO: These really shouldn't be sliders.
            'auto-scale': form.add(npyscreen.TitleSlider, out_of=8, name='AUTO Scale Cubes'),
            'auto-switch': form.add(npyscreen.TitleSlider, out_of=8, name='AUTO Switch Cubes'),

            'scale': form.add(npyscreen.TitleSlider, out_of=16, name='Scale Cubes'),
            'switch': form.add(npyscreen.TitleSlider, out_of=16, name='Switch Cubes'),
            'opposition-switch': form.add(npyscreen.TitleSlider, out_of=16, name='Opposition Switch Cubes'),
            'vault': form.add(npyscreen.TitleSlider, out_of=10, name='Vault Cubes'),
            'climbed': form.add(npyscreen.Checkbox, name='Climbed?'),
            'climb-assists': form.add(npyscreen.TitleSlider, out_of=2, name='Climb assists'),

            # TODO: Full advice
            'notes': form.add(npyscreen.TitleMultiLine, name='Notes'),
        }
        """text = form.add(npyscreen.TitleText, name="Text:",)
        filename = form.add(npyscreen.TitleFilename, name="Filename:")
        filename_title = form.add(npyscreen.TitleFilenameCombo, name="Filename2:")
        date = form.add(npyscreen.TitleDateCombo, name="Date:")
        slider = form.add(npyscreen.TitleSlider, out_of=12, name="Slider")
        multiline = form.add(npyscreen.MultiLineEdit,
                             value="try typing here!\nMutiline text, press ^R to reformat.\n",
                             max_height=5, rely=9)
        radio = form.add(npyscreen.TitleSelectOne, max_height=4, value=[1,], name="Pick One",
                         values=["Option1","Option2","Option3"], scroll_exit=True)
        multiselect = form.add(npyscreen.TitleMultiSelect, max_height =-2, value=[1,], name="Pick Several",
                               values=["Option1","Option2","Option3"], scroll_exit=True)
        """

        # This lets the user interact with the Form.
        form.edit()

if __name__ == "__main__":
    vs = VictiScout()
    vs.run()
