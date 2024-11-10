from tools.tools_functions.tools_action.web_search.search_webs import search_ytb, search_google, search_wikipedia, search_bing, search_gpt


tools = {
    "search_ytb": {"description": "recherche sur youtube, cherche sur youtube" if LANGUAGE == 'fr' else 
                   "search on youtube", 
                   "function": search_ytb},

    "search_google": {"description": "cherche sur google, recherche sur google" if LANGUAGE == 'fr' else 
                      "search on google", 
                      "function": search_google},

    "search_wikipedia": {"description": "cherche sur wikipédia, recherche sur wikipédia" if LANGUAGE == 'fr' else 
                         "search on wikipedia", 
                         "function": search_wikipedia},

    "search_bing": {"description": "cherche sur bing, recherche sur bing" if LANGUAGE == 'fr' else 
                    "search on bing", 
                    "function": search_bing},

    "search_gpt": {"description": "ouvre chat gpt" if LANGUAGE == 'fr' else 
                   "open chat gpt", 
                   "function": search_gpt},
}