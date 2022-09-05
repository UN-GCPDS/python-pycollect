import os

RAWS = list(filter(lambda s:s.endswith('.raw'), os.listdir(os.path.dirname(__file__))))
RAWS_ABSPATH = [os.path.join(os.path.abspath(os.path.dirname(__file__)), p) for p in list(filter(lambda s:s.endswith('.raw'), os.listdir(os.path.dirname(__file__))))]



# os.path.abspath(os.path.dirname(__file__))
# load
