""" define generic base classes for pandas objects """


# define abstract base classes to enable isinstance type checking on our
# objects
def create_pandas_abc_type(name, attr, comp):
    @classmethod
    def _check(cls, inst):
        return getattr(inst, attr, '_typ') in comp

    dct = dict(__instancecheck__=_check, __subclasscheck__=_check)
    meta = type("ABCBase", (type, ), dct)
    return meta(name, tuple(), dct)


ABCIndex = create_pandas_abc_type("ABCIndex", "_typ", ("index", ))
ABCInt64Index = create_pandas_abc_type("ABCInt64Index", "_typ",
                                       ("int64index", ))
ABCFloat64Index = create_pandas_abc_type("ABCFloat64Index", "_typ",
                                         ("float64index", ))
ABCDatetimeIndex = create_pandas_abc_type("ABCDatetimeIndex", "_typ",
                                          ("datetimeindex", ))
ABCCategoricalIndex = create_pandas_abc_type("ABCCategoricalIndex", "_typ",
                                             ("categoricalindex", ))
ABCIndexClass = create_pandas_abc_type("ABCIndexClass", "_typ",
                                       ("index", "int64index",
                                        "float64index", "datetimeindex",
                                        "categoricalindex"
                                        ))

ABCSeries = create_pandas_abc_type("ABCSeries", "_typ", ("series", ))
ABCDataFrame = create_pandas_abc_type("ABCDataFrame", "_typ", ("dataframe", ))
ABCCategorical = create_pandas_abc_type("ABCCategorical", "_typ",
                                        ("categorical"))
ABCDatetimeArray = create_pandas_abc_type("ABCDatetimeArray", "_typ",
                                          ("datetimearray"))
ABCExtensionArray = create_pandas_abc_type("ABCExtensionArray", "_typ",
                                           ("extension",
                                            "categorical",
                                            "datetimearray",
                                            ))
ABCPandasArray = create_pandas_abc_type("ABCPandasArray",
                                        "_typ",
                                        ("npy_extension",))


class _ABCGeneric(type):

    def __instancecheck__(cls, inst):
        return hasattr(inst, "_data")


ABCGeneric = _ABCGeneric("ABCGeneric", tuple(), {})