import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 275) - 792
    _mask = _data(738, None)
    _enc = 215
    return _mask, _enc

def run():
    matrix = 'WM_gNo4={oPM::cz}}G^|?DKS8+l|1'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
