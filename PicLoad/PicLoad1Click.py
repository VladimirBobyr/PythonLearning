import os
import shutil
import requests
import sys

def get_images(infile):
  """ Find - ImageNames """
  imagelist = []
  imagerealnamelist = []
  myfile = open(infile, mode="r", encoding="latin_1")
  what_to_look = 'attachment.php'
  element_number = 1
  for line_image in myfile:
      if what_to_look in line_image:
          image_pos_start = line_image.rfind('attachmentid=')
          image_pos_end = line_image.rfind(' rel=')
          image_name = line_image[image_pos_start:image_pos_end-1]
          amp_pos = image_name.find(('amp;'))
          image_name = image_name[0:amp_pos] + image_name[amp_pos+4:image_name.__len__()]
          image_name = 'https://forum.oneclickchicks.com/attachment.php?' + image_name
          print(image_name)
          imagelist.append(image_name)
          real_name_end = line_image.rfind('.jpg')
          real_name_start = line_image.rfind('alt="')
          imagerealname = line_image[real_name_start+5:real_name_end+4]
          if imagerealname == '':
              imagerealname == str(element_number)
          imagerealnamelist.append(imagerealname)
          element_number = element_number + 1
  return imagelist,imagerealnamelist
  myfile.close()


def get_authorname(link):
   """ Define author and seria and album names based on link"""
   author_name = ''
   seria_name = ''
   album_name = ''

   # Find Album
   symbol_pos = link.rfind('/')
   album_name = link[symbol_pos+1:link.__len__()]

   # Find Seria
   link = link[0:symbol_pos]
   symbol_pos = link.rfind('/')
   seria_name = link[symbol_pos+1:link.__len__()]

   # Find Seria
   link = link[0:symbol_pos]
   symbol_pos = link.rfind('/')
   author_name = link[symbol_pos+1:link.__len__()]

   return (author_name, seria_name, album_name)


def update_progress(progress):
   # update_progress() : Displays or updates a console progress bar
   ## Accepts a float between 0 and 1. Any int will be converted to a float.
   ## A value under 0 represents a 'halt'.
   ## A value at 1 or bigger represents 100%
   barLength = 10 # Modify this to change the length of the progress bar
   status = ""
   if isinstance(progress, int):
       progress = float(progress)
   if not isinstance(progress, float):
       progress = 0
       status = "error: progress var must be float\r\n"
   if progress < 0:
       progress = 0
       status = "Halt...\r\n"
   if progress >= 1:
       progress = 1
       status = "Done...\r\n"
   block = int(round(barLength*progress))
   text = "\rPercent: [{0}] {1}% {2}".format( "#"*block + "-"*(barLength-block), progress*100, status)
   sys.stdout.write(text)
   sys.stdout.flush()

# ========================== MAIN ==============================#

#url_start = 'https://www.imagefap.com/pictures/7847560/Slovanna-3'
#url_start = 'https://forum.oneclickchicks.com/showthread.php?t=69168'
#page = requests.get(url_start) #-- Un-comment in case not on work

inputfile = "script_click.txt"
#myfile = open(inputfile, mode="w", encoding="latin_1")
#myfile.write(page.text)
#myfile.close()

images_list, imagerealname_list = get_images(inputfile)
image_count = images_list.__len__()

folder = 'C:/Inst/01/Click'

print("Saving Images:")
print("progress : 0->" + str(image_count))

payload = {
    'action': 'login',
    'username': 'zlogmein2009',
    'password': 'Q123456'
}

from requests import session

'''
with session() as c:
    c.post('https://forum.oneclickchicks.com/secure-login.php', data=payload)
    saved_count = 1
    for image_name in enumerate(images_list):
        path = folder + '/' + str(imagerealname_list[saved_count])
        #if os.path.exists(path):
        #    print('Canceled, already exist: ' + path)
        #continue
        print(image_name)
        url = image_name[1]
        print(url)
        r = c.request(url, stream=True)
        with open(path, 'wb') as f:
            print(path)
            r.raw.decode_content = True
            shutil.copyfileobj(r.raw, f)
        saved_count = saved_count + 1


print("\nSaved imagges: " + str(saved_count))
'''


