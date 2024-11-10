from tools.tools_functions.tools_action.screenshot import screen


tools = {
    "screen": {"description": "prends un screenshot, prends une capture d'écran" if LANGUAGE == 'fr' else 
               "take a screenshot", 
               "function": screen},
}