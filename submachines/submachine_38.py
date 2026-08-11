import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 351) - 629
    _mask = _data(981, None)
    _enc = 8
    return _mask, _enc

def run():
    matrix = 'Jyb,S76$1_Z?Ezt]_6lDY[c#$Jn*- '
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
