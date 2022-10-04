#!/usr/bin/env python3

import os
import sys
import GSDfiletools

###################
#
# Standard stuff
#
###################


if __name__ == "__main__":
    
    gsd_config = GSDfiletools.LoadConfigs()
    
    print("gsd_database_path: " + gsd_config.get_gsd_database_path())
    print("gsd_database_path: " + gsd_config.get_gsd_tools_path())

    filename =  sys.argv[1]

    file_path, file_name = os.path.split(os.path.realpath(sys.argv[0]))
    print("file_name: " + file_path)

    gsd_file = GSDfiletools.LoadJSONFile(filename)
    gsd_file_content = gsd_file.get_JSON_content()
    print("full_path: " + gsd_file.get_file_path())

    print(gsd_file_content)