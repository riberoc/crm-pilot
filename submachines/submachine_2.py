import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 738) - 918
    _mask = _data(1733, None)
    _enc = 159
    return _mask, _enc

def run():
    matrix = '|7c;;/CfC_q1-g &*=H$RZ2TZ%F$X1'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
