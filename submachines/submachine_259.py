import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 102) - 793
    _mask = _data(961, None)
    _enc = 147
    return _mask, _enc

def run():
    matrix = '2fnFw5$EuvfL$)~,!YrulF()1:GGF '
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
