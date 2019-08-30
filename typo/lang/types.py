class typo_type:
    name = 'object'

class Bool(typo_type, int):
    name = 'bool'
    def __str__(self):
        return str(bool(self)).lower()
    def __repr__(self):
        return str(bool(self)).lower()