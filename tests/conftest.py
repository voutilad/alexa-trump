from dotenv import load_dotenv

# Inspired by https://github.com/MobileDynasty/pytest-env
def pytest_addoption(parser):
    parser.addini("dotenv",
                  type="linelist",
                  help="List of files to source for environment variables",
                  default=[".env"])

def pytest_configure(config):
    for e in config.getini("dotenv"):
        try:
            load_dotenv(e)
        except Exception:
            print("error loading environment vars from: " + e)
