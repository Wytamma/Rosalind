import os
from importlib import import_module

solutions = {
    f[:-3]: import_module(f".{f[:-3]}", "bioinformatics_stronghold")
    for f in os.listdir("bioinformatics_stronghold")
    if f.endswith(".py")
}
