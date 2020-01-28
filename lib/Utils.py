import os

def try_get_RJSeries(path):
    if (type(path) is not str):
        raise ValueError(path, path.__name__)

    base_path = os.path.basename(path)
    series = next((substr for substr in base_path.split(' ') if "RJ" in substr.upper()), None)
    return series is not None, series

def get_maniax_URL(RJSeries):
    return f"https://www.dlsite.com/maniax/work/=/product_id/{RJSeries}.html"

def get_home_URL(RJSeries):
    return f"https://www.dlsite.com/home/work/=/product_id/{RJSeries}.html"