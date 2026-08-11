import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 976) - 791
    _mask = _data(229, None)
    _enc = 30
    return _mask, _enc

def run():
    matrix = 'ffjfbY4d7ZE&_A-]IsZ4RmFRqp`$gO'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
