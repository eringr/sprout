
import schema

sprout_schema = schema.Schema({
    'c_flags': [str],
    'linker_flags': [str],
    'sources': [str],
    'includes': [str],
    'defines': [str],
    'libraries': [str],
})

class Sprout:
    def __init__(self):
        self.bom = {
            'c_flags': [],
            'linker_flags': [],
            'sources': [],
            'includes': [],
            'defines': [],
            'libraries': [],
        }

    def extend_field(self, field, extender, transformer=lambda x: x):
        if field not in self.bom:
            self.bom[field] = []
        if isinstance(extender, list):
            for f in extender:
                self.bom[field].append(transformer(f))
        else:
            self.bom[field].append(transformer(extender))
        self.validate()

    def validate(self):
        sprout_schema.validate(self.bom)

    def extend_sprout(self, r):
        for field in r.bom:
            self.extend_field(field, r.bom[field])

    def contains_source(self, name):
        return name in self.bom['sources']

    def contains_include(self, name):
        return name in self.bom['includes']

    def contains_define(self, name):
        return name in self.bom['defines']

    def get_c_flags(self):
        return self.bom['c_flags']

    def get_includes(self):
        return self.bom['includes']

    def get_sources(self):
        return self.bom['sources']

    def get_defines(self):
        return self.bom['defines']
