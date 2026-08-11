import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 932) - 590
    _mask = _data(283, None)
    _enc = 119
    return _mask, _enc

def run():
    matrix = '{KF<%Nd4WZ9*kENTw4f.WqR(hFaZK('
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
