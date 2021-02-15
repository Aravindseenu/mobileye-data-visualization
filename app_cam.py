# run this scrpt to visualise lane details with camera feed on html page 
# python2 is prefered 
# execute the code "python app_cam.py" and click on the web address to open page in web browser


from flask import Flask,Response,render_template,jsonify
import subprocess
from json import dumps as JSONdumps
from mobileye_data import MobileyeData
from camera import VideoCamera

# initialize a flask object
app = Flask(__name__)

#This funtion will make flask app call the index template 
@app.route('/',methods=['GET'])
def show_charts():
    return render_template('index.html')

@app.route('/lanedata')
def get_lane_data():
    # obtain lane data from the MobileyeData class, pass it to the server by returning or using an event stream
    def stream(): 
        mobileye_parser = MobileyeData()
        for lane_data in mobileye_parser.parse_data():
            if lane_data is None: 
                yield ':'
            else: 
                yield 'data: %s\n\n' % JSONdumps(lane_data) 
    return Response(stream(),mimetype='text/event-stream')
# funtion to get camera frames from the camera code
def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
# funtion to display the video feed in webpage 
@app.route('/video_feed')
def video_feed():
    return Response(gen(VideoCamera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

# the main funtion is executed here the ip and port can be defined here
if __name__ == '__main__':
    app.run(debug=False,port=5081,host='127.0.0.1')
