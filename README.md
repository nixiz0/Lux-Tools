# Lux Official Tools

Welcome to the official repository for Lux assistant tools. Here, you will find a collection of tools designed to integrate seamlessly with the Lux assistant.


## Installation of Tools on Lux

You just need to download the tool ZIP File you want.


## [For Developers] How to Create a Tool for Lux

Follow these steps:

1. **Create `tools_list.py`:**
    This is where you will put your function(s) of your tool as well as the description(s) which will enable you to trigger the tool via the similarity between the user prompt and your description(s).

    ```python
    from kernel.tools.tools_functions.tools_action.your_folder.your_script import function_1, function_2
    
    tools = {
        "function_1": {
            "description": "description pour activer une fonction de votre outil" if LANGUAGE == 'fr' else 
                           "description to activate a function of your tool",
            "function": your_function_name
        },
        "function_2": {
            "description": "autre description pour activer une fonction de votre outil" if LANGUAGE == 'fr' else 
                           "other description to activate a function of your tool",
            "function": your_other_function_name
        },
    }
    ```

2. **(if needed) Create `requirements.txt`:**   
    List any external libraries required by your tool that are not already included in Lux.

    For example : 
    ```python
    nltk==3.9.1
    ```

3. **Create `menu.py`:**
    - Define a dictionary containing the global description of your tool. This will be used to activate and access your tool.
    ```python
    {
        "name": "name of your tool",
        "description_fr": "la description en français de l'outil",
        "description_en": "the English description of the tool",
        "emoji": "optional emoji"
    }
    ```

4. **Create a Folder:**
    - For action tools, place your scripts in the `tools_action` folder.
    - For response tools, place your scripts in the `tools_response` folder.

5. **(if needed) Create `select_tool.py`:**
    - If your tool needs to take user input as a parameter, create a `select_tool.py` file listing the names of the functions that require user input.
    ```python
    ["function_name"]
    ```

    ---*Example for a tool that takes user input*---
    On the `select_tool.py` you put: ["vocal_note"]

    On the `tools_list.py` you put:
    ```python
    from kernel.tools.tools_functions.tools_action.take_note import vocal_note

    tools = {
        "vocal_note": {
            "description": "prends note" if LANGUAGE == 'fr' else "take note",
            "function": vocal_note
        },
    }
    ```


## Author

- [@nixiz0](https://github.com/nixiz0)