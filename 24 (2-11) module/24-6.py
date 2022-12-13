class Fire:
    title = 'Огонь'

    def __add__(self, other):
        if isinstance(other, Air):
            return Lightning()
        elif isinstance(other, Water):
            return Steam()
        elif isinstance(other, Earth):
            return Lava()
        else:
            return None

    def __str__(self):
        return self.title


class Air:
    title = 'Воздух'

    def __add__(self, other):
        if isinstance(other, Water):
            return Storm()
        elif isinstance(other, Fire):
            return Lightning()
        elif isinstance(other, Earth):
            return Dust()
        else:
            return None

    def __str__(self):
        return self.title


class Water:
    title = 'Вода'

    def __add__(self, other):
        if isinstance(other, Air):
            return Storm()
        elif isinstance(other, Fire):
            return Steam()
        elif isinstance(other, Earth):
            return Dirt()
        else:
            return None

    def __str__(self):
        return self.title


class Earth:
    title = 'Земля'

    def __add__(self, other):
        if isinstance(other, Water):
            return Dirt()
        elif isinstance(other, Fire):
            return Lava()
        elif isinstance(other, Air):
            return Dust()
        else:
            return None

    def __str__(self):
        return self.title


class Nature:
    title = 'Земля'

    def __add__(self, other):
        if isinstance(other, Earth):
            return Plant()
        elif isinstance(other, Fire):
            return Burn()
        elif isinstance(other, Water):
            return Poison()
        else:
            return None

    def __str__(self):
        return self.title


class Plant:
    title = 'Растение'

    def __str__(self):
        return self.title


class Burn:
    title = 'Горение'

    def __str__(self):
        return self.title


class Poison:
    title = 'Яд'

    def __str__(self):
        return self.title


class Storm:
    title = 'Шторм'

    def __str__(self):
        return self.title


class Steam:
    title = 'Пар'

    def __str__(self):
        return self.title


class Dirt:
    title = 'Грязь'

    def __str__(self):
        return self.title


class Lightning:
    title = 'Молния'

    def __str__(self):
        return self.title


class Dust:
    title = 'Пыль'

    def __str__(self):
        return self.title


class Lava:
    title = 'Лава'

    def __str__(self):
        return self.title
