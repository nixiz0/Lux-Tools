from tools.tools_functions.tools_action.audio_management.audio_gestion import mute, demute, volume_increase, volume_decrease


tools = {
    "mute": {"description": "mute le volume, mute le son, met en mode silence le volume" if LANGUAGE == 'fr' else 
            "mute the volume, mute the sound, mute the volume", 
            "function": mute},

    "demute": {"description": "remet le volume, demute le son" if LANGUAGE == 'fr' else 
               "reset the volume, unmute the sound", 
               "function": demute},

    "volume_increase": {"description": "augmente le volumne, augmente le son" if LANGUAGE == 'fr' else 
                        "increase the volume, increase the sound", 
                        "function": volume_increase},

    "volume_decrease": {"description": "diminue le volumne, diminue le son" if LANGUAGE == 'fr' else 
                        "decrease the volume, decrease the sound", 
                        "function": volume_decrease},
}