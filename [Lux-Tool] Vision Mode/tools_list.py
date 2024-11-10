from tools.tools_functions.tools_action.vision_mode.start_vision import start_llm_vision


tools = {
    "start_llm_vision": {"description": "outil pour utiliser le mode vision" if LANGUAGE == 'fr' else 
                         "tool to use vision mode", 
                         "function": start_llm_vision},
}