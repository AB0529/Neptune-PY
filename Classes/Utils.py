from termcolor import colored

# Utils class
class Utils:
    def __init__(self, nep):
        self.nep = nep
    
    # ---------------------------------------------------

    # Prettier log
    def log(self, title='no title', content='no content', misc=''):
        print(f'[{colored(title, "blue")}] <> {content} ({colored(misc, "yellow")})')


    # ---------------------------------------------------