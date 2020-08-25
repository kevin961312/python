def get_pages(*links):
    for link in links:
    #download the link with urllib
        print(link)

print(get_pages(),
      get_pages('http://www.archlinux.org'),
      get_pages('http://www.archlinux.org','http://ccphillips.net/'))


class Options:
    default_options = {'port': 21,
                    'host': 'localhost',
                    'username': None,
                    'password': None,
                    'debug': False,
                    }

    def __init__(self, **kwargs):
        self.options = dict(Options.default_options)
        self.options.update(kwargs)

    def __getitem__(self, key):
        return self.options[key]

options = Options(username="dusty", password="drowssap",debug=True)

print(options['debug'])
print(options['port'])
print(options['username'])


import shutil
import os.path
def augmented_move(target_folder, *filenames,verbose=False, **specific):
    def print_verbose(message, filename):
        if verbose:
            print(message.format(filename))
        for filename in filenames:
            target_path = os.path.join(target_folder, filename)
            if filename in specific:
                if specific[filename] == 'ignore':
                    print_verbose("Ignoring {0}", filename)
                elif specific[filename] == 'copy':
                    print_verbose("Copying {0}", filename)
                    shutil.copyfile(filename, target_path)
            else:
                print_verbose("Moving {0}", filename)
shutil.move(filename, target_path)