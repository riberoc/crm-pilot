import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 303) - 646
    _mask = _data(997, None)
    _enc = 71
    return _mask, _enc

def run():
    matrix = 'unnc>T]Fj_sM@1g29&z[:4l%F{IGq<'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
