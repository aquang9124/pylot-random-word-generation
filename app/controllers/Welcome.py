"""
    Sample Controller File

    A Controller should be in charge of responding to a request.
    Load models to interact with the database and load views to render them to the client.

    Create a controller using this template
"""
from system.core.controller import *
from random import choice
from string import ascii_uppercase

class Welcome(Controller):
    def __init__(self, action):
        super(Welcome, self).__init__(action)
        """
            This is an example of loading a model.
            Every controller has access to the load_model method.

            self.load_model('WelcomeModel')
        """

    """ This is an example of a controller method that will load a view for the client """
    def index(self):
        """ 
        A loaded model is accessible through the models attribute 
        self.models['WelcomeModel'].get_all_users()
        """
        if 'count' in session:
            session['count'] += 1
        else:
            session['count'] = 0
        return self.load_view('index.html', count = session['count'])
    def generate(self):
        num = ''.join(choice(ascii_uppercase) for i in range(14))
        session['num'] = num
        return redirect('/')
