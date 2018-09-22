import argparse
import os


class RemoveLocked:

    list_of_folder = []
    list_of_cwd_folder = []
    filtered_list = []

    def argument_parser(self):
        parser = argparse.ArgumentParser(description="Remove locked files from the folders listed on this input file")
        parser.add_argument("-f", "--file", type=str, help="filename to read folder names from", required=True)
        args = parser.parse_args()
        return args

    def read_lines(self):
        input_filename = self.argument_parser()
        with open(input_filename.file) as f:
            for item in f:
                stripped_item = item.strip('\n')
                self.list_of_folder.append(stripped_item)
            return self.list_of_folder

    def check_folder(self):
        line_list = self.read_lines()
        pwd_folders = os.listdir(os.getcwd())
        for line in line_list:
            if line in pwd_folders:
                folder = os.path.join(os.getcwd(),line)
                self.filtered_list.append(folder)

            else:
                print("{} folder is not in the current working directory".format(line))
        return self.filtered_list

    def remove_locked_file(self):
        removal_folder = self.check_folder()
        filename = "locked"
        for folder in removal_folder:
            full_path = os.path.join(folder,filename)
            if os.path.exists(full_path):
                print("{0} file is present in {1} and will be deleted ". format(filename,folder))
                os.remove(full_path)
                print("{} has been deleted ".format(full_path))
            else:
                print("{0} file is not present in {1}". format(filename,folder))


