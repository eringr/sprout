
import os
import argparse
import sprout

parser = argparse.ArgumentParser()

parser.add_argument('-C', type=str, nargs=1)

args = parser.parse_args()

print(args)
if args.C:
    os.chdir(args.C[0])

sprout.ctx.set_base()

sprout.add_subdirectory('.')

sprout.build.run(sprout.ctx.get_ctx())
