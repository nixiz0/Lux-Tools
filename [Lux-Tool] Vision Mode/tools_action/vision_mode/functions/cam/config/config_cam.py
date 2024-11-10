import cv2

from constant.colors import * 
from CONFIG import LANGUAGE
from tools.tools_functions.tools_action.cam.config.list_cam_devices import list_video_devices


def select_video_device():
    def select_camera(index):
        cap = cv2.VideoCapture(index)
        if not cap.isOpened():
            print(f"{RED}Impossible d'ouvrir la caméra avec index {index}{RESET}" if LANGUAGE == 'fr' else 
                  f"{RED}Cannot open camera with index {index}{RESET}")
            return None
        return cap

    devices = list_video_devices()
    if not devices:
        print(f"{RED}Aucun périphérique de capture vidéo trouvé.{RESET}" if LANGUAGE == 'fr' else 
              f"{RED}No video capture devices found.{RESET}")
        return
    
    print(f"{CYAN}Appareils de capture vidéo disponibles :{RESET}" if LANGUAGE == 'fr' else
          f"{CYAN}Available video capture devices:{RESET}")
    for i, device in enumerate(devices):
        print(f"{GREEN}{i}: Device {device}{RESET}")
    
    while True:
        selected_index = int(input(f"{CYAN}Saisissez l'index de la caméra que vous souhaitez utiliser : {RESET}" if LANGUAGE == 'fr' else 
                                   f"{CYAN}Enter the index of the camera you want to use: {RESET}"))
        if selected_index < 0 or selected_index >= len(devices):
            print(f"{RED}Index non valide sélectionné.{RESET}" if LANGUAGE == 'fr' else 
                  f"{RED}Invalid index selected.{RESET}")
        else:
            break
    
    cap = select_camera(devices[selected_index])
    if cap:
        print(f"{GREEN}Caméra {selected_index} sélectionnée.{RESET}" if LANGUAGE == 'fr' else 
              f"{GREEN}Camera {selected_index} selected.{RESET}")
        cap.release()
        
        # Update CONFIG.py with the selected camera index
        with open('CONFIG.py', 'r') as file:
            config_content = file.readlines()
        
        with open('CONFIG.py', 'w') as file:
            for line in config_content:
                if line.startswith('CAM_INDEX_USE'):
                    file.write(f'CAM_INDEX_USE= {selected_index}\n')
                else:
                    file.write(line)
