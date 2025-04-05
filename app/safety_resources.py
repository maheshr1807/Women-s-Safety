"""
Safety resources module providing access to safety tips and information.
"""
import json
import os
from kivy.network.urlrequest import UrlRequest

class SafetyResources:
    def __init__(self):
        self.resources = {
            'emergency_numbers': {
                'police': '100',
                'women_helpline': '1091',
                'ambulance': '102'
            },
            'safety_tips': [
                {
                    'title': 'Basic Safety Tips',
                    'tips': [
                        'Stay aware of your surroundings',
                        'Keep emergency contacts easily accessible',
                        'Learn basic self-defense techniques',
                        'Trust your instincts'
                    ]
                },
                {
                    'title': 'Travel Safety',
                    'tips': [
                        'Share your location with trusted contacts',
                        'Keep your phone charged',
                        'Use well-lit and populated routes',
                        'Have emergency numbers on speed dial'
                    ]
                }
            ],
            'self_defense': [
                {
                    'title': 'Basic Self-Defense Moves',
                    'techniques': [
                        'Palm Strike',
                        'Knee Strike',
                        'Elbow Strike',
                        'Basic Blocks'
                    ],
                    'description': 'Links to video tutorials and detailed instructions'
                }
            ],
            'legal_information': [
                {
                    'title': 'Women\'s Rights',
                    'content': 'Overview of legal rights and protections'
                },
                {
                    'title': 'Reporting Procedures',
                    'content': 'Steps to file complaints and seek legal help'
                }
            ]
        }
    
    def get_emergency_numbers(self):
        """Return emergency contact numbers."""
        return self.resources['emergency_numbers']
    
    def get_safety_tips(self):
        """Return safety tips and guidelines."""
        return self.resources['safety_tips']
    
    def get_self_defense_info(self):
        """Return self-defense techniques and resources."""
        return self.resources['self_defense']
    
    def get_legal_information(self):
        """Return legal rights and procedures information."""
        return self.resources['legal_information']
    
    def update_resources(self):
        """Update resources from remote server."""
        # Implementation for updating resources from a remote API
        pass
    
    def search_resources(self, query):
        """Search through resources using keywords."""
        results = []
        query = query.lower()
        
        # Search through all resource categories
        for category in self.resources:
            if isinstance(self.resources[category], list):
                for item in self.resources[category]:
                    if query in str(item).lower():
                        results.append({
                            'category': category,
                            'content': item
                        })
        
        return results