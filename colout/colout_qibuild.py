
def theme():
    # CMake theme:
    #  actions performing in cyan
    performing="cyan"
    #  actions performed in green
    performed="green"
    #  actions taking an unknown time
    untimed="blue"

    return [
	# qibuild configure
	[ "^(Current build worktree:) (.*/)([^/]+)$", "214,154,154", "normal,normal,bold" ],
        [ "^(Using toolchain:) (.*)$", "214,154", "normal,bold" ],
        [ "^(Build type:) (.*)$", "214,154", "normal,bold" ],
        [ "^(\* \( *[0-9]+/[0-9]+\)) (Configuring) (.*)", "197,214,154", "bold,normal,bold" ],
        # qibuild warning
        [ "^(\[WARN \]:) (.*)", "red", "normal,bold" ],
        [ "^-- Library: (.*)$", "yellow", "bold" ],
        [ "^-- Binary: (.*)$", "154", "bold" ],
        # Configure
        [ "^-- (The) (.* compiler) (identification is) (.*)$", "117", "normal,bold,normal,bold" ],
        [ "^-- (Check for working) ([^ ]+ compiler): (.*/)([^/]+)( -- works)$", "117", "normal,bold,normal,bold" ],
        [ "^-- (Detecting) ([^ ]+ compiler ABI info - done)$", "117", "normal,bold" ],
        [ "^-- (Looking for include files) ([^ ]+) (- found)$", "117", "normal,bold" ],
        [ "^-- (Looking for include files) ([^ ]+) (- not found)$", "red", "normal,bold" ],
        [ "^-- (Looking for) ([^ ]+) (in) (.*) (- found)$", "117", "normal,bold,normal,normal,bold" ],
        [ "^-- (Looking for) ([^ ]+) (in) (.*) (- not found)$", "red", "normal,bold,normal,normal,bold" ],
        [ "^-- (Looking for) ([^ ]+) (- found)$", "117", "normal,bold" ],
        [ "^-- (Looking for) ([^ ]+) (- not found.)$", "red", "normal,bold" ],
        [ "^-- (Configuring done)$", "117", "bold" ],
        [ "^-- (Generating done)$", "117", "bold" ],
        [ "^-- (Build files have been written to:) (.*/)([^/]+)$", "135", "bold,normal,bold" ],
        [ "^-- (Using) (.*)$", "135", "normal,bold" ],
        [ "^-- (Build Options:)$", "135", "bold" ],
        [ "^-- (WITH_.* : .*)$", "135", "bold" ],
        [ "^-- (Found) (.*): (.*) (\(found version) (.*)(\))$", "117", "normal,bold,bold,normal,bold,normal" ],
        # Build
        [ "^(\* \( *[0-9]+/[0-9]+\)) (Building) (.*)", "197,214,154", "bold,normal,bold" ],
        [ "^(Scanning dependencies of target) (.*)$", "white", "normal,bold" ],
        [ "^\[\s*[0-9]+%\]\s(Building \w* object)(\s+.*/)([-\w]+.c.*)(.o)$", "117", "normal,normal,bold,bold"],
        [ "^\[\s*[0-9]+%\]\s(Built target)(\s.*)$", "214,154", "normal,bold" ],
        [ "^(Linking .*) (shared library|library|executable) (.*/)*(.+(\.[aso]+)*)$", "white", "normal,normal,normal,bold,bold" ],
        [ "^\[\s*[0-9]+%\]\s(Generating)(\s+.*)$", "white", "normal" ],
        # 
        [ "^-- Found.*NO", "red" ],
        [ "^--.*broken", "red" ],
        [ "^-- Coult NOT find.*", "red" ],
        [ "^-- Configuring incomplete, errors occurred!", "red" ],
        #[ "^--.*", performing ],
        # Errors
        [ "CMake Error:", "red" ],
        [ "CMake Warning", "yellow" ],
        # Scan
        #[ "^(Scanning dependencies of target)(.*)$",
        #  performing, "normal,bold" ],
        # Link
        #[ "^(Linking .* )(library|executable) (.*/)*(.+(\.[aso]+)*)$",
        #  untimed, "normal,normal,bold" ],
        # [percent] Built
        #[ "^\[\s*[0-9]+%\]\s(Built target)(\s.*)$",
        #  performed, "normal,bold" ],
        # [percent] Building
        #[ "^\[\s*[0-9]+%\]\s(Building \w* object)(\s+.*/)([-\w]+.c.*)(.o)$",
        #    performing, "normal,normal,bold,normal"],
        # [percent] Generating
        #[ "^\[\s*[0-9]+%\]\s(Generating)(\s+.*)$",
        #    performing, "normal,bold"],
        # make errors
        [ "make\[[0-9]+\].*", "yellow"],
        [ "(make: \*\*\* \[.+\] )(.* [0-9]+)", "red", "normal,bold"],
        # progress percentage
        [ "^(\[\s*[0-9]+%\])","Scale" ]
    ]
