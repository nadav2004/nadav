import numpy as np
import cv2
import base64 
import socket 
import sys 
host = '0.0.0.0'
port = 8001
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host,port))
s.listen(1)
conn , addr = s.accept()

print (addr)


cam_cap = cv2.VideoCapture(0)

fourcc = cv2.VideoWriter_fourcc('X','V','I','D')
out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640,480))



while True:
	ret , frame =cam_cap.read()
	out.write(frame)
	
	cv2.imshow("frame", frame)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
	
		
SendVid = input("Send this Capture: [Y/n]")

if SendVid=="Y" or SendVid=="y":
	out.release()
	with open("output.avi", "rb")as f :
		f_bytes = base64.b64encode(f.read())
		bytes_file = open("VideoBytes.txt", "wb")
		bytes_file.write(f_bytes)
		conn.send(f_bytes)
		buffer_size =sys.getsizeof(f_bytes)
		print ("Bytes of the Video: {}".format(buffer_size))		
		buffer_size_to_recive = int(input("How many bytes would you like to recive? "))
		data = conn.recv(buffer_size_to_recive)
		vid_bytes = open("Video_bytes.txt", "wb")
		vid_bytes.write(data)
		vid_bytes.close()
		video_file = open("recivedVideo.avi", "wb")
		video_file.write(base64.b64decode(open("Video_bytes.txt", "rb").read()))

		
if SendVid=="n" or SendVid=="No":
	print ("Ok")		
cam_cap.release()
cv2.destroyAllWindows()		
        
        

