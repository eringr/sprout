
import os
from sprout.sprout import Sprout

def get_default_ctx():
    return {
        'base_dir': '',
        'sprouts': {
            'default': Sprout(),
        },
    }

_g_ctx = get_default_ctx()

def reset_context():
    global _g_ctx
    _g_ctx = get_default_ctx()

def sprout_context(func):
    global _g_ctx
    def wrapped(*args, **kwargs):
         ret = func(_g_ctx, *args, **kwargs)
         return ret
    return wrapped

@sprout_context
def get_ctx(ctx):
    return ctx

@sprout_context
def set_base(ctx):
    ctx['base_dir'] = os.getcwd()

@sprout_context
def path_from_base(ctx, path):
    if os.path.isabs(path):
        return path
    common = os.path.commonpath([ctx['base_dir'], os.getcwd()])
    return os.path.normpath(os.path.join(os.getcwd()[len(common):], path)).strip('/')

@sprout_context
def extend_field(ctx, name, field, extender, transformer=lambda x: x):
    s = ctx['sprouts'].get(name, Sprout())
    ctx['sprouts'][name] = s
    s.extend_field(field, extender, transformer)

@sprout_context
def get_sprout(ctx, name):
    return ctx['sprouts'].get(name, None)

@sprout_context
def get_flattened_sprouts(ctx):
    ret = Sprout()
    for s in ctx['sprouts'].values():
        ret.extend_sprout(s)
    return ret
