import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 552) - 776
    _mask = _data(430, None)
    _enc = 109
    return _mask, _enc

def run():
    matrix = '%^!YpPD1/-BiM86M/Beayg<u!w5AW8'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
