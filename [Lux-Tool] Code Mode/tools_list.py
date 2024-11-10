from tools.tools_functions.tools_action.code_mode.start_code_mode import use_code_mode


tools = {
    "use_code_mode": {"description": "mode code qui est un outil pour faire de la programmation, du codage" if LANGUAGE == 'fr' else 
                      "code mode which is a tool for programming, coding", 
                      "function": use_code_mode},
}