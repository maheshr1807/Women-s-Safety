"""
Recording services module for audio and video capture.
"""
from kivy.core.audio import Audio
from kivy.utils import platform
from datetime import datetime
import os

class RecordingSession:
    def __init__(self):
        self.recording = False
        self.start_time = None
        self.audio_file = None
        self.video_file = None
        self.storage_path = self._get_storage_path()
    
    def _get_storage_path(self):
        """Get appropriate storage path based on platform."""
        if platform == 'android':
            from android.storage import primary_external_storage_path
            return os.path.join(primary_external_storage_path(), 'WomenSafety', 'Recordings')
        else:
            return os.path.join(os.path.expanduser('~'), 'WomenSafety', 'Recordings')
    
    def start_recording(self):
        """Start audio and video recording."""
        if not self.recording:
            self.recording = True
            self.start_time = datetime.now()
            timestamp = self.start_time.strftime('%Y%m%d_%H%M%S')
            
            # Create storage directory if it doesn't exist
            os.makedirs(self.storage_path, exist_ok=True)
            
            # Initialize audio recording
            self.audio_file = os.path.join(self.storage_path, f'audio_{timestamp}.wav')
            self._start_audio_recording()
            
            # Initialize video recording
            self.video_file = os.path.join(self.storage_path, f'video_{timestamp}.mp4')
            self._start_video_recording()
    
    def stop_recording(self):
        """Stop audio and video recording."""
        if self.recording:
            self.recording = False
            self._stop_audio_recording()
            self._stop_video_recording()
            return {
                'audio_file': self.audio_file,
                'video_file': self.video_file,
                'duration': (datetime.now() - self.start_time).seconds
            }
    
    def _start_audio_recording(self):
        """Platform-specific audio recording implementation."""
        if platform == 'android':
            from jnius import autoclass
            MediaRecorder = autoclass('android.media.MediaRecorder')
            self.audio_recorder = MediaRecorder()
            self.audio_recorder.setAudioSource(MediaRecorder.AudioSource.MIC)
            self.audio_recorder.setOutputFormat(MediaRecorder.OutputFormat.MPEG_4)
            self.audio_recorder.setAudioEncoder(MediaRecorder.AudioEncoder.AAC)
            self.audio_recorder.setOutputFile(self.audio_file)
            self.audio_recorder.prepare()
            self.audio_recorder.start()
    
    def _stop_audio_recording(self):
        """Stop audio recording."""
        if hasattr(self, 'audio_recorder'):
            self.audio_recorder.stop()
            self.audio_recorder.release()
    
    def _start_video_recording(self):
        """Platform-specific video recording implementation."""
        if platform == 'android':
            from jnius import autoclass
            MediaRecorder = autoclass('android.media.MediaRecorder')
            self.video_recorder = MediaRecorder()
            self.video_recorder.setVideoSource(MediaRecorder.VideoSource.CAMERA)
            self.video_recorder.setOutputFormat(MediaRecorder.OutputFormat.MPEG_4)
            self.video_recorder.setVideoEncoder(MediaRecorder.VideoEncoder.H264)
            self.video_recorder.setOutputFile(self.video_file)
            self.video_recorder.prepare()
            self.video_recorder.start()
    
    def _stop_video_recording(self):
        """Stop video recording."""
        if hasattr(self, 'video_recorder'):
            self.video_recorder.stop()
            self.video_recorder.release()