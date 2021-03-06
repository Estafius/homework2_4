import subprocess
import os
import glob


def resize(files):
 for file in files:
  file = file.strip("Source\\")
  args = ['convert.exe','./Source/' + file,'-resize', '200x200', './Result/' + file.replace(".jpg","_edit.jpg")]
  subprocess.call(args)


def main():
  files = glob.glob(os.path.join('Source', '*jpg'))
  print('Список искомых файлов= ', files)
  print('Уменьшаем фотографии до 200px')
  if not os.path.exists('Result'):
      os.makedirs('Result')
  resize(files)
  files_res = glob.glob(os.path.join('Result', '*jpg'))
  print('Файлы были изменены= ', files_res)
main()