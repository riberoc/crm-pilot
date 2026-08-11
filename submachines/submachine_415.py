import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 757) - 385
    _mask = _data(174, None)
    _enc = 217
    return _mask, _enc

def run():
    matrix = 'Zzf OPTVPc}*,l<^T>r>A;?`FyQP0z'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
