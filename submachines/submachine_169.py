import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 437) - 648
    _mask = _data(741, None)
    _enc = 210
    return _mask, _enc

def run():
    matrix = 'uOb76SUK`mnCag8b.HZ@^m92AU uAa'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
