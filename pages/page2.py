import streamlit as st
from streamlit import session_state as ss
from modules.nav import MenuButtons
from pages.account import get_roles

import os
import numpy as np
import librosa
import matplotlib.pyplot as plt
import librosa.display
import IPython.display as ipd
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation
from keras.optimizers import Adam
from keras.utils import to_categorical
from sklearn.preprocessing import LabelEncoder
import tensorflow as tf
from tensorflow.keras import layers,models
from keras.callbacks import ModelCheckpoint
from datetime import datetime
from tensorflow.keras.models import load_model

import streamlit_authenticator as stauth

import io
import tempfile

from st_audiorec import st_audiorec

# If the user reloads or refreshes the page while still logged in,
# go to the account page to restore the login status. Note reloading
# the page changes the session id and previous state values are lost.
# What we are doing is only to relogin the user.
if 'authentication_status' not in ss:
    st.switch_page('./pages/account.py')

MenuButtons(get_roles())


def load_audio(file_path):
    y, sr = librosa.load(file_path)
    return y, sr

def extract_features(y, sr):
    mfcc = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=38)
    # chroma = librosa.feature.chroma_stft(y=y, sr=sr)
    # contrast = librosa.feature.spectral_contrast(y=y, sr=sr)
    # tonnetz = librosa.feature.tonnetz(y=y, sr=sr)
    
    # feature_vector = np.hstack([np.mean(mfcc, axis=1), np.mean(chroma, axis=1),
    #                             np.mean(contrast, axis=1), np.mean(tonnetz, axis=1)])
    
    mfccs_scaled_features = np.mean(mfcc.T, axis=0)

    return mfccs_scaled_features
    # return feature_vector
# Function to extract features from all audio files in the dataset directory

extracted_features = []    

def extract_features_from_directory(directory):
    features = []
    labels = []
    
    # Loop over each raga folder in the directory
    for raga_folder in os.listdir(directory):
        raga_path = os.path.join(directory, raga_folder)
        if os.path.isdir(raga_path):
            # Loop over each audio file in the raga folder
            for file in os.listdir(raga_path):
                file_path = os.path.join(raga_path, file)
                if file.endswith('.wav'):
                    y, sr = load_audio(file_path)
                    feature_vector = extract_features(y, sr)
                    features.append(feature_vector)
                    labels.append(raga_folder)  # Folder name is used as label (raga)
                    extracted_features.append([feature_vector, raga_folder])
    
    print(f"Extracted {len(features)} feature vectors.")
    return np.array(features), np.array(labels)

dataset_directory = r'F:\BE Project\Dataset\mydataset4'



@st.cache_resource

def load_cnn_model():
    return load_model("cnn_audio_model.h5")

# Function to load label encoder classes
@st.cache_resource
def load_label_encoder():
    le = LabelEncoder()
    le.classes_ = np.load("label_classes.npy", allow_pickle=True)
    return le

# Load the model and label encoder
model = load_cnn_model()
label_encoder = load_label_encoder()

# # Streamlit UI
# st.title("Audio Raga Classification")
# st.write("Upload an audio file to predict its raga.")

# uploaded_file = st.file_uploader("Choose a WAV file", type=["wav"])

# if uploaded_file is not None:
#     # Display the uploaded audio file
#     st.audio(uploaded_file, format="audio/wav")

#     # Load and preprocess the audio
#     y, sr = librosa.load(uploaded_file)
#     features = extract_features(y, sr)
#     features = features.reshape(1, -1)

#     # Predict the class
#     predicted_probabilities = model.predict(features)
#     predicted_class_index = np.argmax(predicted_probabilities)
#     predicted_class = label_encoder.inverse_transform([predicted_class_index])

#     # Display the prediction
#     st.success(f"Predicted Raga: {predicted_class[0]}")






st.subheader("Hii, How are You :wave:")

st.title("A system for efficient identification of ragas from audio clip.")
# st.write("A system for efficient identification of ragas from audio clip of a song")
st.write("Indian classical music is rich and diverse, featuring a wide range of Ragas that each evoke distinct emotions and moods. However, the identification of Ragas requires deep knowledge and expertise in the music theory and practice, which poses a challenge for automated systems.")
st.write("The goal of this project is to develop a robust and accurate system for the automatic identification of Ragas from audio recordings of Indian classical music. This system will leverage AI/ML techniques to classify audio recordings into predefined Raga categories, facilitating easier access to and analysis of Indian classical music.")
st.write("[Learn more>](https://google.com)")

# audio=r'F:\BE Project\Dataset\archive\yaman01.wav'
# st.audio(audio,format="audio/mp3")
# aud=st.file_uploader("upload your audio file",type=["mp3","wav"])
# if aud:
#     st.audio(aud,format="audio/mp3")
    
# file =r'F:\BE Project\Dataset\mydataset4\asavari\asavari01.wav'
# file =r'C:\Users\Dell\OneDrive\Desktop\bhoopali.dat.wav'

# file=st.file_uploader("UPLOAD YOUR RAAGA AUDIO FOR PREDICTION",type=["mp3","wav"])
# if file:
#     st.audio(file,format="audio/mp3")
#     x,sr1 = librosa.load(file)
#     ipd.Audio(x,rate=sr1)

#     prediction_feature = extract_features(x,sr1)
#     prediction_feature = prediction_feature.reshape(1,-1)
#     predicted_probabilities = model.predict(prediction_feature)
#     predicted_class_label = np.argmax(predicted_probabilities)
#     predicted_class_label = np.array([predicted_class_label])
#     prediction_class = label_encoder.inverse_transform(predicted_class_label)
#     print("Predicted class:", prediction_class[0]) 
    
#     st.write(prediction_class[0])   
    
    # Start recording
audio_bytes = st_audiorec()

# Playback and save

# if audio_bytes:
#     # st.audio(audio_bytes, format="audio/wav")
#     with open("recorded_audio.wav", "wb") as f:
#         f.write(audio_bytes)
#     st.success("Audio saved as 'recorded_audio.wav'")
#     file =r'F:\BE Project\recorded_audio.wav'
#     x,sr1 = librosa.load(file)
#     ipd.Audio(x,rate=sr1)

#     prediction_feature = extract_features(x,sr1)
#     prediction_feature = prediction_feature.reshape(1,-1)
#     predicted_probabilities = model.predict(prediction_feature)
#     predicted_class_label = np.argmax(predicted_probabilities)
#     predicted_class_label = np.array([predicted_class_label])
#     prediction_class = label_encoder.inverse_transform(predicted_class_label)
#     print("Predicted class:", prediction_class[0]) 
    
#     st.write(prediction_class[0])  



# Assuming 'audio_bytes' contains the audio data
if audio_bytes:
    # Create a temporary file
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp_file:
        tmp_file.write(audio_bytes)
        tmp_file_path = tmp_file.name

    # Load the audio file
    x,sr1 = librosa.load(tmp_file_path)
    ipd.Audio(x,rate=sr1)

    prediction_feature = extract_features(x,sr1)
    prediction_feature = prediction_feature.reshape(1,-1)
    predicted_probabilities = model.predict(prediction_feature)
    predicted_class_label = np.argmax(predicted_probabilities)
    predicted_class_label = np.array([predicted_class_label])
    prediction_class = label_encoder.inverse_transform(predicted_class_label)
    print("Predicted class:", prediction_class[0]) 
    
    # st.write(prediction_class[0])  
    predicted_raga = prediction_class[0].upper()
    st.success(f"🎵 Predicted Raga: **{predicted_raga}**")

