"""This is the main file for the app."""

from kivy_visualizer import *

if __name__ == '__main__':
    kv_file = Builder.load_file('Food.kv')
    page_manager = PageManager()
    # TODO Fill up this list
    pages = [ProfileAndSettingsPage(), RecipeAdderPage(), RecipeFollowerPage(), CreditsPage()]
    for page in pages:
        page_manager.add_widget(page)

    # TODO Fill this up.
    page_manager.current = 'profile and settings'

    app = FoodApp(page_manager)

    app.run()
