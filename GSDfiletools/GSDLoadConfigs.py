import os
import json

class GSDLoadConfigs:
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
