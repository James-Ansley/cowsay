# Changelog

All notable changes to this project will be documented in this file.

## [1.2.0]

### Additions

- Added `cowsay` and `cowthink` command line programs.
- Added a `--random` flag to the `cowsay` and `cowthink` programs.
  This is a non-standard option, but allows for the easy selection of
  random cows.

### Changes

- Any string variable declarations in `.cow` files are now inlined in the cow.
- `python-cowsay` now looks for a `COWPATH` environment variable, if found,
  the directory this references will be used when loading cows.
- Changed cows back to original cowsay cows.

[1.2.1]: https://github.com/James-Ansley/pipe-utils/compare/v1.1.1...v1.2.0
