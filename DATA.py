
from VAR import user_name, code_lang, lang_version

class CL_DATA:

    def __init__(self, user_name, code_lang, lang_version):

        self.user_name = user_name
        self.code_lang = code_lang
        self.lang_version = lang_version

    def welcome_note(self):

        print("Hello {} to {} {}. Let's Start the course".format(user_name, code_lang, lang_version))


    def dsply_data(self):

         print("::::::::::::::::::::::::Alphatuts++:::::::::::::::::::::::")
         print(":::::::::::::::::::   User Information :::::::::::::::::::")
         print("         NAME : {}           Course : {}".format(user_name, code_lang))
