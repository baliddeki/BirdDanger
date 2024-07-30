from django.shortcuts import render, redirect
from .models import VoiceNote
from .voice_analyzer import VoiceAnalyzer

def upload_voice(request):
    '''function for uploading voice notes'''
    if request.method == 'POST':
        audio_file = request.FILES['audio_file']  # Assuming the form field is named 'audio_file'
        voice_analyzer = VoiceAnalyzer()
        predicted_class = voice_analyzer.predict_audio_file(audio_file)

        # Save the voice note to the database
        voice_note = VoiceNote(audio_file=audio_file, result=predicted_class)
        voice_note.save()

        return render(request, 'result.html', {'predicted_class': predicted_class})
    return render(request, 'index.html')  # Changed from 'upload_voice.html' to 'index.html'

def voice_list(request):
    '''function for listing voice notes'''   
    voice_notes = VoiceNote.objects.all()
    return render(request, 'voice_list.html', {'voice_notes': voice_notes})
