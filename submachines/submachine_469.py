import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 324) - 629
    _mask = _data(999, None)
    _enc = 51
    return _mask, _enc

def run():
    matrix = 'KuyL%j.ZLP`-aEK<1K3MMFgC|0IqY '
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
