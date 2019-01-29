import os
import shutil
import requests
import sys
import datetime


#from html.parser import HTMLParser


def get_galleryid(infile):
  """ Find Galleryid_input - Argument1 """
  galleryid_input = 0
  myfile = open(infile, mode="r", encoding="latin_1")
  what_to_look = 'galleryid_input'
  for line_getgalleryid in myfile:
      if what_to_look in line_getgalleryid:
          galleryid_input = line_getgalleryid[72:79]
          print("GaleriID: " + galleryid_input.strip())
  return galleryid_input
  myfile.close()


def get_imagecount(infile):
   """ Find - Image count for ProgressBar """
   what_to_look = '1 of '
   infile = open(infile, mode="r", encoding="latin_1")
   for line_get_argument_count in infile:
       if what_to_look in line_get_argument_count:
           start_pos = line_get_argument_count.rfind(what_to_look)
           end_pos = line_get_argument_count.rfind(' pics')
           image_count = line_get_argument_count[start_pos+5:end_pos]
           print('Images count: ' + image_count)
           break
   return image_count.strip()
   myfile.close()


def get_username(infile):
  """ Find Username of Galary """
  username = 0
  myfile = open(infile, mode="r", encoding="latin_1")
  what_to_look = 'Uploaded by '
  for line_username in myfile:
      if what_to_look in line_username:
          username_length = line_username.find('</font>')
          username = line_username[58:username_length]
          print("Username: " + username.strip())
  myfile.close()
  if username == 0:
      myfile = open(infile, mode="r", encoding="latin_1")
      what_to_look = 'gallery by '
      for line_username in myfile:
          if what_to_look in line_username:
              username_start_pos = line_username.find('gallery by') + 11
              i = username_start_pos
              spaceis = line_username[i]
              while spaceis != ' ':
                  i = i + 1
                  spaceis = line_username[i]
              username_end_pos = i
              username = line_username[username_start_pos:username_end_pos]
              print("Username: " + username.strip())
      myfile.close()
  return username.strip()


def get_argument2(infile):
  """ Find - Argument2 """
  what_to_look = '<div class="h"'
  infile = open(infile, mode="r", encoding="latin_1")
  list2 = []
  for line_get_argument2 in infile:
      if what_to_look in line_get_argument2:
          last_symbol = line_get_argument2.rfind('">')
          image2 = line_get_argument2[53:int(last_symbol)]
          # if image2[8] == '"':
          #    image2 = image2[0:7]
          list2.append(image2.strip())
  return list2
  myfile.close()


def get_image_link_for_long(galeriid, argument2):
   """Define real image_name from inside page """
   # Forming link to indide page
   link_page = "https://www.imagefap.com/photo/" + argument2 + "/?pgid=&gid=" + galeriid + "&page=0&idx=0"
   #print("Inside link: " + link_page)
   direct_link = ''
   inside_page = requests.get(link_page)
   inputfile = "script_inside.txt"
   myfile_inside = open(inputfile, mode="w", encoding="latin_1")
   myfile_inside.write(inside_page.text)
   myfile_inside.close()

   myfile_inside = open(inputfile, mode="r", encoding="latin_1")
   for line_for_long_image in myfile_inside:
       what_to_look = 'contentUrl'
       if what_to_look in line_for_long_image:
           #image_end_pos = line_for_long_image.find('Pic From') - 6
           direct_link = line_for_long_image[17:line_for_long_image.__len__()-3]
           break
   if direct_link == '':
       print('Something goes wrong in parsing inside page')
   myfile_inside.close()
   return direct_link


def get_argument3(infile):
  """ Find - Argument3 - ImageName """
  list3 = []
  myfile = open(infile, mode="r", encoding="latin_1")
  what_to_look = '<font face=verdana color="#000000"><i>'
  count_arg2 = 1
  for line_get_argument3 in myfile:
      if what_to_look in line_get_argument3:
          image_length = 0
          image_name3_end_letters = ''
          image_name3_end = line_get_argument3.find('</i>')
          image_name3 = line_get_argument3[57:image_name3_end]
          image_name3 = image_name3.strip()
          list3.append(image_name3)
  return list3
  myfile.close()


def get_album_name(infile):
   """ Define album_name based on galery link"""
   album_name = ''
   myfile = open(infile, mode="r", encoding="latin_1")
   what_to_look = '<meta name="description" content="'
   for line_get_argument3 in myfile:
       if what_to_look in line_get_argument3:
           image_length = 0
           album_name_start_pos = line_get_argument3.find('Browse ')+7
           album_name_end_pos = line_get_argument3.find('picture gallery')-6
           album_name = line_get_argument3[album_name_start_pos:album_name_end_pos]
   myfile.close()
   return album_name


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
url_start = 'https://www.imagefap.com/pictures/7903083/Soccer-Mom-Nancy-Part-1'
is_full_view = url_start.find('view=2')
if is_full_view == -1:
   url_start = url_start + '?view=2'
page = requests.get(url_start) #-- Un-comment in case not on work

inputfile = "script.txt"
myfile = open(inputfile, mode="w", encoding="latin_1")
myfile.write(page.text)
myfile.close()

username_for_contstanta = get_username(inputfile)

stroka = ""
constanta = 'https://x.imagefapusercontent.com/u/' + username_for_contstanta + '/'
print("Contstanta: ")

galeryid = ''
argument_list2 = []
argument_list3 = []

galeryid = get_galleryid(inputfile)

#image_count = get_imagecount(inputfile)

argument_list2 = get_argument2(inputfile)

argument_list3 = get_argument3(inputfile)

len2 = argument_list2.__len__()
len3 = argument_list3.__len__()
print("Count in Argument2 list: " + str(len2))
print("Count in Argument3 list: " + str(len3))

diff = len2-len3

if diff != 0:
  print ("WARNING - counts are different")
  exit()

listurl = []

print("Filling ImageList:")
image_count = argument_list3.__len__()
print("progress : 0->" + str(image_count))
for x in range(0, argument_list3.__len__()):#image3.__len__()-1):
   # ==== Check whether imagename is long name with .. at the end
   image_length = argument_list3[x].__len__()
   image_name3_end_letters = argument_list3[x][(image_length - 2):image_length]
   if image_name3_end_letters == '..':
       # Call function to get real image name
       stroka = get_image_link_for_long(galeryid, argument_list2[x])
   else:
       stroka = constanta + galeryid + '/' + argument_list2[x] + "/" + argument_list3[x]
   #print(stroka)
   listurl.append(stroka)
   update_progress(round(x/argument_list3.__len__(),2))

#================= Part for saving Images locally =======================#
folder = 'C:/Inst/01/'
sub_folder_name = get_album_name(inputfile)
print(sub_folder_name)
folder = folder + sub_folder_name
print(folder)
if not os.path.exists(folder):
  os.makedirs(folder)
url = listurl[0]
count = 1

print("Saving Images:")
print("progress : 0->" + str(image_count))
saved_count=0
for idx, url in enumerate(listurl):
  last_position = url.rfind('/')+1
  image_name = url[last_position:url.__len__()]
  path = folder + '/' + image_name
  if os.path.exists(path):
      print('Canceled, already exist: ' + path)
      continue

  # Uncomment in case want file load
  r = requests.get(url, stream=True)
  update_progress(round(idx/listurl.__len__(),2))

  with open(path, 'wb') as f:
      print(path)
      r.raw.decode_content = True
      shutil.copyfileobj(r.raw, f)
      saved_count = saved_count + 1

print("\nSaved imagges: " +  str(saved_count))