import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 225) - 113
    _mask = _data(509, None)
    _enc = 175
    return _mask, _enc

def run():
    matrix = 'tlhW A7}0{Nn4KFL(hGjb+R[K}{|Te'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
