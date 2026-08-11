import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 986) - 166
    _mask = _data(592, None)
    _enc = 242
    return _mask, _enc

def run():
    matrix = 'dfYGI#Kslv|B05Rf|TnhL& u!Hm5C/'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
