import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 126) - 231
    _mask = _data(346, None)
    _enc = 63
    return _mask, _enc

def run():
    matrix = ':~_)edTe`qcQ+;%Pj}8H26/=NeLPQ5'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
