#python script to display camera view using python and send data to html
import cv2

class VideoCamera(object):
    def __init__(self):
        self.video = cv2.VideoCapture(-1) #camera input 
    
    def __del__(self):
        self.video.release()
    
    def get_frame(self):
        success, image = self.video.read()
        flip = cv2.flip(image,1)
        ret, jpeg = cv2.imencode('.jpg', flip)
        return jpeg.tobytes()
