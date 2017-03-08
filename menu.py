import fire

class Menu(object):
    def get(self, item):
        return ["spam", "spam", item, "spam"]

if __name__ == '__main__':
    fire.Fire(Menu)