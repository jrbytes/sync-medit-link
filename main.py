import pyautogui
import time
import pygetwindow as gw
import os
import sys

base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
sync_button_path = os.path.join(base_path, './sync.png')
uploading_all_path = os.path.join(base_path, './carregar_todos.png')
without_network = os.path.join(base_path, './sem_rede.png')
switch_network = os.path.join(base_path, './switch_network_on.png')
close = os.path.join(base_path, './fechar.png')

def image_found(img, confidence):
  try:
    location = pyautogui.locateOnScreen(img, confidence=confidence)
    if location:
      return location
    else:
      print(f"Imagem {img} não encontrada.")
      return None
  except Exception as e:
    print(f"Erro ao localizar a imagem: {e}")
  
# Abre a janela do medit link
windowMeditLink = gw.getWindowsWithTitle('Medit Link')[0]
if windowMeditLink:
  print(windowMeditLink)
  # Restaura a janela
  if windowMeditLink.isMinimized:
    windowMeditLink.restore()
  # Ativa a janela
  windowMeditLink.activate()
  # Espera a tela carregar
  time.sleep(2)
  # Localiza o botão usando imagem
  try:
    print('Executando tarefas...')

    buttonWithoutNetwork = image_found(without_network, confidence=.95)
    if buttonWithoutNetwork:
      pyautogui.click(buttonWithoutNetwork)
      print("Botão WithoutNetwork clicado com sucesso via imagem!")
      pyautogui.click()

      time.sleep(1)
      
      buttonSwitchNetwork = image_found(switch_network, confidence=.8)
      if buttonSwitchNetwork:
        pyautogui.click(buttonSwitchNetwork)
        print("Botão SwitchNetwork clicado com sucesso via imagem!")
        pyautogui.click()

        time.sleep(30)

        buttonClose = image_found(close, confidence=.8)
        if buttonClose:
          pyautogui.click(buttonClose)
          print("Botão Fechar clicado com sucesso via imagem!")
          pyautogui.click()
        else:
          print("Botão Fechar não encontrado na tela!")

        time.sleep(1)

        buttonClose = image_found(close, confidence=.8)
        if buttonClose:
          pyautogui.click(buttonClose)
          print("Botão Fechar clicado com sucesso via imagem!")
          pyautogui.click()
        else:
          print("Botão Fechar não encontrado na tela!")
      else:
        print("Botão SwitchNetwork não encontrado na tela!")
    else:
      print("Botão WithoutNetwork não encontrado na tela!")
    
    time.sleep(1)

    buttonSync = image_found(sync_button_path, confidence=.5)
    if buttonSync:
      pyautogui.click(buttonSync)
      print("Botão ManualSyncButton clicado com sucesso via imagem!")
      pyautogui.click()
    else:
      print("Botão ManualSyncButton não encontrado na tela!")
    
    time.sleep(1)

    buttonUploadingAll = image_found(uploading_all_path, confidence=.5)
    if buttonUploadingAll:
      pyautogui.click(buttonUploadingAll)
      print("Botão Carregar Todos clicado com sucesso via imagem!")
      pyautogui.click()
    else:
      print("Botão Carregar Todos não encontrado na tela!")
  except Exception as e:
    print(f"Erro ao localizar a imagem: {e}")
else:
  print('Janela não encontrada')