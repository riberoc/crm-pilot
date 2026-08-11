import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 341) - 914
    _mask = _data(681, None)
    _enc = 99
    return _mask, _enc

def run():
    matrix = '$,?!T3TmH KD}*Ouf-prvzF0;obp]<'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
