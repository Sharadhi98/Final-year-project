import speech_recognition as sr

def listen():    
    mic_name = "Bus 002 Device 013: ID 0d8c:013c C-Media Electronics, Inc. CM108 Audio Controller"
    sample_rate = 48000
    chunk_size = 2048
    r = sr.Recognizer()
    mic_list = sr.Microphone.list_microphone_names()

    for i, microphone_name in enumerate(mic_list):
        if microphone_name == mic_name:
            print("match !!")
            device_id = i
    print(i)

listen()