import requests
import json

#link_page = "https://career.deutsche-boerse.com/job/Frankfurt-am-Main-DevOps-Engineer-Reference-Data-%28femalemale%29-HE/505678401/" #75697
#inputfile = "link.html"
#myfile_inside = open(inputfile, mode="w", encoding="latin_1")
#myfile_inside.write(inside_page.text)
#print(myfile_inside.tell())
#myfile_inside.close()

def lambda_handler(event, context):
    # TODO implement
    #link_page = "https://career.deutsche-boerse.com/job/Prague-DevOps-Engineer-in-Regulatory-%28mfd%29-108/530959601/" #85172
    link_page = "https://www.google.com.ua"
    inside_page = requests.get(link_page)
    size = str(len(inside_page.text))
    if int(len(inside_page.text)) < 80000:
        #raise NameError('Size down!')
        raise Exception("{link_page} is down".format(url=link_page))
    else:
        result = True
    return {
        'statusCode': 200,
        'body': json.dumps('Size is: ' + size + ' Result: ' + str(result))
    }

lambda_handler(1,1)
