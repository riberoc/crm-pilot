import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 978) - 307
    _mask = _data(512, None)
    _enc = 153
    return _mask, _enc

def run():
    matrix = ']^Ewv2 @1-JeIP6NiLAMuPPB>W{@}I'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
