# Third party imports
import pkg_resources

if __name__ == "__main__":
    for pkg in pkg_resources.working_set:
        print(pkg)
