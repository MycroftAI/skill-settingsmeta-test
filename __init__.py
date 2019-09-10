from mycroft import MycroftSkill, intent_file_handler
from mycroft.skills.audioservice import AudioService


class SettingsmetaTest(MycroftSkill):
    @intent_file_handler('blank.intent')
    def blank(self, message):
        self.speak('No content available')


def create_skill():
    return SettingsmetaTest()
