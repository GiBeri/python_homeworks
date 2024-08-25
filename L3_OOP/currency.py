class Currency:
    dict1 = {"USD": 2.68, "EUR": 2.88, "GEL": 1}

    def __init__(self, value: float, unit: str = "GEL") -> None:
        self.value = value
        self.unit = unit

    def __str__(self) -> str:
        return f"{self.value} {self.unit}"

    def change_to(self, unit: str):
        new_value = self.value / dict1.get(unit)
        return f"{new_value} {unit}"

    def 