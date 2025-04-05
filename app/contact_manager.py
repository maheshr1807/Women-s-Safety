"""
Contact manager module for handling emergency contacts.
"""
import json
import os
from kivy.storage.jsonstore import JsonStore

class ContactManager:
    def __init__(self):
        self.contacts_file = 'emergency_contacts.json'
        self.contacts_store = JsonStore(self.contacts_file)
    
    def add_contact(self, name, phone, email=None, relation=None):
        """Add a new emergency contact."""
        contact_id = str(len(self.contacts_store) + 1)
        self.contacts_store.put(contact_id, 
            name=name,
            phone=phone,
            email=email,
            relation=relation
        )
        return contact_id
    
    def remove_contact(self, contact_id):
        """Remove an emergency contact."""
        if contact_id in self.contacts_store:
            self.contacts_store.delete(contact_id)
            return True
        return False
    
    def get_all_contacts(self):
        """Retrieve all emergency contacts."""
        contacts = []
        for contact_id in self.contacts_store:
            contact = self.contacts_store.get(contact_id)
            contact['id'] = contact_id
            contacts.append(contact)
        return contacts
    
    def update_contact(self, contact_id, **kwargs):
        """Update an existing contact's information."""
        if contact_id in self.contacts_store:
            current = dict(self.contacts_store.get(contact_id))
            current.update(kwargs)
            self.contacts_store.put(contact_id, **current)
            return True
        return False
    
    def notify_emergency_contacts(self, message, location=None):
        """Send emergency notification to all contacts."""
        for contact in self.get_all_contacts():
            self._send_notification(contact, message, location)
    
    def _send_notification(self, contact, message, location=None):
        """Send notification to a single contact."""
        # Implementation for sending SMS/email notifications
        # This would integrate with platform-specific APIs
        notification = {
            'to': contact['phone'],
            'message': message,
            'location': location
        }
        
        # Implement actual sending mechanism (SMS/email)
        if contact.get('phone'):
            self._send_sms(notification)
        if contact.get('email'):
            self._send_email(notification)
    
    def _send_sms(self, notification):
        """Send SMS notification."""
        if platform == 'android':
            from jnius import autoclass
            PythonActivity = autoclass('org.kivy.android.PythonActivity')
            SmsManager = autoclass('android.telephony.SmsManager')
            sms = SmsManager.getDefault()
            sms.sendTextMessage(
                notification['to'],
                None,
                notification['message'],
                None,
                None
            )
    
    def _send_email(self, notification):
        """Send email notification."""
        # Implementation for email notifications
        pass