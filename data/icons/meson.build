pkgdatadir = join_paths(get_option('prefix'), get_option('datadir'), meson.project_name())

application_id = 'io.github.hakandundar34coding.system-monitoring-center'

scalable_apps_dir = join_paths('hicolor', 'scalable', 'apps')
install_data([
    'apps/io.github.hakandundar34coding.system-monitoring-center.svg',
    ],
    install_dir: join_paths(get_option('datadir'), 'icons', scalable_apps_dir)
)

scalable_apps_theme_dir = join_paths('hicolor', 'scalable', 'apps')
install_data([
    'apps/system-monitoring-center.svg',
    ],
    install_dir: join_paths(pkgdatadir, 'icons', scalable_apps_theme_dir)
)

actions_icons = files(
  run_command(
    'find', 'actions', '-name', '*.svg', check: true
  ).stdout().strip().split('\n')
)

scalable_actions_theme_dir = join_paths('hicolor', 'scalable', 'actions')
install_data(actions_icons,
    install_dir: join_paths(pkgdatadir, 'icons', scalable_actions_theme_dir),
)
