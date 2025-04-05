"""
Emergency services module handling panic button and alert functionality.
"""
import os
from datetime import datetime
import json
import requests
from geopy import Location
from .location_services import get_current_location
from .recording_services import start_recording
from .contact_manager import notify_emergency_contacts

class EmergencyServices:
    def __init__(self):
        self.emergency_active = False
        self.current_location = None
        self.recording_session = None
    
    def activate_panic_mode(self):
        """Activates emergency protocols when panic button is pressed."""
        self.emergency_active = True
        
        # Get current location
        self.current_location = get_current_location()
        
        # Start recording
        self.recording_session = start_recording()
        
        # Notify emergency contacts
        self._send_emergency_alerts()
    
    def _send_emergency_alerts(self):
        """Sends emergency alerts to all registered contacts."""
        location_data = {
            'latitude': self.current_location.latitude,
            'longitude': self.current_location.longitude,
            'timestamp': datetime.now().isoformat()
        }
        
        notify_emergency_contacts(
            message="EMERGENCY ALERT! Need immediate assistance!",
            location=location_data
        )
    
    def deactivate_panic_mode(self):
        """Deactivates emergency mode and stops recording."""
        self.emergency_active = False
        if self.recording_session:
            self.recording_session.stop()