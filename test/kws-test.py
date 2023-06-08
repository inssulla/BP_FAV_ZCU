from vosk import Model, KaldiRecognizer 
import json  
import wave  
import os  
import speech_recognition


def record_and_recognize_audio(*args: tuple):
    """
    Запись и распознавание аудио
    """
    with microphone:
        recognized_data = ""

        # запоминание шумов окружения для последующей очистки звука от них
        recognizer.adjust_for_ambient_noise(microphone, duration=5)

        try:
            print("Listening...")
            audio = recognizer.listen(microphone, 5, 5)

            with open("microphone-results.wav", "wb") as file:
                file.write(audio.get_wav_data())

        except speech_recognition.WaitTimeoutError:
            play_voice_assistant_speech(translator.get("Can you check if your microphone is on, please?"))
            traceback.print_exc()
            return

        # использование online-распознавания через Google (высокое качество распознавания)
        # try:
        #     print("Started recognition...")
        #     recognized_data = recognizer.recognize_google(audio, language=assistant.recognition_language).lower()

        # except speech_recognition.UnknownValueError:
        #     pass  # play_voice_assistant_speech("What did you say again?")

        # # в случае проблем с доступом в Интернет происходит попытка использовать offline-распознавание через Vosk
        # except speech_recognition.RequestError:
        #     print(colored("Trying to use offline recognition...", "cyan"))
        #     recognized_data = use_offline_recognition()

        print("Started recognition...")
        recognized_data = use_offline_recognition()
        return recognized_data


def use_offline_recognition():
    """
    Переключение на оффлайн-распознавание речи
    :return: распознанная фраза
    """
    recognized_data = ""
    try:
        # проверка наличия модели на нужном языке в каталоге приложения
        if not os.path.exists("vosk-model-small-en-us-0.15"):
            print(colored("Please download the model from:\n"
                          "https://alphacephei.com/vosk/models and unpack as 'model' in the current folder.",
                          "red"))
            exit(1)

        # анализ записанного в микрофон аудио (чтобы избежать повторов фразы)
        wave_audio_file = wave.open("microphone-results.wav", "rb")
        model = Model("vosk-model-small-en-us-0.15")
        offline_recognizer = KaldiRecognizer(model, wave_audio_file.getframerate())

        data = wave_audio_file.readframes(wave_audio_file.getnframes())
        if len(data) > 0:
            if offline_recognizer.AcceptWaveform(data):
                recognized_data = offline_recognizer.Result()

                # получение данных распознанного текста из JSON-строки (чтобы можно было выдать по ней ответ)
                recognized_data = json.loads(recognized_data)
                recognized_data = recognized_data["text"]
    # except:
    #     traceback.print_exc()
    #     print(colored("Sorry, speech service is unavailable. Try again later", "red"))
    except:
        print("Sorry, speech service is unavailable. Try again later")

    return recognized_data

def execute_command_with_name(command_name: str, *args: list):
    """
    Выполнение заданной пользователем команды и аргументами
    :param command_name: название команды
    :param args: аргументы, которые будут переданы в метод
    :return:
    """
    for key in commands.keys():
        if command_name in key:
            commands[key](*args)
        else:
            pass  # print("Command not found")

def play_test():
    print("+")

# перечень команд для использования (качестве ключей словаря используется hashable-тип tuple)
# в качестве альтернативы можно использовать JSON-объект с намерениями и сценариями
# (подобно тем, что применяют для чат-ботов)
commands = {
    ("hello", "hi", "morning", "привет"): play_test,
}





if __name__ == "__main__":

    # инициализация инструментов распознавания и ввода речи
    recognizer = speech_recognition.Recognizer()
    microphone = speech_recognition.Microphone()

    # # настройка данных пользователя
    # person = OwnerPerson()
    # person.name = "Tanya"
    # person.home_city = "Yekaterinburg"
    # person.native_language = "ru"
    # person.target_language = "en"

    # # настройка данных голосового помощника
    # assistant = VoiceAssistant()
    # assistant.name = "Alice"
    # assistant.sex = "female"
    # assistant.speech_language = "en"

    while True:
        # старт записи речи с последующим выводом распознанной речи и удалением записанного в микрофон аудио
        voice_input = record_and_recognize_audio()
        #os.remove("microphone-results.wav")
        print(voice_input)

        # отделение комманд от дополнительной информации (аргументов)
        voice_input = voice_input.split(" ")
        command = voice_input[0]
        command_options = [str(input_part) for input_part in voice_input[1:len(voice_input)]]
        execute_command_with_name(command, command_options)