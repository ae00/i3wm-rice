config.set("colors.webpage.darkmode.enabled", True)
config.load_autoconfig()
config.bind(',M', 'hint links spawn mpv --profile=qutebrowser {hint-url}')
