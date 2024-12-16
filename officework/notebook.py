class Notebook(list):
    def __init__(self, notes: list[dict[str, bool | str]], *args, **kwargs):
        super().__init__(*args, **kwargs)

        for note in notes:
            self.append({"collected": False, "note": note})

    def __add__(self, other, *args, **kwargs):
        if isinstance(other, Notebook):
            self.extend(other)
            return self
        elif isinstance(other, str):
            collected = args["collected"]
            self.append({"collected": collected, "note": other})
            return self
        else:
            raise TypeError

    def __iadd__(self, other, *args, **kwargs):
        return self.__add__(other, *args, **kwargs)
