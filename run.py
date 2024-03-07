import os
import numpy
import cv2

list_of_names = []
list_of_teams = []


def delete_old_data():
   for i in os.listdir("generated-certificates/"):
      os.remove("generated-certificates/{}".format(i))


def cleanup_data():
   with open('name-data.txt') as f:
      for line in f:
          list_of_names.append(line.strip())

   with open('team.txt') as g:
      for line in g:
         list_of_teams.append(line.strip())


def generate_certificates():

   for index, name in enumerate(list_of_names):
      certificate_template_image = cv2.imread("3.jpg")
      cv2.putText(certificate_template_image, name.strip(), (1118,690), cv2.FONT_HERSHEY_COMPLEX, 1.5, (0, 0, 0), 5, cv2.LINE_AA)
      cv2.putText(certificate_template_image, list_of_teams[index].strip(), (578,784), cv2.FONT_HERSHEY_COMPLEX, 1.5, (0, 0, 0), 5, cv2.LINE_AA)
      cv2.putText(certificate_template_image, "Pitch or Ditch", (648,876), cv2.FONT_HERSHEY_COMPLEX, 1.5, (0, 0, 0), 5, cv2.LINE_AA)
      cv2.imwrite("generated-certificates/{}.jpg".format(name.strip()), certificate_template_image)
      print("Processing {} / {}".format(index + 1,len(list_of_names)))
      
def main():
   delete_old_data()
   cleanup_data()
   generate_certificates()



if __name__ == '__main__':
   main()

