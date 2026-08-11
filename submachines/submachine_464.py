import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 817) - 618
    _mask = _data(331, None)
    _enc = 23
    return _mask, _enc

def run():
    matrix = 'J8x*KvqyLxnQj^|Bkli=s*CIH<eiG]'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
