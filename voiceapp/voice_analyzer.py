import librosa
import numpy as np
from tensorflow.keras.models import load_model
from scipy.ndimage import zoom

class VoiceAnalyzer:
    '''class for analyzing voice notes'''
    def __init__(self):
        self.model = load_model('bird_call_classifier_model.h5')

    def preprocess_audio_file(self, audio_file, target_sr=22050, fixed_shape=(128, 128)):
        '''function for preprocessing audio files'''
        y, sr = librosa.load(audio_file, sr=target_sr)
        spectrogram = librosa.feature.melspectrogram(y=y, sr=sr)
        spectrogram_db = librosa.power_to_db(spectrogram, ref=np.max)
    
        resized_spectrogram = zoom(spectrogram_db, (fixed_shape[0] / spectrogram_db.shape[0], fixed_shape[1] / spectrogram_db.shape[1]))
    
        input_data = np.expand_dims(resized_spectrogram, axis=-1)
        input_data = np.expand_dims(input_data, axis=0)
        return input_data

    def predict_audio_file(self, audio_file):
        '''function for predicting audio files'''
        input_data = self.preprocess_audio_file(audio_file)
        predictions = self.model.predict(input_data)
    
        predicted_class_index = np.argmax(predictions)
        class_names = ['This is an alarm call', 'This is a mating call', 'This is neither a mating nor an alarm call']
        predicted_class = class_names[predicted_class_index]
    
        return predicted_class
