# Standard Library Imports
from dataclasses import dataclass, field, fields
from typing import Optional

# Third Party Imports
from pandas import DataFrame

try:
    # Standard Library Imports
    from importlib.metadata import metadata, packages_distributions, version
except ImportError:
    # Third Party Imports
    from importlib_metadata import metadata, packages_distributions, version


def none_on_fail(fn):
    # Standard Library Imports
    from functools import wraps

    @wraps(fn)
    def wrapper(self, *args, **kw):
        try:
            return fn(self, *args, **kw)
        except Exception:
            return None

    return wrapper


@none_on_fail
def get_metadata(p):
    return metadata(p)


@none_on_fail
def get_field(meta, f):
    return meta.json.get(f)


@dataclass(frozen=True)
class Package:
    name: str
    summary: Optional[str] = field(default=None)
    license: Optional[str] = field(default=None)
    home_page: Optional[str] = field(default=None)
    version: Optional[str] = field(default=None)

    @classmethod
    def from_pkg(cls, p):
        meta = get_metadata(p)
        return (
            Package(**{f.name: get_field(meta, f.name) for f in fields(cls)})
            if meta
            else Package(name=p)
        )


def build_markdown_table():
    return DataFrame(
        data=[Package.from_pkg(p) for p in packages_distributions()],
        columns=[f.name for f in fields(Package)],
    ).to_markdown()


if __name__ == "__main__":
    print(build_markdown_table())
