# Specifications Plugin

The `Specifications` plugin traces `Requirement`s of provided `Specification`s.  It does this through the `spec-csv` command, which generates a .csv file for a `Specification` which tracks its `Requirement`s.

## Spec-Csv Command
```bash
aac spec-csv architecture-file.aac output_directory
```

### Arguments

#### Architecture File
The AaC file containing the `Specification`s and `Requirement`s definitions.

#### Output Directory
The directory in which the .csv file will be generated.

## Plugin Usage Example

An Architecture File, `architecture_file.aac`, contains the following definitions:
```yaml
req_spec:
  name: Subsystem
  description:  This is a representative subsystem requirement specification.
  requirements:
    - "SUB-1"
  sections:
    - Other Requirements
---
req_spec:
    name: Other Requirements
    description: Other requirements
    requirements:
        - "SUB-2"
---
req:
    name: SUB-1
    id: "SUB-1"
    shall: When receiving a message, the subsystem shall respond with a value.
    attributes:
        - name: TADI
          value: Test
---
req:
    name: SUB-2
    id: "SUB-2"
    shall: Do things.
    attributes:
        - name: TADI
          value: Test
---
req_spec:
  name: Module
  description:  This is a representative module requirement specification.
  requirements:
    - "MOD-1"
    - "MOD-2"
---
req:
    name: MOD-1
    id: "MOD-1"
    shall:  When receiving a message, the module shall respond with a value.
    parents:
        - "SUB-1"
    attributes:
        - name: TADI
          value: Test
---
req:
    name: MOD-2
    id: "MOD-2"
    shall:  When receiving a message, do things.
    parents:
        - "SUB-2"
    attributes:
        - name: TADI
          value: Test
```
If you would like to generate a CSV file tracking the requirement relationships in the current directory, you would execute the following command:
```bash
aac spec-csv architecture-file.aac .
```
Which would return this in the command line:
![Run Spec-Csv in Command Line](../images/spec-csv_command_line.png)

It would also generate the following three CSV files:

`Module.csv`:
![Module CSV File](../images/Module_csv.png)

`Subsystem.csv`:
![Subsystem CSV File](../images/Subsystem_csv.png)

`Other_Requirements.csv`:
![Other_Requirements CSV File](../images/Other_Requirements_csv.png)
