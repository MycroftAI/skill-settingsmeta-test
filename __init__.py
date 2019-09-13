from mycroft import MycroftSkill, intent_file_handler


class SettingsmetaTest(MycroftSkill):
    def initialize(self):
        self.settings.set_changed_callback(self.print_settings)

    def print_settings(self):
        print(self.settings)
        self.log.info(self.name)
        self.speak("Settings changed")

    @intent_file_handler('blank.intent')
    def blank(self, message):
        self.speak('No content available')


def create_skill():
    return SettingsmetaTest()
