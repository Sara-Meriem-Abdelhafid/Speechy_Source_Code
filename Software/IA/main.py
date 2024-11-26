import os
import wave
import pygame # type: ignore
import langid # type: ignore
#import openai
#import librosa
import sklearn # type: ignore
import pyaudio # type: ignore #python bindings for PortAudio the cross_platform audio i/o  library
# Load the pre-trained language identification model
import fasttext # type: ignore # i sould use python 3.12.x verion it wont work with newer
import playsound # type: ignore
from gtts import gTTS # type: ignore
import librosa.display # type: ignore
from langdetect import detect # type: ignore
from pydub import AudioSegment # type: ignore
import pyttsx3 # type: ignore #text to speech
import matplotlib.pyplot as plt # type: ignore
import speech_recognition as sr # type: ignore #Speech to text
from translate import Translator # type: ignore
#from googletrans import Translator
from tempfile import NamedTemporaryFile
from IPython.display import Audio, display # type: ignore
from transformers import MarianMTModel, MarianTokenizer # type: ignore
from transformers import GPT2LMHeadModel, GPT2Tokenizer # type: ignore
#from transliterate import translit
# Ensure pydub can find the ffmpeg/ffprobe binary
AudioSegment.converter = "ffmpeg"  # path to ffmpeg binary



'''
import torch
print("PyTorch:", torch.__version__)  # If PyTorch is installed

import tensorflow as tf
print("TensorFlow:", tf.__version__)  # If TensorFlow is installed

from flax import linen as nn
print("Flax installed")  # If Flax is installed

import pygame
pygame.mixer.init()
pygame.mixer.music.load("your-audio-file.mp3")
pygame.mixer.music.play()

while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)
'''