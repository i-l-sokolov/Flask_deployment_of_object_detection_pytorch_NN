from PIL import Image
import cv2
from torchvision import transforms
from .get_model import get_model
from .coco_dict import COCO_INSTANCE_CATEGORY_NAMES

model = get_model()


def get_prediction(img_path, threshold):
    """

    :param img_path:
    :param threshold:
    :return:
    """
    img = Image.open(img_path) # Load the image
    transform = transforms.Compose([transforms.ToTensor()]) # Define PyTorch Transform
    img = transform(img) # Apply the transform to the image
    pred = model([img]) # Pass the image to the model
    pred_class = [COCO_INSTANCE_CATEGORY_NAMES[i] for i in list(pred[0]['labels'].numpy())] # Get the Prediction Score
    pred_boxes = [[(i[0], i[1]), (i[2], i[3])] for i in list(pred[0]['boxes'].detach().numpy())] # Bounding boxes
    pred_score = list(pred[0]['scores'].detach().numpy())
    # Get list of index with score greater than threshold.
    pred_t = [pred_score.index(x) for x in pred_score if x > threshold][-1]
    pred_boxes = pred_boxes[:pred_t+1]
    pred_class = pred_class[:pred_t+1]
    return pred_boxes, pred_class


def object_detection_api(img_path, threshold=0.5, rect_th=3, text_size=1.5, text_th=3):
    """

    :param img_path:
    :param threshold:
    :param rect_th:
    :param text_size:
    :param text_th:
    :return:
    """

    boxes, pred_cls = get_prediction(img_path, threshold) # Get predictions
    img = cv2.imread(img_path) # Read image with cv2
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) # Convert to RGB
    for i in range(len(boxes)):
      left = (int(boxes[i][0][0]),int(boxes[i][0][1]))
      right = (int(boxes[i][1][0]),int(boxes[i][1][1]))
      cv2.rectangle(img, left, right,color=(0, 255, 0), thickness=rect_th) # Draw Rectangle with the coordinates
      cv2.putText(img,pred_cls[i], left,  cv2.FONT_HERSHEY_SIMPLEX, text_size, (0,0,255),thickness=text_th) # Write the prediction class
    image = Image.fromarray(img)
    return image