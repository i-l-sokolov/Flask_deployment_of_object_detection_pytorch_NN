import torchvision


def get_model():
    """

    :return: Pretrained model for objects detection. In particular case - Resnet50_FPN
    """
    model = torchvision.models.detection.fasterrcnn_resnet50_fpn(weights='COCO_V1')
    model.eval()
    return model
