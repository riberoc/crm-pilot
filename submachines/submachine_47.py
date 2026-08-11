import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 129) - 943
    _mask = _data(1223, None)
    _enc = 142
    return _mask, _enc

def run():
    matrix = 'i@Bc,C/z$ltTC.+G^W=q6OSRLeheTB'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
