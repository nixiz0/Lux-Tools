from tools.tools_functions.tools_action.discussion_mode.start_discussion_mode import use_discussion_mode


tools = {
    "use_discussion_mode": {"description": "mode discussion qui permet d'avoir une conversation, une discussion, de discuter" if LANGUAGE == 'fr' else 
                            "discussion mode which allows to have a conversation, a discussion, to discuss", 
                            "function": use_discussion_mode},
}