class Phone:

    def __init__(self, color, model):
        self.color = color
        self.model = model

    # обычный метод
    def check_sim(self, mobile_operator):
        if self.model == 'I785' and mobile_operator == 'MTS':
            print('Your mobile operator is MTS')

    # статический метод
    @staticmethod
    def model_hash(model):
        if model == 'I785':
            return 34565
        elif model == 'K498':
            return 45567
        else:
            return None


###################################################################


class Distance:
    MIN_DISTANCE = 0
    MAX_DISTANCE = 100

    @classmethod
    def validate(cls, arg):
        # этот метод не сможет обращаться к динамическим свойствам класса.
        # у нас будет иметься доступ только к атрибутам самого класса
        return cls.MIN_DISTANCE <= arg <= cls.MAX_DISTANCE
