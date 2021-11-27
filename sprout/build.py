
import sprout
import sprout.ctx
import os

outfile_header = """
cflags = {}

rule cc
  deps = gcc
  depfile = $out.d
  command = gcc -MD -MF $out.d $cflags -c $in -o $out

rule link
  command = gcc $in -o $out

"""

def run(ctx, build_dir='build'):
    os.makedirs(build_dir, exist_ok=True)
    os.chdir(build_dir)

    flattened = sprout.ctx.get_flatteoned_sprouts()
    sources = flattened.get_sources()
    includes = ['-I../' + inc for inc in flattened.get_includes()]
    c_flags = flattened.get_c_flags()

    with open('build.ninja', 'w') as outfile:
        outfile.write(outfile_header.format(' '.join(c_flags + includes)))

        outputs = []
        for source in sources:
            if os.path.dirname(source):
                os.makedirs(os.path.dirname(source), exist_ok=True)
            output = source.replace('.c', '.o')
            outputs.append(output)
            outfile.write(f'build {output}: cc ../{source}\n')
            # line = 'gcc ' + ' '.join(includes) + ' -c ../' + source + ' -o ' + source.replace('.c', '.o')
            # print(line)
            # os.system(line)

        outfile.write(f'build target: link {" ".join(outputs)}\n')
        outfile.write(f'default target\n')
    # line = 'gcc ' + ' '.join(outputs) + ' -o ' + 'target'
    # os.system(line)
