from tools.tools_functions.tools_action.cam.screen_cam import screen_with_cam


tools = {
    "screen_with_cam": {"description": "screen avec la caméra" if LANGUAGE == 'fr' else 
                        "screen with the camera", 
                        "function": screen_with_cam},
}
