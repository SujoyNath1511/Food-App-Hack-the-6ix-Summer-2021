""" Kivy Visualizer

This is the main file to be used for window management and using kivy.
"""
# The following are imports used for kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.config import Config
from kivy.uix.popup import Popup
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
Config.set('graphics', 'resizable', False)


class PageManager(ScreenManager):
    """An extension of the ScreenManager class from Kivy used to manage all the
    different pages in the app.
    """
    pass


class ProfileAndSettingsPage(Screen):
    """This is the Profile and Settings Page."""
    page_manager: PageManager

    # Global Class Variables required for kivy.
    name_label = ObjectProperty(None)
    name_input = ObjectProperty(None)
    preferences_label = ObjectProperty(None)
    timer_label = ObjectProperty(None)
    timer_input = ObjectProperty(None)
    page_selector_label = ObjectProperty(None)
    to_recipe_adder = ObjectProperty(None)
    to_recipe_follower = ObjectProperty(None)
    to_credits = ObjectProperty(None)

    def add_page_manager(self, page_manager: PageManager):
        """Adds a Page Manager."""
        self.page_manager = page_manager

    def move_to_recipe_adder(self) -> None:
        """Changes the window to Recipe Adder."""
        self.page_manager.current = "recipe adder"

    def move_to_recipe_follower(self) -> None:
        """Changes the window to Recipe Adder."""
        self.page_manager.current = "recipe follower"

    def move_to_credits(self) -> None:
        """Changes the window to Recipe Adder."""
        self.page_manager.current = "credits"


class RecipeAdderPage(Screen):
    """The Page for adding recipes."""
    page_manager: PageManager

    def add_page_manager(self, page_manager: PageManager):
        """Adds a Page Manager."""
        self.page_manager = page_manager

    def add_ing(self) -> None:
        """Add an ingredient."""
        self.ids.gd1.add_widget(TextInput(multiline=False, size_hint_y=None))
        self.ids.gd1.add_widget(TextInput(multiline=False, size_hint_y=None))
        self.ids.gd1.add_widget(Label(text='', size_hint_y=None))
        # btn = Button(text='Add Ingredient', size_hint_y=None)
        # btn.bind(on_press=self.add_ing)
        # self.ids.gd1.add_widget(btn)


class RecipeFollowerPage(Screen):
    """The Recipe Follower Page."""
    page_manager: PageManager

    def add_page_manager(self, page_manager: PageManager):
        """Adds a Page Manager."""
        self.page_manager = page_manager


class CreditsPage(Screen):
    """Page used to display credits and citations."""
    page_manager: PageManager

    def add_page_manager(self, page_manager: PageManager):
        """Adds a Page Manager."""
        self.page_manager = page_manager


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
