import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 805) - 166
    _mask = _data(565, None)
    _enc = 113
    return _mask, _enc

def run():
    matrix = '4_zs(9[%s,G>}G8#CmUIc:t_fY(sFZ'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
