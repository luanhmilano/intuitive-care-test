from pandera import Check, Column, DataFrameSchema

ROL_SCHEMA = DataFrameSchema({
    "PROCEDIMENTO": Column(str),
    "RN": Column(str, nullable=True),
    "VIGÊNCIA": Column(str),
    "OD": Column(str, checks=Check.isin(["S", "N"])),
    "AMB": Column(str, checks=Check.isin(["S", "N"])),
    "HCO": Column(str, nullable=True),
    "HSO": Column(str, nullable=True),
    "REF": Column(str),
    "PAC": Column(str),
    "DUT": Column(str),
    "SUBGRUPO": Column(str),
    "GRUPO": Column(str),
    "CAPÍTULO": Column(str)
})