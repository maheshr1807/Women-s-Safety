"""
Location services module for tracking and sharing user location.
"""
from plyer import gps
from kivy.utils import platform
import json

class LocationServices:
    def __init__(self):
        self.location = None
        self._setup_gps()
    
    def _setup_gps(self):
        """Initialize GPS service based on platform."""
        if platform == 'android':
            from android.permissions import request_permissions, Permission
            request_permissions([
                Permission.ACCESS_FINE_LOCATION,
                Permission.ACCESS_COARSE_LOCATION
            ])
        
        gps.configure(
            on_location=self._on_location,
            on_status=self._on_status
        )
    
    def start_location_tracking(self):
        """Start GPS location tracking."""
        gps.start(minTime=1000, minDistance=0)
    
    def stop_location_tracking(self):
        """Stop GPS location tracking."""
        gps.stop()
    
    def _on_location(self, **kwargs):
        """Callback for location updates."""
        self.location = {
            'latitude': kwargs['lat'],
            'longitude': kwargs['lon'],
            'altitude': kwargs['altitude'],
            'speed': kwargs['speed']
        }
    
    def _on_status(self, *args, **kwargs):
        """Callback for GPS status updates."""
        pass
    
    def get_current_location(self):
        """Returns current location data."""
        return self.location
    
    def share_location(self, contact):
        """Share current location with specified contact."""
        if self.location:
            message = {
                'type': 'location_share',
                'location': self.location,
                'sender': 'user'
            }
            # Implementation for sharing location via SMS/email
            return True
        return False