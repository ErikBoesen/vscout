#!/usr/bin/env python3

import npyscreen

class VictiScout(npyscreen.NPSApp):
    def main(self):
        form = npyscreen.Form(name="VictiScout",)
        text = form.add(npyscreen.TitleText, name="Text:",)
        filename = form.add(npyscreen.TitleFilename, name="Filename:")
        filename_title = form.add(npyscreen.TitleFilenameCombo, name="Filename2:")
        date = form.add(npyscreen.TitleDateCombo, name="Date:")
        slider = form.add(npyscreen.TitleSlider, out_of=12, name="Slider")
        multiline = form.add(npyscreen.MultiLineEdit,
                             value="""try typing here!\nMutiline text, press ^R to reformat.\n""",
                             max_height=5, rely=9)
        radio = form.add(npyscreen.TitleSelectOne, max_height=4, value=[1,], name="Pick One",
                         values=["Option1","Option2","Option3"], scroll_exit=True)
        multiselect = form.add(npyscreen.TitleMultiSelect, max_height =-2, value=[1,], name="Pick Several",
                               values=["Option1","Option2","Option3"], scroll_exit=True)

        # This lets the user interact with the Form.
        form.edit()

if __name__ == "__main__":
    vs = VictiScout()
    vs.run()
