from pandera import Check, Column, DataFrameSchema

ROL_SCHEMA = DataFrameSchema({
    "PROCEDIMENTO": Column(str),
    "RN": Column(str, nullable=True),
    "VIGÊNCIA": Column(str, nullable=True),
    "Seg. Odontológica": Column(str, nullable=True),
    "Seg. Ambulatorial": Column(str, nullable=True),
    "HCO": Column(str, nullable=True),
    "HSO": Column(str, nullable=True),
    "REF": Column(str, nullable=True),
    "PAC": Column(str, nullable=True),
    "DUT": Column(float, nullable=True),
    "SUBGRUPO": Column(str),
    "GRUPO": Column(str),
    "CAPÍTULO": Column(str)
})