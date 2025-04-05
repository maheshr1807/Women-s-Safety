# Women Safety Mobile Application

## Overview
This mobile application is designed to enhance women's safety through a comprehensive set of features including emergency alerts, location tracking, and quick access to safety resources. Built using the Kivy framework, this application provides a user-friendly interface while incorporating robust safety mechanisms.

## Features
- **Emergency Panic Mode**: Quick activation of emergency protocols
- **Location Tracking**: Real-time GPS location tracking and sharing
- **Emergency Contacts Management**: Add and manage trusted contacts
- **Audio/Video Recording**: Quick recording capabilities in emergency situations
- **Safety Resources**: Access to emergency numbers, safety tips, and legal information

## Technical Requirements
- Python 3.x
- Dependencies:
  - Kivy (≥2.1.0) - UI Framework
  - Plyer (≥2.1.0) - Platform-specific features
  - Twilio (≥8.0.0) - SMS notifications
  - OpenCV (≥4.8.0) - Video recording
  - Firebase Admin (≥6.2.0) - Backend services
  - Additional requirements listed in requirements.txt

## Key Components

### Contact Manager
- Manages emergency contacts
- Handles SMS and email notifications
- Supports adding, removing, and updating contacts

### Emergency Services
- Controls panic mode activation/deactivation
- Coordinates emergency alerts and notifications
- Integrates with other safety features

### Location Services
- Provides real-time GPS tracking
- Enables location sharing with contacts
- Monitors user location status

### Recording Services
- Manages audio and video recording
- Securely stores recorded content
- Supports emergency documentation

### Safety Resources
- Provides access to emergency numbers
- Offers safety tips and self-defense information
- Includes legal resources and information

## Installation
1. Clone the repository
2. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Configuration
- Set up environment variables for sensitive information
- Configure Twilio credentials for SMS functionality
- Set up Firebase Admin SDK for backend services

## Usage
1. Launch the application:
   ```bash
   python app/main.py
   ```
2. Set up emergency contacts
3. Configure personal settings
4. Access safety features through the main interface

## Security Considerations
- All sensitive data is encrypted
- Location data is protected
- Emergency contacts are verified
- Recording storage is secure

## Contributing
Contributions to enhance the application's safety features or improve its functionality are welcome. Please follow standard pull request procedures.

## Support
For support or questions, please contact via Issues
