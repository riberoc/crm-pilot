import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 705) - 236
    _mask = _data(838, None)
    _enc = 153
    return _mask, _enc

def run():
    matrix = 'C{ ]uIcX-vyfY&&dB~t3y~~I}~>gM='
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
