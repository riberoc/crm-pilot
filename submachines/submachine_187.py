import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 444) - 122
    _mask = _data(362, None)
    _enc = 74
    return _mask, _enc

def run():
    matrix = 'a$%vi4ncp&5FxH6_jCF6e* 3L>C}XE'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
