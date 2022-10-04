#!/usr/bin/env python3

import GSDfiletools

gsd_config = GSDfiletools.GSDLoadConfigs()

print(gsd_config.get_gsd_database_path())
print(gsd_config.get_gsd_tools_path())
