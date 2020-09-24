from mycroft import MycroftSkill, intent_handler


class SettingsmetaTest(MycroftSkill):
    def initialize(self):
        self.settings_changed_callback = self.print_settings
        try:
            self.gui.register_settings()
        except AttributeError:
            self.log.error('GUI settings registration not available')

    def print_settings(self):
        print(self.settings)
        self.log.info(self.name)
        self.speak("Settings changed")

    @intent_handler('display.settings.intent')
    def handle_display_settings(self, message):
        self.speak_dialog('on.screen')
        self.gui.show_settings()

    @intent_handler('what.is.text.field.intent')
    def handle_speak_text_field(self, message):
        if self.settings.get("single_text_field") is None:
            self.speak_dialog("settings.unavailable")
        elif self.settings["single_text_field"] == "":
            self.speak_dialog("setting.field.empty")
        else:
            self.speak_dialog(self.settings.single_text_field)


def create_skill():
    return SettingsmetaTest()
