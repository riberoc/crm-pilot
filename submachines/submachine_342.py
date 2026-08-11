import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 397) - 254
    _mask = _data(213, None)
    _enc = 80
    return _mask, _enc

def run():
    matrix = 'De(vq^RBCB (9;~$Pr{KO4$+|del{g'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
