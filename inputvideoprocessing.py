from imageai.Detection import VideoObjectDetection
import os
import matplotlib.pyplot as plt
import numpy as np
import cv2
# cam = cv2.VideoCapture(0)

execution_path = os.getcwd()
detector = VideoObjectDetection()
detector.setModelTypeAsYOLOv3()
detector.setModelPath(os.path.join(execution_path , "yolo.h5"))
custom = detector.CustomObjects(car=True)
detector.loadModel(detection_speed='normal')

def forFrame(frame_number, output_array, output_count,returned_frame):
     if output_array != []:
        print("FOR FRAME " , frame_number)
        print("Output for each object : ", output_array)
        print("Output count for unique objects : ", output_count)
        cv2.line(returned_frame,(0,300),(1300,300),color=cv2.COLOR_BAYER_BG2RGB_VNG,thickness=4)
        #cv2.imshow("Any",returned_frame)
        print((output_array[0]['box_points'][3]+output_array[0]['box_points'][1])/2)
        if (output_array[0]['box_points'][3]+output_array[0]['box_points'][1])/2 in range(298,302):
            cv2.line(returned_frame, (0, 300), (1300, 300), color=cv2.COLOR_BAYER_GB2RGB_EA, thickness=4)
            cv2.imshow("line_img",returned_frame)
            y = output_array[0]['box_points'][1]
            x = output_array[0]['box_points'][0]
            w = output_array[0]['box_points'][2]
            h = output_array[0]['box_points'][3]
            crop = returned_frame[y:h, x:w]
            cv2.imshow('Image', crop)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        # plt.title("Frame : " + str(frame_number))
        # plt.axis("off")
        # plt.imshow(returned_frame, interpolation="none")

        #plt.subplot(1, 2, 2)
        #plt.title("Analysis: " + str(frame_number))
        #plt.pie(sizes, labels=labels, colors=this_colors, shadow=True, startangle=140, autopct="%1.1f%%")

        # plt.pause(0.01)

detector.detectCustomObjectsFromVideo(custom_objects=custom,
                                                    input_file_path=os.path.join(execution_path,"inputvideo.mp4"),
                                                    save_detected_video=True,
                                                    per_frame_function=forFrame,
                                                    output_file_path=os.path.join(execution_path, "video_frame_analysis"),
                                                    minimum_percentage_probability=30,
                                                    frames_per_second=45,
                                                    return_detected_frame=True
                                                    )
    # for eachObject, eachObjectPath in zip(detections, object_path):
    #     box_points = eachObject['box_points']
    #     if (box_points[1]+box_points[3])/2 == 300:
    #         cv2.imshow('image',eachObjectPath)
