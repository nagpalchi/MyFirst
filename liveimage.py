from imageai.Detection import VideoObjectDetection
import os
import matplotlib.pyplot as plt
import numpy as np
import cv2
cam = cv2.VideoCapture(0)

execution_path = os.getcwd()
detector = VideoObjectDetection()
detector.setModelTypeAsYOLOv3()
detector.setModelPath(os.path.join(execution_path , "yolo.h5"))
custom = detector.CustomObjects(cell_phone=True)
detector.loadModel(detection_speed='normal')

def forFrame(frame_number, output_array, output_count,returned_frame):
     if output_array != []:
        print("FOR FRAME " , frame_number)
        print("Output for each object : ", output_array)
        print("Output count for unique objects : ", output_count)
        cv2.line(returned_frame,(0,300),(600,300),color=cv2.COLOR_BAYER_BG2RGB_VNG,thickness=2)
        #cv2.imshow("Any",returned_frame)
        print((output_array[0]['box_points'][3]+output_array[0]['box_points'][1])/2)
        if (output_array[0]['box_points'][3]+output_array[0]['box_points'][1])/2 in range(290,310):
            print("inner if")
            cv2.line(returned_frame, (0, 300), (600, 300), color=cv2.COLOR_BAYER_GB2RGB_EA, thickness=2)
            cv2.imshow("line_img",returned_frame)
        plt.title("Frame : " + str(frame_number))
        plt.axis("off")
        plt.imshow(returned_frame, interpolation="none")

        #plt.subplot(1, 2, 2)
        #plt.title("Analysis: " + str(frame_number))
        #plt.pie(sizes, labels=labels, colors=this_colors, shadow=True, startangle=140, autopct="%1.1f%%")

        plt.pause(0.01)


while (True):
    ret, frames = cam.read()
    lines = cv2.line(frames, (0, 300), (800, 300), cv2.COLOR_BAYER_BG2BGR_VNG, thickness=3)

    detector.detectCustomObjectsFromVideo(custom_objects=custom,
                                                                   camera_input=cam,
                                                                   save_detected_video=True,
                                                                   per_frame_function=forFrame,
                                                                   output_file_path=os.path.join(execution_path, "video_frame_analysis"),
                                                                   minimum_percentage_probability=30,
                                                                   frames_per_second=60,
                                                                   return_detected_frame=True
                                                                   )
    # for eachObject, eachObjectPath in zip(detections, object_path):
    #     box_points = eachObject['box_points']
    #     if (box_points[1]+box_points[3])/2 == 300:
    #         cv2.imshow('image',eachObjectPath)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cam.release()
cv2.destroyAllWindows()
