
import os
import sprout
from sprout.ctx import extend_field

def sprout_add_sources(s, adder):
    sprout.ctx.extend_field(s, 'sources', adder, transformer=sprout.ctx.path_from_base)

def sprout_add_includes(s, adder):
    sprout.ctx.extend_field(s, 'includes', adder, transformer=sprout.ctx.path_from_base)

def sprout_add_defines(s, adder):
    sprout.ctx.extend_field(s, 'defines', adder)

# Convenience functions for default target
def add_sources(adder):
    sprout_add_sources('default', adder)

def add_includes(adder):
    sprout_add_includes('default', adder)

def add_defines(adder):
    sprout_add_defines('default', adder)

def add_subdirectory(new_pwd, **kwargs):
    assert os.path.isdir(new_pwd)
    prev_pwd = os.getcwd()
    os.chdir(new_pwd)
    with open('sproutfile.py', 'r') as sproutfile:
        exec(sproutfile.read())
    os.chdir(prev_pwd)
