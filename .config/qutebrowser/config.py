config.set("colors.webpage.darkmode.enabled", True)
config.load_autoconfig()
config.bind(',M', 'hint links spawn mpv --profile=qutebrowser {hint-url}')
config.bind(',I', 'hint images download')
config.bind(',i', 'hint images spawn feh {hint-url}')

config.set("fileselect.handler", "external")
config.set("fileselect.single_file.command", ['alacritty', '--class', 'ranger,ranger', '-e', 'ranger', '--choosefile', '{}'])
config.set("fileselect.multiple_files.command", ['alacritty', '--class', 'ranger,ranger', '-e', 'ranger', '--choosefiles', '{}'])
