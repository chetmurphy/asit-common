# Application Global Variables
# This module serves as a way to share variables across different
# modules (global variables).

import os

# Gets the name of the add-in from the name of the folder the py file is in.
# This is used when defining unique internal names for various UI elements 
# that need a unique name. It's also recommended to use a company name as 
# part of the ID to better ensure the ID is unique.
ADDIN_NAME = 'ASIT'
COMPANY_NAME = 'NEQ1'

class PaletteIds():
    ASIT_CMD_PALETTE_ID = f'{COMPANY_NAME}_{ADDIN_NAME}_asit_cmd_palette_id'
    ASIT_EDITOR_PALETTE_ID = f'{COMPANY_NAME}_{ADDIN_NAME}_asit_editor_palette_id'

# Command IDs
class CommandIds:   
    base_CMD_Id = f'{COMPANY_NAME}_{ADDIN_NAME}_CMD_ID_'
    launch_CMD_Id = base_CMD_Id + 'Launch'
    NewAsitDocument = base_CMD_Id + 'NewAsitDocument'
    OpenAsitDocument = base_CMD_Id + 'NewAsitDocument'
    
class CommandNames:   
    launch_CMD_Id = 'Launch'

WORKSPACE_ID = 'FusionSolidEnvironment'
class Events():
    send_html_event_id =  f'{COMPANY_NAME}_{ADDIN_NAME}_send_html_event_id'
    post_info_html_event_id =  f'{COMPANY_NAME}_{ADDIN_NAME}_post_info_html_event_id'
    post_command_event_id =  f'{COMPANY_NAME}_{ADDIN_NAME}_post_command_event_id'
    post_future_event_id =  f'{COMPANY_NAME}_{ADDIN_NAME}_post_future_event_id'
    
class Menu():
    file_commands = 'File'
    edit_commands = 'Edit'
    run_commands = 'Run'
    NewAsitDocument = 'New..'
    
class MenuDescription():
    NewAsitDocument = 'Create a new ASIT document'

