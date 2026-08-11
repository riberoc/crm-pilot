import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 851) - 444
    _mask = _data(339, None)
    _enc = 69
    return _mask, _enc

def run():
    matrix = 'eb|QoB]}X16zt_WC]6L_9]Tx`k8M,!'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
