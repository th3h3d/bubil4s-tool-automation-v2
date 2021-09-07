import os
import time
from utilities.utility_logger import UtilityLogger


class FileOperation:
    class_path = "file_operations.FileOperation"
    ulogger = UtilityLogger()

    @classmethod
    def load_all(cls, file_name):
        """?"""
        try:
            fo = open(os.path.join("./in_out", file_name), "r")
            lines = fo.readlines()
            fo.close()
            return lines
        except Exception as e:
            # Manual logger for logging
            cls.ulogger.log_this("{} -> load_all -> {}\n".format(str(time.strftime("%Y%m%d-%H:%M:%S - ", time.localtime())) + cls.class_path, str(e)))

    @classmethod
    def dump_all(cls, file_name, data):
        """?"""
        try:
            fo = open(os.path.join("./in_out", file_name), "w")
            fo.write(data)
            fo.close()
        except Exception as e:
            # Manual logger for logging
            cls.ulogger.log_this("{} -> dump_all -> {}\n".format(str(time.strftime("%Y%m%d-%H:%M:%S - ", time.localtime())) + cls.class_path, str(e)))

    @classmethod
    def merge_both(cls, new_source, solid_output):
        """?"""
        try:
            # new_source
            f1 = open(os.path.join("./in_out", new_source), "r")
            new_source_data = f1.readlines()
            f1.close()

            try:
                # solid_output
                f2 = open(os.path.join("./in_out", solid_output), "r")
                solid_output_data = f2.readlines()
                f2.close()
            except FileNotFoundError:
                # if file does not exist, create it!
                f2 = open(os.path.join("./in_out", solid_output), "w")
                f2.close()
                # re-do
                f2 = open(os.path.join("./in_out", solid_output), "r")
                solid_output_data = f2.readlines()
                f2.close()

            solid_output_data.extend(new_source_data)

            f2 = open(os.path.join("./in_out", solid_output), "w")
            f2.writelines(solid_output_data)
            f2.close()
        except Exception as e:
            # Manual logger for logging
            cls.ulogger.log_this("{} -> merge_both -> {}\n".format(str(time.strftime("%Y%m%d-%H:%M:%S - ", time.localtime())) + cls.class_path, str(e)))

    @classmethod
    def unique_them(cls, source_file_name):
        """?"""
        try:
            f1 = open(os.path.join("./in_out", source_file_name), "r")
            source_data = f1.readlines()
            f1.close()

            source_data = set(source_data)

            f2 = open(os.path.join("./in_out", source_file_name), "w")
            f2.writelines(source_data)
            f2.close()
        except Exception as e:
            # Manual logger for logging
            cls.ulogger.log_this("{} -> execute_shell_command -> {}\n".format(str(time.strftime("%Y%m%d-%H:%M:%S - ", time.localtime())) + cls.class_path, str(e)))

    @classmethod
    def merge_unique_sort(cls, new_source, solid_output):
        """?"""
        try:
            # new_source
            f1 = open(os.path.join("./in_out", new_source), "r")
            new_source_data = f1.readlines()
            f1.close()

            try:
                # solid_output
                f2 = open(os.path.join("./in_out", solid_output), "r")
                solid_output_data = f2.readlines()
                f2.close()
            except FileNotFoundError:
                # if file does not exist, create it!
                f2 = open(os.path.join("./in_out", solid_output), "w")
                f2.close()
                # re-do
                f2 = open(os.path.join("./in_out", solid_output), "r")
                solid_output_data = f2.readlines()
                f2.close()

            solid_output_data.extend(new_source_data)
            solid_output_data = list(set(solid_output_data))
            solid_output_data.sort()

            f2 = open(os.path.join("./in_out", solid_output), "w")
            f2.writelines(solid_output_data)
            f2.close()
        except Exception as e:
            # Manual logger for logging
            cls.ulogger.log_this("{} -> execute_shell_command -> {}\n".format(str(time.strftime("%Y%m%d-%H:%M:%S - ", time.localtime())) + cls.class_path, str(e)))

    @classmethod
    def clean_all(cls, file_name, data):
        """?"""
        try:
            cleaned_lines = ""
            data.append("\n")
            for row in cls.load_all(file_name):
                for value_to_clean in data: # iterate the list
                    row = row.replace(value_to_clean, "")
                cleaned_lines = cleaned_lines + row + "\n"
            cls.dump_all(file_name, cleaned_lines)

        except Exception as e:
            # Manual logger for logging
            cls.ulogger.log_this("{} -> clean_up -> {}\n".format(str(time.strftime("%Y%m%d-%H:%M:%S - ", time.localtime())) + cls.class_path, str(e)))
