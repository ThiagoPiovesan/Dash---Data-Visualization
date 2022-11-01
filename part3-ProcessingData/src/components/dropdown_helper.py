def to_dropdown_options(values: "list[str]"):
    return [{"label": value, "value": value} for value in values]
