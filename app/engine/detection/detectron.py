import torch

from detectron2.config import get_cfg
from detectron2 import model_zoo
from detectron2.engine import DefaultPredictor
from detectron2.data import MetadataCatalog

from .base import BaseDetection


class Detectron(BaseDetection):
    cfg = get_cfg()
    cfg.merge_from_file(model_zoo.get_config_file('COCO-Detection/faster_rcnn_R_101_DC5_3x.yaml'))
    cfg.MODEL.DEVICE = 'cpu'
    predictor = DefaultPredictor(cfg)

    metadata =  MetadataCatalog.get(
        cfg.DATASETS.TEST[0] if len(cfg.DATASETS.TEST) else "__nonexist__"
    )
    class_catalog = metadata.thing_classes

    def detect_frame_objects(self, frame) -> list[int]:
        with torch.no_grad():
            outputs = self.predictor(frame)
            pred_classes = outputs['instances'].pred_classes.cpu().numpy().tolist()

            return pred_classes

    def classes_to_labels(self, classes: list[int]) -> list[str]:
        return [self.class_catalog[i] for i in classes]
