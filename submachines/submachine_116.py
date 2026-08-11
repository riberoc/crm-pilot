import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 866) - 207
    _mask = _data(755, None)
    _enc = 210
    return _mask, _enc

def run():
    matrix = 'GoHKna#NLja4^LRB =pn;&7B~X;;AS'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
