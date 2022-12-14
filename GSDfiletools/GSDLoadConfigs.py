import os
import json
import jsonschema

class LoadConfigs:
    def __init__(self, testing=False):
        # Set gsdconfig globals like pathnames
        # TODO: check for trailing slash at some point
        self.user_homedir_path = os.path.expanduser('~')
        self.gsdconfig_path = self.user_homedir_path + "/.gsdconfig"

        if os.path.exists(self.gsdconfig_path): 
            with open(self.gsdconfig_path, "r") as f:
                gsdconfig_data = json.load(f)

            if "gsd_database_path" in gsdconfig_data:
                self.gsd_database_path = gsdconfig_data["gsd_database_path"]
            else:
                print("ERROR: NO gsd_database_path set in ~/.gsdconfig")
                quit()

            if "gsd_tools_path" in gsdconfig_data:
                self.gsd_tools_path = gsdconfig_data["gsd_tools_path"]
            else:
                print("ERROR: NO gsd_tools_path set in ~/.gsdconfig")
                quit()

        else:
            print("ERROR: no ~/.gsdconfig file set, please create one, see comments in this script for details")
            quit()

    def get_gsd_database_path(self):
        return(self.gsd_database_path)

    def get_gsd_tools_path(self):
        return(self.gsd_tools_path)

class LoadJSONFile:
    def __init__(self, file):
        self.file = file
        self.file_path, self.file_name = os.path.split(os.path.realpath(self.file))
    def get_file_name(self):
        return(self.file_name)
    def get_file_path(self):
        return(self.file_path)
    def get_JSON_content(self):
        with open(self.file, 'r') as f:
            try:
                self.JSON_content = json.load(f)
            except ValueError as e:
                print("ERROR: " + self.file_path + "/" + self.file_name + " is not a valid JSON file")
                quit()
        return(self.JSON_content)

class IdentifyJSONDataType:
    def __init__(self, file_content):
        self.file_content = file_content
        print("checks filetype based on jsonschema")

    # returns: 
    # type: GSD/OSV/CVE/NVD, etc
    # subtype: REJECT/RESERVED/PUBLIC, OSV/CVE, NVD_FEED/NVD_INDIVIDUAL
    # namespace: namespace if applicable cve.org/nvd.nist.gov/mozilla.org, etc.
    # version 4.0/5.0/1.0.0/1.2.0/1.3.0/etc.

    def check_JSON_keys(self):
    # GSD
        if "gsd" in self.file_content:
            print("GSD")

    # OSV
        if "schema_version" in self.file_content:
            print("OSV")

    # CVE
        if "data_type" in self.file_content:
            if self.file_content["data_type"] == "CVE"
                print("CVE")

    # NVD
        print("NVD")
        
    def check_JSON_schema(self):
        print("Checks against JSON schemas to find most likely fit")


class CheckJSONSchemaType:
    def __init__(self, file_content):
        print("checks filetype based on jsonschema")
