import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 194) - 790
    _mask = _data(813, None)
    _enc = 223
    return _mask, _enc

def run():
    matrix = 'J=L/(pe8AB{N%<5]e5}0ULidDgd&%p'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
