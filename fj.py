import cv2

class ComVis:
  def xpass(img):
    FaceSize = []
    Classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    Image = cv2.imread(img)
    Height, Width, ColChannel = Image.shape
    ConvertGrayscale = cv2.cvtColor(Image, cv2.COLOR_BGR2GRAY)
    Faces = Classifier.detectMultiScale(ConvertGrayscale, 1.3, 5)
    for (x, y, w, h) in Faces:
      print("Face detected")
      FaceSize.append((x+w)*(y+h))

    Calculated = []
    # Calculate each face
    for xFaces in FaceSize:
      Calculated.append((xFaces/(Width*Height))*100)

    return Calculated