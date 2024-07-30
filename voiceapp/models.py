from django.db import models

class VoiceNote(models.Model):
    '''creating a model for voice notes'''
    audio_file = models.FileField(upload_to='voice_notes/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    result = models.CharField(max_length=255, default='') # Field for storing the predicted result

    def __str__(self):
        return f"VoiceNote {self.id}"

    class Meta:
        '''specifying the app label'''
        app_label = 'voiceapp'
