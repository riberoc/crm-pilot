import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 611) - 776
    _mask = _data(466, None)
    _enc = 187
    return _mask, _enc

def run():
    matrix = '*0fNACi|h5-zY0`zU1 5(:Ws6pB+(U'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
