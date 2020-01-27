def try_get_RJSeries(path):
    if (type(path) is not str):
        raise ValueError(path, path.__name__)
    series = next((substr for substr in path.split(' ') if "RJ" in substr.upper()), None)

    return series is not None, series