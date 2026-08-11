import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 746) - 273
    _mask = _data(984, None)
    _enc = 44
    return _mask, _enc

def run():
    matrix = '8.6q3|dQ3G+9; Zy{_WX&e:HGk8]pS'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
