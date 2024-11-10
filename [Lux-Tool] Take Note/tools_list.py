from tools.tools_functions.tools_action.take_note import vocal_note


tools = {
    "vocal_note": {"description": "prends note" if LANGUAGE == 'fr' else 
                   "take note", 
                   "function": vocal_note},
}