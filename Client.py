import socket 
import base64
import cv2
import sys 
def Connect_hendler():
	s = socket.socket()

	s.connect(('192.168.1.104', 8000))
	buffer_size = int(input("How much bytes would you like to Recive? "))
	data =s.recv(buffer_size)
	vid_bytes = open("Video_bytes.txt", "wb")
	vid_bytes.write(data)
	vid_bytes.close()
	video_file = open("recivedVideo.avi", "wb")
	video_file.write(base64.b64decode(open("Video_bytes.txt", "rb").read()))

Connect_hendler()


fourcc = cv2.VideoWriter_fourcc('X','V','I','D')
out = cv2.VideoWriter('VideoToSend.avi',fourcc, 20.0, (640,480))

Cam_cam = cv2.VideoCapture(0)

while True:
	ret , frame = Cam_cam.read()
	out.write(frame)
	cv2.imshow("Web Cam", frame)
			
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
				
	SaveorNo = input("Save This Capture?[Y/n]")
	if SaveorNo =="y" or SaveorNo=="Y":
		out.release()
		with open("VideoToSend.avi", "rb")as f:
			f_bytes=base64.b64encode(f.read())
			bytes_file_to_send = open("VideoBytesToSend.txt", "wb")
			bytes_file_to_send.write(f.bytes)
			s.send(f_bytes)
			buffer_size=sys.getsizeof(f_bytes)
			print ("Video bytes: {}".format(buffer_size))		
				
	
	
	
				
cv2.destroyAllWindows()			

















