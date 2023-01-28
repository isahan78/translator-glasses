import cv2
import speech_recognition as sr
from langdetect import detect
from googletrans import Translator

# Open the video capture
cap = cv2.VideoCapture(0)

# Initialize the recognizer
r = sr.Recognizer()

while True:
    # Read a frame from the video capture
    ret, frame = cap.read()

    # Access the microphone
    with sr.Microphone() as source:
        # Listen for audio
        audio = r.listen(source)
    try:
        # Recognize the language of the audio
        language = detect(audio)
        # Translate the audio to English
        translator = Translator()
        translated_text = translator.translate(audio, dest='en').text
    except:
        translated_text = "Error: Could not detect language"

    # Add the text to the frame
    cv2.putText(frame, translated_text, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

    # Show the frame
    cv2.imshow("Frame", frame)

    # Exit the loop if the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture
cap.release()

# Close all the windows
cv2.destroyAllWindows()
