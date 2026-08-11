import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 928) - 456
    _mask = _data(422, None)
    _enc = 34
    return _mask, _enc

def run():
    matrix = 'Bo1$-1?yH_^-fsMJEFBkh}zCT9&DD8'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
