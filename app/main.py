"""
Main application module for Women's Safety Alert App.
Contains core application setup and navigation.
"""
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

class MainScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        # Panic Button
        panic_button = Button(
            text='EMERGENCY\nPANIC BUTTON',
            size_hint=(1, 0.4),
            background_color=(1, 0, 0, 1)
        )
        panic_button.bind(on_press=self.activate_panic_mode)
        
        # Navigation buttons
        location_btn = Button(text='Location Sharing', size_hint=(1, 0.15))
        contacts_btn = Button(text='Emergency Contacts', size_hint=(1, 0.15))
        recording_btn = Button(text='Audio/Video Recording', size_hint=(1, 0.15))
        resources_btn = Button(text='Safety Resources', size_hint=(1, 0.15))
        
        # Add all buttons to layout
        layout.add_widget(panic_button)
        layout.add_widget(location_btn)
        layout.add_widget(contacts_btn)
        layout.add_widget(recording_btn)
        layout.add_widget(resources_btn)
        
        self.add_widget(layout)
    
    def activate_panic_mode(self, instance):
        # To be implemented in emergency_services.py
        pass

class WomenSafetyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainScreen(name='main'))
        return sm

if __name__ == '__main__':
    WomenSafetyApp().run()