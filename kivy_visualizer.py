""" Kivy Visualizer

This is the main file to be used for window management and using kivy.
"""
# The following are imports used for kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label


class ProfileAndSettingsPage(Screen):
    """This is the Profile and Settings Page."""
    pass


class RecipeAdderPage(Screen):
    """The Page for adding recipes."""
    pass


class RecipeFollowerPage(Screen):
    """The Recipe Follower Page."""
    pass


class CreditsPage(Screen):
    """Page used to display credits and citations."""
    pass


class PageManager(ScreenManager):
    """An extension of the ScreenManager class from Kivy used to manage all the
    different pages in the app.
    """
    pass


class FoodApp(App):
    """An extension of the Kivy App class used to create the main app.

    Instance Attributes:
    - page_manager: Is an instance of the PageManager Class.
    """
    page_manager: PageManager

    def __init__(self, page_manager: PageManager, **kwargs) -> None:
        """The initializer."""
        super().__init__(**kwargs)
        self.page_manager = page_manager

    def build(self) -> PageManager:
        """Returns a window manager which shows all the different pages."""
        return self.page_manager


if __name__ == '__main__':
    ...
