import cv2
import hashlib
from mtcnn.mtcnn import MTCNN
from decouple import config
from PicMetric.classes.img_handler import upload_file_to_s3

def faces(input_path):
    #declares MTCNN NN
    detector = MTCNN()
    #loads in the image
    image = cv2.imread(input_path)
    #output of the model
    result = detector.detect_faces(image)
    data = dict()
    #creates boudning boxes for each key point MTCNN identifies
    try:
        bounding_box = result[0]['box']
        keypoints = result[0]['keypoints']
        cv2.rectangle(image,
                (bounding_box[0], bounding_box[1]),
                (bounding_box[0]+bounding_box[2], bounding_box[1] + bounding_box[3]),
                (0,155,255),
                2)
        cv2.circle(image,(keypoints['left_eye']), 2, (0,155,255), 2)
        cv2.circle(image,(keypoints['right_eye']), 2, (0,155,255), 2)
        cv2.circle(image,(keypoints['nose']), 2, (0,155,255), 2)
        cv2.circle(image,(keypoints['mouth_left']), 2, (0,155,255), 2)
        cv2.circle(image,(keypoints['mouth_right']), 2, (0,155,255), 2)

        out_path = "PicMetric/assets/temp/face_test_modeled.jpg"
        cv2.imwrite(out_path, image)
        
        #writes to the data object the URL for original image and the analyzed image.
        #except if there is no data found, then 'no_faces' is placed
        with open(input_path, 'rb') as infile, open(out_path, 'rb') as outfile:
            filename= hashlib.md5(infile.read()).hexdigest() + '_faces.png'
            data['url'] = upload_file_to_s3(outfile, config('S3_BUCKET'), filename)

    except: data['url'] = 'no_faces'

    return data