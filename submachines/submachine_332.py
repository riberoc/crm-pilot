import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 372) - 888
    _mask = _data(692, None)
    _enc = 65
    return _mask, _enc

def run():
    matrix = 'xI}?$/eI0eW+uey~%=TK4>9ptQ:/!A'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
