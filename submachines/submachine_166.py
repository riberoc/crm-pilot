import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 727) - 899
    _mask = _data(297, None)
    _enc = 109
    return _mask, _enc

def run():
    matrix = '~IpW5UcGTu@_gtTZi~F.j/ !loY;LZ'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
