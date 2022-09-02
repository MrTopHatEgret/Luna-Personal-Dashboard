from Backend.ReturnTypes import *


def process(text: str) -> ReturnTypeBase:
    # TODO: Using nlp, extract keyword befitting of each function and then pass on the arguments to said function
    data = TestTypeData(text)

    return data
