import json

OUTPUT_PATH = "../LFXX/"
ROOT_PATH = ""

PROFILE_SETTINGS = json.load(open("profile_settings.json"))
SECTOR_FILES = json.load(open("sector_files_name.json"))
SETTINGS = json.load(open("settings.json"))
PLUGIN_SETTINGS = json.load(open("plugin_settings.json"))
PROFILE_TEMPLATE = open("profile_template.txt").read()

for profile in PROFILE_SETTINGS:
    content = PROFILE_TEMPLATE

    content = content.replace("$ROOT_PATH$", ROOT_PATH)

    # Sector file
    sector_filename = SECTOR_FILES[profile["sector"]]
    content = content.replace("$SECTOR$", f"Settings	sector	\\{sector_filename}")

    # Settings
    settings_content = []
    for setting in SETTINGS:
        settings_content.append(f"Settings	{setting}	{ROOT_PATH}\\Settings\\{SETTINGS[setting]}")
    content = content.replace("$SETTINGS$", "\n".join(settings_content))
    content = content.replace("$FIR$", profile["sector"])

    # Recent files
    recent_files_content = []
    n = 1
    for recent in profile["recentFiles"]:
        recent = recent.replace("/", "\\") # replace slash with anti-slash
        recent_files_content.append(f"RecentFiles	Recent{n}	{ROOT_PATH}\\ASR\\{recent}")
        n += 1
    content = content.replace("$RECENTFILES$", "\n".join(recent_files_content))

    # Plugins
    plugins_content = open(PLUGIN_SETTINGS[profile["plugins"]]).read()
    content = content.replace("$PLUGINS$", plugins_content.rstrip())

    with open(OUTPUT_PATH + profile["name"] + ".prf", "w") as f:
        f.write(content)