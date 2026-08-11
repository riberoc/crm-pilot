import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 303) - 836
    _mask = _data(741, None)
    _enc = 142
    return _mask, _enc

def run():
    matrix = '6i&16J!1 2KnQr|;gNJW*dwr9DO:EG'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
