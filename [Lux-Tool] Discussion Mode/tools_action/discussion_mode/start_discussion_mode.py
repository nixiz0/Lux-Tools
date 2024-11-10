import subprocess
from constant.colors import *
from CONFIG import TEMP_AUDIO_PATH
from tools.tools_functions.tools_action.discussion_mode.CONFIG_TOOL import *
from tools.tools_functions.tools_action.discussion_mode.functions.auto_build_model import build_discussion_model
from tools.tools_functions.tools_action.discussion_mode.functions.discussion_llm import discussion_llm_prompt
from audio.speech_to_text.record import record_audio
from audio.speech_to_text.whisper import SpeechToText
from audio.synthetic_voice.voice import LuxVoice
from tools.tools_functions.tools_action.discussion_mode.functions.save_history import save_history


conversation_history = []
def use_discussion_mode():
    global conversation_history
    whisper = SpeechToText()
    lux_voice = LuxVoice()

    # Run the 'ollama list' command and get the output
    result = subprocess.run(['ollama', 'list'], capture_output=True, text=True)
    
    # Checks if LLM_NAME is in the list of models
    if DISCUSSION_MODEL_NAME in result.stdout:
        pass
    else:
        print(f"{RED}Modèle {DISCUSSION_MODEL_NAME} non trouvé. Installation..{RESET}" if LANGUAGE == 'fr' else
              f"{RED}Model {DISCUSSION_MODEL_NAME} not found. Installation..{DISCUSSION_BASE_LLM}.{RESET}")
        subprocess.run(['ollama', 'pull', DISCUSSION_BASE_LLM])
        build_discussion_model()

    lux_voice.speak("Vous souhaitez discuter de quoi monsieur" if LANGUAGE == 'fr' else "What do you wish to discuss sir")

    running = True
    skip_prompt = False
    while running:
        skip_prompt = False
        record_audio()
        speech_transcribe = whisper.transcribe(TEMP_AUDIO_PATH)
        user_prompt = speech_transcribe
        print(user_prompt + "\n")

        if user_prompt in ["c'est bon", "arrête le mode discussion", "arrête la discussion", "tu peux arrêter", "arrête", "stop",
                           "it's okay", "stop chat mode", "stop discussion mode", "you can stop", "stop the discussion", "you can stop"]:
            lux_voice.speak("J'arrête de la discussion" if LANGUAGE == 'fr' else "I'm stopping the discussion")
            running = False
            continue

        if user_prompt in ["sauvegarde", "sauvegarde ça", "sauvegarde moi ça", "sauvegarde sauvegarde", "sauvegarde moi ça"
                           "save", "save this", "save this for me", "save save"]:
            save_history(response_text)
            lux_voice.speak("Sauvegarde de ma réponse sur votre bureau effectué" if LANGUAGE == 'fr' else 
                            "Saved my response to your desktop")
            skip_prompt = True
            continue

        if user_prompt in ["sauvegarde moi tout ça", "sauvegarde tout", "sauvegarde globale", "sauvegarde notre discussion", 
                           "save everything for me", "save everything", "global save", "save our discussion"]:
            save_history(conversation_history)
            lux_voice.speak("Sauvegarde de la discussion sur votre bureau effectué" if LANGUAGE == 'fr' else 
                            "Saved the chat to your desktop")
            skip_prompt = True
            continue

        if not skip_prompt:
            response_text = discussion_llm_prompt(user_prompt, conversation_history)
            lux_voice.speak(response_text)
        else:
            skip_prompt = False