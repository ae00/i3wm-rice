config.set("colors.webpage.darkmode.enabled", True)
config.load_autoconfig()
config.bind(',M', 'hint links spawn mpv --profile=qutebrowser {hint-url}')
config.bind(',I', 'hint images download')
config.bind(',i', 'hint images spawn feh {hint-url}')
