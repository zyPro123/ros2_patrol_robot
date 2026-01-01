import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/ziyue/Project/chapt6/chapt6_ws/src/install/fishbot_application'
