# DesktopCleanAuto - AI Coding Instructions

## Project Overview
A complete Python desktop automation tool for organizing Rust server mod files (`.cs` plugin files). The tool scans a directory, creates organized folder structures, moves files into appropriate folders, and cleans up empty directories.

## Core Architecture

### Main Components
- **`DesktopCleaner.py`**: Complete single-file application with full file organization workflow
- **Target Directory**: `'c:/Users/admin/Desktop/Rust server mods'` - source location for Rust plugins
- **Output Structure**: Creates `{PluginName}.cs folder/` directories and moves files into them

### Key Functions (Execution Order)
1. `convert_date(timestamp)`: Converts Unix timestamps to readable format (`'%d %b %Y'`)
2. `plugin_files(basepath)`: Lists and displays file/directory info using `os.scandir()`
3. `create_plugin_folders(basepath, plugins_files)`: Creates folders with existence checks
4. `move_files_to_folders(basepath, plugins_files)`: Moves .cs files into their respective folders
5. `delete_empty_folders(basepath)`: Removes empty directories after file organization

## Implementation Patterns

### File Operations
- **Consistent API**: Uses `os.scandir()` throughout for performance and metadata access
- **Path Handling**: Uses `os.path.join()` for cross-platform compatibility
- **Error Prevention**: Includes `os.path.exists()` checks before operations
- **File Moving**: Uses `os.rename()` for efficient file relocation

### Workflow Architecture
```python
# Sequential execution pattern:
plugin_files(basepath)                           # 1. List and display files
create_plugin_folders(basepath, os.scandir())   # 2. Create folder structure
move_files_to_folders(basepath, os.scandir())   # 3. Move files to folders
delete_empty_folders(basepath)                  # 4. Clean up empty folders
```

### Safety Features
- **Existence Checks**: Verifies folders exist before moving files
- **Empty Folder Validation**: Uses `os.listdir()` to check before deletion
- **Path Construction**: Always uses `os.path.join()` for proper path building
- **Detailed Logging**: Prints every operation for transparency

## Development Guidelines

### Adding New Features
1. Follow the `os.scandir()` pattern for directory iteration
2. Use `os.path.join(basepath, ...)` for all path construction
3. Add existence checks before file/folder operations
4. Include descriptive print statements for all actions

### Error Handling Opportunities
- Add try-catch blocks around `os.mkdir()`, `os.rename()`, `os.rmdir()`
- Handle permission errors and file locks
- Validate target directory existence before execution
- Implement rollback mechanisms for failed operations

### Testing Approach
- Test with various .cs file types (plugins, extensions, zips)
- Verify behavior with existing folder structures
- Test edge cases: special characters, long filenames, permission issues
- Validate cleanup of truly empty vs non-empty folders

## Critical Implementation Details
- **Complete Workflow**: All core functionality is implemented and functional
- **Path Safety**: Uses forward slashes but `os.path.join()` handles OS differences
- **Rust Context**: Designed for Oxide/uMod plugin files (.cs) from Rust game servers
- **Sequential Execution**: Functions run in specific order to ensure proper organization
- **No External Dependencies**: Uses only Python standard library

## Execution Flow
The script runs automatically when executed - no user interaction required. It processes all .cs files in the target directory through the complete organization workflow.

When extending this codebase, maintain the simple, sequential execution pattern and comprehensive logging for transparency.
