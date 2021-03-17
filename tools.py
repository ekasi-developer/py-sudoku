class Tools:
    @staticmethod
    def in_array(value, array: list) -> bool:
        for element in array:
            if element == value:
                return True
        return False
