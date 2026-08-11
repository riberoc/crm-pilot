import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 990) - 972
    _mask = _data(1881, None)
    _enc = 161
    return _mask, _enc

def run():
    matrix = '(H?ahq9q,4PLg)(;l8z6@2>Ob/ &ok'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
