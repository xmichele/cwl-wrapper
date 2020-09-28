from yaml import full_load as load_yaml_file


class Rulez:
    stagein_out = ''
    stageout_file = ''
    stagein_file = ''
    driver = ''

    def __init__(self, file_):
        with open(file_) as f:
            self.rulez = load_yaml_file(f)

        if 'parser' in self.rulez:
            if 'type' in self.rulez['parser']:
                self.parser_type = self.rulez['parser']['type']
            else:
                self.parser_type = '$graph'

        if 'stagein' in self.rulez:
            if 'file' in self.rulez['stagein']:
                self.stagein_file = self.rulez['stagein']['file']

        if 'stageout' in self.rulez:
            if 'file' in self.rulez['stagein']:
                self.stageout_file = self.rulez['stageout']['file']

        if 'driver' in self.rulez:
            self.driver = self.rulez['driver']
        else:
            self.driver = 'cwl'
