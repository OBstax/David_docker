import socket
#!/usr/bin/python3
#net = jetson.inference.detectNet(argv=['--model=/jetson-inference/python/training/detection/ssd/models/peopledet/ssd-mobilenet.onnx', "--labels=/jetson-inference/python/training/detection/ssd/models/peopledet/labels.txt","--input-blob=input_0", '--output-cvg=scores', '--output-bbox=boxes','--clustering=0'])
#net.SetClusteringThreshold(0.25)
UDP_IP = "172.17.0.2"
UDP_PORT = 5005

print("$$$$$$$$$$$$$$$$TEST$$$$$$$$$$$$")
import jetson.utils
camera = jetson.utils.videoSource("/dev/video0")      # '/dev/video0' for V4L2
display = jetson.utils.videoOutput("display://0") # 'my_video.mp4' for file display://0
#display = jetson.utils.glDisplay() # 'my_video.mp4' for file display://0
import jetson.inference
net = jetson.inference.detectNet("ssd-mobilenet-v2", threshold=0.5)

MESSAGE = ""
my_list = []
print("Still Working")
while display.IsStreaming():
	print("Still Working in while")
	img = camera.Capture()

	detections = net.Detect(img)

	display.Render(img)
	display.SetStatus("Object Detection | Network {:.0f} FPS".format(net.GetNetworkFPS()))
	for det in detections:
		#my_list.append((det.ClassID, det.Left, det.Top, det.Right, det.Bottom))
		#print(my_list)
		MESSAGE = str(det.ClassID) + ", Left:" + str(det.Left) +", Top:"+ str(det.Top) + ", Right:" + str(det.Right) + ", Bottom:" + str(det.Bottom) 

		MESSAGE = str(MESSAGE)
		sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
		sock.sendto(MESSAGE.encode(),(UDP_IP, UDP_PORT))


#print("UDP target IP: %s" % UDP_IP)
#print("UDP target port: %s" % UDP_PORT)
#print("message: %s" % MESSAGE)



