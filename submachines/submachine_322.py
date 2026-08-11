import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 705) - 359
    _mask = _data(236, None)
    _enc = 195
    return _mask, _enc

def run():
    matrix = 'L%#P? cMqca~GofiUucRk&?f&cVu#<'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
