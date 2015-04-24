
def theme():
    subdued = "black"  # e.g. 242
    neutral = "white"  # e.g. 117
    info    = "cyan"   # e.g. 117
    error   = "red"    # e.g. 197
    warning = "blue"   # e.g. 214
    summary = "yellow" # e.g. 230

    section_label="blue"   # e.g. 214
    section_title="green"  # e.g. 154

    return [
        # qideploy config
        [ "^The following projects\s*$", section_label, "normal" ],
        [ "^and the following packages\s*$", section_label, "normal" ],
        [ "^ (\*) ([\w\-]+)\s*$", ",".join([section_label,section_title]), "normal,bold" ],
        [ "^will be deployed to", section_label, "normal" ],
        [ "^::\s+Deploying (?:projects|packages)\s*$", section_label, "reverse" ],
        # qideploy progress
        [ "^\* (\( *[0-9]+/[0-9]+\)) (Deploying package) ([\w]+) to ", ",".join(["red", section_label, section_title]), "bold" ],
        [ "^(\* \( *[0-9]+/[0-9]+\)) (Deploying project) (.*) to ", ",".join(["red", section_label, section_title]), "bold" ],
        [ "^-- (Install (?:configuration|component):) \"(.*)\"$", ",".join([section_label,section_title]), "normal,bold" ],
        [ "^-- (Up-to-date:) ([^\s]+/)(.*)$", ",".join([neutral]), "normal,normal,bold" ],
        [ "^-- (Installing:) ([^\s]+/)(.*)$", ",".join([info,neutral,info]), "normal,normal,bold" ],
        [ "^sending incremental file list$", section_label, "reverse" ],
        [ "^([^\s]+/)([^:\s])$", ",".join([neutral, info]), "normal,bold" ],
        [ "\s+\d+\s+\d{1,3}%\s+(\d{1,3}\.\d{2}\wB/s)\s+\d{1,2}:\d{2}:\d{2}\s+\(xfer#\d{1,4}, to-check=(\d+/\d+)\)\s*", ",".join([neutral,"Scale"]), "bold" ],
        [ "^sent \d+ bytes\s+received \d+ bytes\s+(\d+\.\d{2} bytes/sec)$", summary, "bold" ],
        [ "^total size is (\d+)\s+speedup is (\d+\.\d{2})$", summary, "bold" ],
        # Generic
        [ "\s(\w+)(@)(\w+)(:)(\w+)\s", "magenta", "normal,normal,bold,normal,normal" ]
    ]
