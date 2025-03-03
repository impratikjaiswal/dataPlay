from python_helpers.ph_keys import PhKeys
from python_helpers.ph_modes_execution import PhExecutionModes


class TestData:
    # Unit Testing Sequences
    dynamic_data = {
        PhExecutionModes.UNIT_TESTING:
            {
                PhKeys.VAR_EXECUTION_MODE: 'UNIT_TESTING',
            },
        PhExecutionModes.USER:
            {
                PhKeys.VAR_EXECUTION_MODE: 'USER',
            },
        PhExecutionModes.SAMPLES_LIST:
            {
                PhKeys.VAR_EXECUTION_MODE: 'SAMPLES_LIST',
            },
        PhExecutionModes.DEV:
            {
                PhKeys.VAR_EXECUTION_MODE: 'DEV',
            },
        PhExecutionModes.KNOWN_ISSUES:
            {
                PhKeys.VAR_EXECUTION_MODE: 'KNOWN_ISSUES',
            },
        PhExecutionModes.UNIT_TESTING_EXTERNAL:
            {
                PhKeys.VAR_EXECUTION_MODE: 'UNIT_TESTING_EXTERNAL',
            },
        PhExecutionModes.ALL:
            {
                PhKeys.VAR_EXECUTION_MODE: 'ALL',
            },
    }

    dynamic_data_cli = {
        'no_param':
            {
                PhKeys.BATCH_PARAMS: '',
            },
        '--help':
            {
                PhKeys.BATCH_PARAMS: '--help',
            },
    }

    read_me_cli_pool = [
    ]

    dynamic_data_default = {
        PhKeys.VAR_EXECUTION_MODE: 'ALL',
        PhKeys.VAR_ERROR_HANDLING_MODE: 'CONTINUE_ON_ERROR',
        PhKeys.VAR_TOP_FOLDER_PATH: '[]',
    }

    dynamic_data_cli_default = dynamic_data_default.copy()
    dynamic_data_cli_default.update({PhKeys.VAR_EXECUTION_MODE: 'USER'})

    @classmethod
    def generate_dynamic_cli_from_read_me(cls):
        for index, batch_param in enumerate(TestData.read_me_cli_pool):
            TestData.dynamic_data_cli.update({f'read_me_{index}': {PhKeys.BATCH_PARAMS: f'"{batch_param}"'}})
