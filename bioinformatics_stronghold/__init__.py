import os
from importlib import import_module

package = "bioinformatics_stronghold"

solutions = {
    f[:-3]: import_module(f".{f[:-3]}", package)
    for f in os.listdir(package)
    if f.endswith(".py")
}
