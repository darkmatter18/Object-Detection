from .base import BaseDetection

def instance(model='detectron') -> BaseDetection:
    if model == 'detectron':
        from .detectron import Detectron
        return Detectron()
    else:
        raise NotImplementedError(f'Model {model} not implemented')
