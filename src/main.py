from getter import Api


def main():
    api = Api()
    api.get_global_stats()
    api.get_country_stats()

if __name__ == "__main__":
    main()
