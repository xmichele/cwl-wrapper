from yaml import full_load as load_yaml_file


class Rulez:
    def __init__(self, file_):
        # self.prop = {}
        with open(file_) as f:
            self.rulez = load_yaml_file(f)

    def __getattr__(self, item):

        val = item.split('_')
        max = len(val)
        obj = self.rulez
        for i in range(max):
            if val[i] in obj and i == max - 1:
                super(Rulez, self).__setattr__(item, obj[val[i]])
                return obj[val[i]]
            else:
                obj = obj[val[i]]

        return ''
