import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 865) - 469
    _mask = _data(280, None)
    _enc = 170
    return _mask, _enc

def run():
    matrix = 'CU03O=*v#.w-TH Q|o4,YP`&?{;SOf'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
