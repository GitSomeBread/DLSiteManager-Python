import multiprocessing
import os
import Utils
from DLSiteHtmlParser import DLSiteHtmlParser
from functools import partial

def rename_directory(format, path):
    has_series, series = Utils.try_get_RJSeries(path)
    if not has_series:
        return None
        
    parser = DLSiteHtmlParser.LoadFromURL("http://www.google.com")
    new_path = format.upper()
    new_path = new_path.replace("<RJ>".upper(), series)
    new_path = new_path.replace("<CYCLE>".upper(), parser.cycle)
    new_path = new_path.replace("<NAME>".upper(), parser.product_name)
    new_path = new_path.replace("<SEIYUU>".upper(), "&".join(parser.seiyuus))

    star = "★"
    if star in path:
        new_path.replace(star, '')
        new_path += star

    print("new_path= " + new_path)
    os.renames(path, new_path)   
    return new_path

def rename_directories(format, *args):
    pool = multiprocessing.Pool(os.cpu_count())
    return pool.map_async(partial(rename_directory, format), args)

