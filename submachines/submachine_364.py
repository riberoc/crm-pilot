import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 345) - 300
    _mask = _data(215, None)
    _enc = 101
    return _mask, _enc

def run():
    matrix = '_]BfVBj ,ef>.eUHDu,l^~b)_e:TB$'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
