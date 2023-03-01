# gsd-file-tools

This reads the following types of files:

GSD (mix of type)
OSV
CVE
NVD (CVE like)
GHSA (OSV)

And it can write the following types of file:

GSD (miv of types)
GSD in OSV format (lossy)
GSD in CVE format (lossy)

# Basic capabilities:

* Set configuration (dirs, files, etc.)
* Load files into memory and identify them (GSD, OSV, GHSA, etc.)
* Schema validation of files including "deep" validations (e.g. GSD, NVD) - validateFileSchema.py
* Add files into appropriate GSD namespaces (e.g. mozilla.org, GHSA) - addDataToFile.py
* Extract data from namespaces (e.g. mozilla.org) data and add to GSD area (used in convertFile.py)
* Generate GSD files (GSD, OSV and CVE formats) based on GSD files and older GSD files, OSV, CVE - convertFile.py
* Intelligently deal wth some of the obviously broken data like "** RESERVED **" and "n/a"

# Extended capabilities:

* Data values validation, e.g. correcting vendor names
* Verify that URLs are semi valid
* Allow listing of certain data changes based on content, e.g. reference sources with allowlisted domains (e.g. msrc.microsoft.com, theregister.co.uk)

## Reading files

Read file into the GSD data structure, the following are supported:

GSD-YEAR-INTEGER.json (GSD)
CVE-YEAR-INTEGER.json (CVE and NVD?)
GHSA-stuff.json (GHSA)

### GSD

```
{
    "gsd": {
        "cve_schema": {},
        "osv_schema": {}
    },
    {
        "namespace": {}
    },
    "GSD": {},
    "OSV: {},
}
```

### OSV 1.1.0 and later, if we encounter unversioned try 1.0.0/1.2.0/1.3.x, throw an error otherwise

{
    "format": "OSV"
}

### CVE 4.0

CVE 4.0 uses three main JSON schemas for PUBLIC, REJECT and RESERVED

#### CVE 4.0 PUBLIC

```
  "data_format": "MITRE",
  "data_type": "CVE",
  "data_version": "4.0",
  "CVE_data_meta": {
    "STATE": "PUBLIC"
  },
```

#### CVE 4.0 REJECT

```
  "data_format": "MITRE",
  "data_type": "CVE",
  "data_version": "4.0",
  "CVE_data_meta": {
    "STATE": "REJECT"   
  }
```

#### CVE 4.0 RESERVED

```
  "data_type": "CVE",
  "data_format": "MITRE",
  "data_version": "4.0",
  "CVE_data_meta": {
    "STATE": "RESERVED"
  }
```

### CVE 5.0

A single unified schema https://github.com/CVEProject/cve-schema/blob/master/schema/v5.0/CVE_JSON_5.0_schema.json

### NVD

Parse the CVE / CVSS stuff

### GHSA

TODO: check database_specific for other interesting data

{
    "format": "OSV"
    "database_specific": {
        "cwe_ids": [
        "CWE-1321"
        ],
        "severity": "MODERATE"
    }
}
